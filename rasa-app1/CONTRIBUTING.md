# Contributing to rasa-app1

Thank you for contributing!

## Workflow

- Use [Poetry](https://python-poetry.org/) for all dependency management.
- Before opening a PR:
  - Run pre-commit (`pre-commit run --all-files`)
  - Run all tests (`pytest` and `rasa test nlu`)
  - Ensure code passes `ruff`, `black`, and `mypy`
- For new FAQ or intents, add data to `data/nlu.yml`, and update tests in `tests/test_nlu.yml`.

## Coding Standards

- Python code must be linted (`ruff`), formatted (`black`), and type-checked (`mypy`).
- Scripts must include usage comments and be testable.

## Security

- Do not commit secrets or credentials. Use `.env.example` for environment variables.

## Documentation

- Update `README.md` and usage comments for any workflow or interface changes.
