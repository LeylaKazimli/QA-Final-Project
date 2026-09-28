#!/usr/bin/env bash
# Framework-ün öz testləri. İstifadə:
#   ./framework-tests/run-selftest.sh          # hamısı
#   ./framework-tests/run-selftest.sh ui       # yalnız UI
#   ./framework-tests/run-selftest.sh api      # yalnız API
set -euo pipefail
cd "$(dirname "$0")/.."

case "${1:-all}" in
  ui)  SPECS="framework-tests/ui-selftest.spec" ;;
  api) SPECS="framework-tests/api-selftest.spec" ;;
  *)   SPECS="framework-tests" ;;
esac

# UI playground üçün lokal HTTP server (cookie/localStorage file:// üzərində işləmir)
python3 -m http.server 8765 --directory framework-tests/pages >/dev/null 2>&1 &
SERVER_PID=$!
trap 'kill $SERVER_PID 2>/dev/null || true' EXIT
sleep 1

mvn -q test -Dgauge.specs.dir="$SPECS"
