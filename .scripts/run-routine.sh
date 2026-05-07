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

if [[ -z "${ANTHROPIC_API_KEY:-}" ]]; then
    echo "ERROR: ANTHROPIC_API_KEY nicht gesetzt (in .env?)" >&2
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
exit $EXIT_CODE
