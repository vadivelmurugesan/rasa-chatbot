# rasa-app1

**Enterprise-Ready FAQ Chatbot NLU Microservice**
*Built on Rasa 3.6.21+ (2025) | Poetry 2.1.x | Python 3.8–3.10 | Secure, Containerized, MLOps-Enabled*

---

## 🧠 What is This Project?

**rasa-app1** is a modern, production-grade FAQ intent classifier—built with [Rasa Open Source](https://rasa.com/docs/rasa/) and [Poetry](https://python-poetry.org/).
It maps end-user questions (e.g., “How do I reset my password?”) to enterprise-approved, static answers, powering scalable FAQ chatbots in any app.
**Features:**

* 100% data-driven, versioned, and audit-friendly.
* Container-ready for OpenShift, Kubernetes, or Docker.
* ONNX model export for ultra-fast inference.
* Easy to extend for escalation, hand-off, or analytics.

---

## 📦 Project Structure Overview

```
rasa-app1/
├── data/            # NLU, stories, rules (edit here to add questions/intents)
├── models/          # Trained .tar.gz models + ONNX export
├── model-info/      # Model version/audit info
├── scripts/         # Automation: ONNX export, model info, retrain hash
├── tests/           # Unit and NLU regression tests
├── .github/         # CI/CD workflows
├── .env.example     # Sample environment variables
├── Dockerfile       # Poetry + Rasa container image
├── pyproject.toml   # Dependency manager (Poetry)
├── README.md        # (This file)
└── CONTRIBUTING.md  # Team workflow & quality standards
```

---

## 🟢 Quickstart: Day 1 Developer Setup

### 1. Pre-requisites

* **Python**: 3.9 (other versions not officially supported)
* **Poetry**: 2.1.x ([install guide](https://python-poetry.org/docs/#installation))
* **Docker**: 24.x+ (optional for containers)

### 2. Clone and Install

```bash
git clone <YOUR_REPO_URL>
cd rasa-app1
poetry install
```

### 3. Train the Model

```bash
poetry run rasa train
```

* Uses all data in `data/nlu.yml`, `data/stories.yml`, and `data/rules.yml`.
* Trained model is saved to `models/`.

### 4. Test the Model

```bash
poetry run rasa test nlu
poetry run pytest
```

---

## 🖥️ Running and Testing the Bot

### 5. Start the Bot Server (Local API)

```bash
poetry run rasa run --enable-api --cors "*"
```

* Default port: **5005**

### 6. Chat with the Bot (Interactive Shell)

```bash
poetry run rasa shell
```

* Try:

  ```
  Your input -> How do I reset my password?
  ```

### 7. Test with HTTP (curl)

```bash
curl -X POST http://localhost:5005/model/parse \
  -H "Content-Type: application/json" \
  -d '{"text":"How do I reset my password?"}'
```

* Returns detected intent and confidence as JSON.

---

## 📚 How to Add a New FAQ

1. **Add new intent and examples in `data/nlu.yml`.**
2. **Add corresponding answer in `domain.yml`.**
3. **Optionally add a rule in `data/rules.yml`.**
4. **Retrain the model:**

   ```bash
   poetry run rasa train
   ```

---

## 🔄 Model Versioning & ONNX Export

* **Export ONNX model (after training):**

  ```bash
  poetry run python scripts/export_onnx.py
  ```
* **Generate model info (for audit/versioning):**

  ```bash
  poetry run python scripts/model_info.py
  ```

---

## 🛡️ Security & Dependency Management

* **All dependencies are version-locked in `poetry.lock`.**
* **Regularly audit with:**

  ```bash
  poetry run pip-audit
  poetry run safety check
  ```
* **Never commit secrets.** Use `.env` (see sample below).

**.env.example**

```env
RASA_PORT=5005
MODEL_DIR=models/
ONNX_DIR=models/onnx/
```

---

## 🐳 Docker Usage (for Containers/OpenShift/K8s)

```bash
docker build -t rasa-app1-nlu:3.6.21 .
docker run -p 5005:5005 rasa-app1-nlu:3.6.21
```

---

## 🧪 Quality, CI/CD, and Linting

* **Pre-commit hooks:**

  ```bash
  poetry run pre-commit run --all-files
  ```
* **Code and data checks:**

  ```bash
  poetry run ruff .
  poetry run black --check .
  poetry run mypy scripts/
  ```
* **CI/CD:** Automated in `.github/workflows/ci.yml` for every PR and push.

---

## 🦾 Troubleshooting & Learning

* **If install fails:**

  * Check Python/Poetry versions (`python --version`, `poetry --version`)
  * Re-run `poetry install`
* **If training fails:**

  * Check for YAML syntax errors in `data/`
* **If in doubt:**

  * See [Rasa Documentation](https://rasa.com/docs/rasa/)
  * [Poetry Documentation](https://python-poetry.org/docs/)
  * Ask your team or open a [GitHub issue](https://github.com/yourorg/rasa-app1/issues)
  * Join the [Rasa Community](https://forum.rasa.com/)

---

## 🤝 Contributing & Support

* See [CONTRIBUTING.md](CONTRIBUTING.md) for PR and branching workflow.
* **Open GitHub issues** for bugs or enhancements.
* Internal questions? Use [#chatbot-dev-support](https://slack.yourcompany.com/) (replace with your team’s real support channel).

---

## 📜 License

MIT License (see [LICENSE](LICENSE) for details).

---

## 🔗 Learn More

* [Rasa Docs](https://rasa.com/docs/rasa/)
* [Poetry Docs](https://python-poetry.org/docs/)
* [Best Practices: Secure Python Dependencies (Snyk)](https://snyk.io/blog/python-dependencies-security-best-practices/)
* [FAQ Chatbots at Scale (Rasa Blog)](https://rasa.com/blog/?tag=faq)
