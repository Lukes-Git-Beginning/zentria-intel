#!/usr/bin/env bash
# Wrapper fuer claude-CLI Routine-Runs.
#
# Usage:
#   .scripts/run-routine.sh <routine-name>
#
# - Liest das Modell aus settings.yaml > routines.<name>.model
# - Laedt .env (ANTHROPIC_API_KEY u.a.)
# - Ruft `claude -p` mit dem Routine-Prompt im Headless-Modus
#
# Wird von systemd via zentria-intel-routine@<name>.service aufgerufen,
# kann aber auch manuell ausgefuehrt werden.

set -euo pipefail

NAME="${1:?usage: $0 <routine-name>}"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PROMPT_FILE="${REPO_ROOT}/.routines/${NAME}.prompt.md"

if [[ ! -f "$PROMPT_FILE" ]]; then
    echo "ERROR: Prompt file not found: $PROMPT_FILE" >&2
    exit 2
fi

# .env laden falls vorhanden (set -a exportiert alles automatisch)
if [[ -f "${REPO_ROOT}/.env" ]]; then
    set -a
    # shellcheck disable=SC1091
    source "${REPO_ROOT}/.env"
    set +a
fi

if [[ -z "${ANTHROPIC_API_KEY:-}" && -z "${CLAUDE_CODE_OAUTH_TOKEN:-}" ]]; then
    echo "ERROR: weder ANTHROPIC_API_KEY noch CLAUDE_CODE_OAUTH_TOKEN gesetzt (in .env?)" >&2
    exit 3
fi

# Modell aus settings.yaml extrahieren via Python (PyYAML im pipeline-venv)
PYTHON_BIN="${REPO_ROOT}/.scripts/.venv/bin/python"
if [[ ! -x "$PYTHON_BIN" ]]; then
    PYTHON_BIN="$(command -v python3)"
fi

MODEL=$("$PYTHON_BIN" -c "
import yaml
with open('${REPO_ROOT}/settings.yaml', encoding='utf-8') as f:
    s = yaml.safe_load(f)
r = s.get('routines', {}).get('${NAME}', {})
print(r.get('model', 'claude-sonnet-4-6'))
")

MAX_OUTPUT=$("$PYTHON_BIN" -c "
import yaml
with open('${REPO_ROOT}/settings.yaml', encoding='utf-8') as f:
    s = yaml.safe_load(f)
r = s.get('routines', {}).get('${NAME}', {})
print(r.get('max_output_tokens', 25000))
")

cd "$REPO_ROOT"

# venv aktivieren — sodass der claude-Subprocess (Bash-Tool im Agent)
# automatisch die richtige Python-Umgebung mit feedparser/PyYAML/simhash/trafilatura
# nutzt. Andernfalls scheitert `python .scripts/fetch_all.py` an fehlenden Imports.
if [[ -f "${REPO_ROOT}/.scripts/.venv/bin/activate" ]]; then
    # shellcheck disable=SC1091
    source "${REPO_ROOT}/.scripts/.venv/bin/activate"
fi

echo "===== [$(date -Iseconds)] starting ${NAME} (model=${MODEL}, max_tokens=${MAX_OUTPUT}) ====="

# Headless: -p (print mode, ein-shot, exit nach finaler Assistant-Message)
# --dangerously-skip-permissions: kein interactive Permission-Prompt (Cron-Sandbox)
# --max-turns: hardcap, falls Routine sich verheddert
# Tools-Allowlist: alle die unsere Routinen nutzen (Bash fuer fetch_all, Web* fuer evtl. Direkt-Lookups)
claude -p "$(cat "$PROMPT_FILE")" \
    --model "$MODEL" \
    --permission-mode bypassPermissions \
    --max-turns 100 \
    --allowedTools "Bash,Read,Write,Edit,Glob,Grep,WebFetch,WebSearch"

EXIT_CODE=$?
echo "===== [$(date -Iseconds)] ${NAME} finished (exit=${EXIT_CODE}) ====="

# ---------------------------------------------------------------------------
# Auto-commit + push der Routine-Outputs.
#
# Bekannte Output-Verzeichnisse: daily/ weekly/ monthly/ quarterly/ — ausserdem
# .state/pricing_snapshots/ (einzige .state-Subdir die laut intel-monthly-pricing
# committet bleibt; alle anderen .state-Files sind in .gitignore).
#
# Nur wenn die Routine erfolgreich war (EXIT_CODE=0) und tatsaechlich neue Files
# geschrieben wurden. Race mit dem Discord-Bot-Pusher wird via pull --rebase
# --autostash entschaerft. Bei Push-Fail: nur Warnung, kein Routine-Abort.
# ---------------------------------------------------------------------------
if [[ $EXIT_CODE -eq 0 ]]; then
    cd "$REPO_ROOT"
    git add daily/ weekly/ monthly/ quarterly/ \
            .state/pricing_snapshots/ 2>/dev/null || true
    if ! git diff --cached --quiet; then
        DATE=$(date +%Y-%m-%d)
        if ! git pull --rebase --autostash origin main; then
            echo "WARN: pull --rebase failed for ${NAME}, aborting rebase" >&2
            git rebase --abort 2>/dev/null || true
        fi
        if git commit -m "feat(${NAME}): output ${DATE}" --no-verify; then
            git push origin main || \
                echo "WARN: push failed for ${NAME} — output committed locally only" >&2
        else
            echo "WARN: commit failed for ${NAME}" >&2
        fi
    else
        echo "no new output files for ${NAME}, skipping commit"
    fi
fi

exit $EXIT_CODE
