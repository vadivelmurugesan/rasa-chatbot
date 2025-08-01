#!/usr/bin/env bash

set -euo pipefail

# --- Helper: Colored Logging ---
info()    { echo -e "\033[1;36m[INFO]\033[0m $*"; }
success() { echo -e "\033[1;32m[SUCCESS]\033[0m $*"; }
error()   { echo -e "\033[1;31m[ERROR]\033[0m $*"; }
warn()    { echo -e "\033[1;33m[WARN]\033[0m $*"; }

# --- Load .env if present ---
if [ -f .env ]; then
  info "Loading environment from .env"
  set -a; source .env; set +a
fi

# --- Poetry Install ---
if ! command -v poetry &>/dev/null; then
  info "Poetry not found. Installing Poetry (user mode)..."
  curl -sSL https://install.python-poetry.org | python3 -
  export PATH="$HOME/.local/bin:$PATH"
fi
info "Poetry version: $(poetry --version)"

# --- Poetry Env Setup ---
info "Installing project dependencies with Poetry..."
poetry install

info "Rasa version: $(poetry run rasa --version)"

# --- Optional: Prompt to clear models/venv (fresh start) ---
read -rp "Clean previous models before training? [y/N]: " CLEAN
if [[ "$CLEAN" =~ ^[Yy]$ ]]; then
  info "Clearing models/ directory..."
  rm -rf models/
fi

# --- Train Model ---
info "Training Rasa model..."
poetry run rasa train

# --- Run NLU Tests ---
info "Running NLU regression tests..."
poetry run rasa test nlu

# --- Post Setup Instructions ---
success "Local setup complete!"
echo "To run the bot: \033[1;34mpoetry run rasa run --enable-api --cors '*'\033[0m"
echo "To test in shell: \033[1;34mpoetry run rasa shell\033[0m"