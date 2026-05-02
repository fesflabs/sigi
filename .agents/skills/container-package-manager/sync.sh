#!/bin/bash
SERVICE=$1
PACKAGE=$2

if [ "$SERVICE" == "backend" ]; then
    # O Poetry já atualiza o pyproject.toml e o poetry.lock automaticamente.
    docker compose exec backend poetry add $PACKAGE
elif [ "$SERVICE" == "frontend" ]; then
    docker compose exec frontend npm install $PACKAGE
else
    echo "Erro: Use 'frontend' ou 'backend'."
    exit 1
fi