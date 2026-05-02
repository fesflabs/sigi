#!/bin/bash
SERVICE=$1
PACKAGE=$2

if [ "$SERVICE" == "backend" ]; then
    docker compose exec backend pip install $PACKAGE
    docker compose exec backend pip freeze > backend/requirements.txt
elif [ "$SERVICE" == "frontend" ]; then
    docker compose exec frontend npm install $PACKAGE
else
    echo "Erro: Use 'frontend' ou 'backend'."
    exit 1
fi