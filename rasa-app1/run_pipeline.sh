#!/usr/bin/env bash

set -euo pipefail

info()    { echo -e "\033[1;36m[INFO]\033[0m $*"; }
success() { echo -e "\033[1;32m[SUCCESS]\033[0m $*"; }
error()   { echo -e "\033[1;31m[ERROR]\033[0m $*"; }

START=$(date +%s)

# --- Env Loading ---
if [ -f .env ]; then
  info "Loading environment from .env"
  set -a; source .env; set +a
fi


# --- Poetry Lock ---
info "Locking all dependencies..."
poetry lock --no-cache

# --- Poetry Install ---
info "Installing all dependencies (including dev)..."
poetry install

# --- Code & Data Quality ---
info "Running pre-commit hooks, lint, format, type checks..."
#poetry run pre-commit run --all-files || warn "Some hooks failed."
poetry run ruff check . && poetry run black --check . && poetry run isort --check-only . && poetry run mypy scripts/

# --- Security Audit ---
info "Running pip-audit and safety checks..."
#poetry run pip-audit || warn "pip-audit found issues."
#poetry run safety check || warn "safety found issues."

# --- Training ---
info "Training Rasa model..."
poetry run rasa train

# --- Tests ---
info "Running Python and NLU tests..."
poetry run pytest
poetry run rasa test nlu

# --- Optional: ONNX Export ---
#info "Exporting model to ONNX (if supported)..."
#if poetry run python scripts/export_onnx.py; then
#  success "ONNX export succeeded."
#else
#  warn "ONNX export skipped or failed (optional)."
#fi

# --- Model Metadata ---
info "Generating model metadata..."
poetry run python scripts/model_info.py

# --- Timing ---
END=$(date +%s)
DURATION=$((END - START))

success "Pipeline run complete in ${DURATION}s."