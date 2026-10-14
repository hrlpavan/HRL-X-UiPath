#!/usr/bin/env bash
# UiPath Cross-OS Automation & Sync Engine (v3.0)
# Usage: uipath-sync or ./sync-uipath.sh

set -e

SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do
  DIR="$(cd -P "$(dirname "$SOURCE")" >/dev/null 2>&1 && pwd)"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
done
SCRIPT_DIR="$(cd -P "$(dirname "$SOURCE")" >/dev/null 2>&1 && pwd)"

python3 "$SCRIPT_DIR/scripts/sync_uipath.py" "$@"
