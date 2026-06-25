#!/usr/bin/env bash
# ACME Portal - demo start script.
# Syncs dependencies and serves the app locally. Run from anywhere:
#   ./demo-talk/start.sh
set -euo pipefail

cd "$(dirname "$0")"

PORT="${PORT:-8888}"
export PORT

echo "[*] Syncing dependencies (uv)..."
uv sync --quiet

echo "[*] ACME Portal -> http://localhost:${PORT}/"
echo "[*] Login: ${PORTAL_USER:-pentest} / ${PORTAL_PASS:-we-got-graybox-reds}"
echo "[*] Ctrl-C to stop."
exec uv run acme-portal
