#!/usr/bin/env bash
# Idempotenter Installer fuer zentria-intel systemd-Routinen.
#
# Run on Hetzner-Server:
#   sudo bash deploy/install-routines.sh
#
# - Kopiert systemd-Service-Template + 8 Timer-Files nach /etc/systemd/system/
# - Setzt run-routine.sh executable
# - Legt /var/log/zentria-intel/ an
# - daemon-reload + enable + start aller Timer
# - Listet Status am Ende

set -euo pipefail

REPO_ROOT="/opt/zentria-intel"
SYSTEMD_DIR="/etc/systemd/system"
LOG_DIR="/var/log/zentria-intel"

if [[ "$EUID" -ne 0 ]]; then
    echo "ERROR: muss als root laufen (sudo bash $0)" >&2
    exit 1
fi

if [[ ! -d "${REPO_ROOT}/deploy/systemd" ]]; then
    echo "ERROR: ${REPO_ROOT}/deploy/systemd fehlt — Repo aktuell?" >&2
    exit 2
fi

echo "=== Make wrapper executable ==="
chmod +x "${REPO_ROOT}/.scripts/run-routine.sh"

echo "=== Log-Verzeichnis anlegen ==="
mkdir -p "$LOG_DIR"
chown deploy:deploy "$LOG_DIR"

echo "=== systemd-Files kopieren ==="
cp -v "${REPO_ROOT}/deploy/systemd/zentria-intel-routine@.service" "$SYSTEMD_DIR/"
cp -v "${REPO_ROOT}/deploy/systemd/"zentria-intel-routine@*.timer "$SYSTEMD_DIR/"

echo "=== daemon-reload ==="
systemctl daemon-reload

# Liste aller Timer aus dem deploy-dir
TIMERS=()
for f in "${REPO_ROOT}/deploy/systemd/"zentria-intel-routine@*.timer; do
    TIMERS+=("$(basename "$f")")
done

echo "=== Enable + Start aller Timer ==="
for timer in "${TIMERS[@]}"; do
    systemctl enable --now "$timer"
    echo "  enabled: $timer"
done

echo
echo "=== Status (next run pro Timer) ==="
systemctl list-timers --all 'zentria-intel-routine@*' --no-pager

echo
echo "=== Done. Logs in: $LOG_DIR/<routine-name>.log ==="
echo
echo "Manueller Run einer Routine (zum Testen):"
echo "  sudo systemctl start zentria-intel-routine@intel-morning.service"
echo
echo "On-demand Trigger-Watch (kein Timer, manuell triggern):"
echo "  sudo systemctl start zentria-intel-routine@intel-trigger-watch.service"
