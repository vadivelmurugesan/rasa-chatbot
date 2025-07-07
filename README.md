# FAQ Chatbot – On-Premise Microservice Deployment

This project provides a fully self-hosted, enterprise-grade chatbot system designed to answer static FAQ questions using a combination of:

- Rasa (NLU + response engine)
- Custom HTML/JavaScript frontend
- NGINX (frontend microservice)
- Docker Compose (multi-container orchestration)

The chatbot uses rule-based intent recognition to match user queries against a predefined set of FAQs and responds with static, vetted answers. If no confident match is found, it gracefully falls back and offers to contact human support.

## Features

- Purely on-premise, no cloud dependency
- Clean separation of microservices: Rasa backend and static frontend
- Stateless, horizontally scalable architecture
- Secure and predictable (no hallucination or generative output)
- Configurable fallback with human handoff prompt
- Lightweight, minimal UI served via NGINX

## Folder Structure

```
project-root/
│
├── rasa/                    # Rasa NLU and rules engine
│   ├── config.yml
│   ├── domain.yml
│   ├── data/
│   │   ├── nlu.yml
│   │   ├── rules.yml
│   └── models/
│
├── frontend/                # Static chatbot UI served via NGINX
│   ├── index.html
│   └── nginx.conf
│
├── docker-compose.yml       # Orchestration for frontend + rasa backend
└── README.md
```

## Prerequisites

- Docker and Docker Compose installed
- Local machine or OpenShift local environment

## Getting Started

### 1. Train the Rasa model

```
cd rasa
rasa train
cd ..
```

### 2. Start services

```
docker-compose up --build
```

### 3. Access the chatbot

Open your browser to:

```
http://localhost:3000
```

The chatbot UI will appear and is fully functional.

## Service Details

### Rasa Backend (`rasa/`)

- Uses rule-based intent classification via DIETClassifier
- Only predefined answers are returned (static intent-to-response mapping)
- Handles fallback with a controlled message directing users to contact support

### Frontend Microservice (`frontend/`)

- Simple HTML/JS-based UI served via NGINX
- Directly connects to Rasa’s REST webhook endpoint
- Displays bot replies in styled chat bubbles

## Customization

To modify FAQs:

1. Update `data/nlu.yml` with new intents and examples
2. Add matching responses in `domain.yml` under `utter_faq/...`
3. Update rules in `data/rules.yml`
4. Retrain model:

```
cd rasa
rasa train
```

## Security Notes

- All components run locally
- No external APIs or third-party cloud calls
- Does not store user data by default
- Designed to meet on-premise deployment requirements for security-conscious environments

## License

This project is for internal or private enterprise use.