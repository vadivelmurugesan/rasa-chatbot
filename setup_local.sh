#!/bin/bash
set -e
echo "🔧 Building and starting all services..."
docker compose up --build -d
echo "✅ All services are up and running!"

echo "🔗 Access URLs:"
echo "Frontend  : http://localhost:3000"
echo "Rasa API  : http://localhost:5005/webhooks/rest/webhook"