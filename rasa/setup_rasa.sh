#!/bin/bash
set -e

PYTHON_VERSION="3.9.18"
VENV_NAME="rasa-venv-3.9"
RASA_VERSION="3.6.21"
SDK_VERSION="3.6.2"

echo "Checking for pyenv..."
if ! command -v pyenv &> /dev/null; then
  echo "Error: pyenv is not installed."
  echo "Install with:"
  echo "  brew install pyenv pyenv-virtualenv"
  exit 1
fi

# Initialize pyenv
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Install desired Python version if missing
if ! pyenv versions --bare | grep -qx "$PYTHON_VERSION"; then
  echo "Installing Python $PYTHON_VERSION..."
  pyenv install "$PYTHON_VERSION"
else
  echo "Python $PYTHON_VERSION already installed."
fi

# Create virtualenv if not present
if pyenv virtualenvs --bare | grep -qx "$VENV_NAME"; then
  echo "Virtualenv '$VENV_NAME' already exists."
else
  echo "Creating virtualenv '$VENV_NAME'..."
  pyenv virtualenv "$PYTHON_VERSION" "$VENV_NAME"
fi

# Activate environment
pyenv activate "$VENV_NAME"

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install or upgrade Rasa and SDK
echo "Installing or upgrading Rasa CLI and SDK..."
pip install --upgrade "rasa==$RASA_VERSION" "rasa-sdk==$SDK_VERSION" pytest

# Disable telemetry if present
echo "Disabling Rasa telemetry..."
rasa telemetry disable || echo "Warning: Telemetry disable failed."

echo ""
echo "Setup complete. Rasa $RASA_VERSION is ready to use."
echo ""
echo "To use this environment in new sessions:"
echo "  pyenv activate $VENV_NAME"
echo ""
echo "Next steps:"
echo "  rasa train"
echo "  rasa shell"