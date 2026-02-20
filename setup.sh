#!/usr/bin/env bash
# setup.sh — Ubuntu setup, run, and build helper
set -e

ACTION="${1:-run}"

# ── Install system deps needed by pywebview on Linux ────────────────────────
install_system_deps() {
  echo "Installing system dependencies..."
  sudo apt-get update -qq
  sudo apt-get install -y \
    python3-venv python3-dev \
    libgtk-3-dev libwebkit2gtk-4.0-dev \
    gir1.2-webkit2-4.0 \
    python3-gi python3-gi-cairo
}

# ── Create venv + install Python deps ───────────────────────────────────────
setup_venv() {
  if [ ! -d ".venv" ]; then
    python3 -m venv --system-site-packages .venv
  fi
  source .venv/bin/activate
  pip install --upgrade pip -q
  pip install -r requirements.txt -q
}

case "$ACTION" in
  deps)
    install_system_deps
    ;;
  run)
    setup_venv
    echo "Starting desktop app..."
    python main.py
    ;;
  build)
    setup_venv
    echo "Building standalone executable..."
    pyinstaller build.spec --clean
    echo ""
    echo "Done! Executable is in: dist/NiceGUIApp/"
    echo "Run with:  ./dist/NiceGUIApp/NiceGUIApp"
    ;;
  *)
    echo "Usage: $0 [deps|run|build]"
    echo "  deps   Install system-level GTK/WebKit packages (run once)"
    echo "  run    Launch the app in development mode (default)"
    echo "  build  Package into a standalone executable via PyInstaller"
    ;;
esac