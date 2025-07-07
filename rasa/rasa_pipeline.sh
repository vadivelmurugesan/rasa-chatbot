#!/bin/bash

set -e

echo "Activating virtual environment..."

if [ ! -d "venv" ]; then
    echo "Error: venv directory not found. Please run setup_rasa.sh first."
    exit 1
fi

source venv/bin/activate

echo "Validating Rasa project data..."
rasa data validate || {
    echo "Error: Data validation failed. Please fix NLU/stories/rules."
    exit 1
}

echo "Training Rasa model..."
rasa train --force || {
    echo "Error: Training failed."
    exit 1
}

echo "Running model tests..."
rasa test --debug --fail-on-prediction-errors || {
    echo "Error: Some predictions or story paths failed."
    exit 1
}

echo "Model validation, training, and testing completed successfully."