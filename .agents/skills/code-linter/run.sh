#!/bin/bash
# Uso: ./run.sh <target>
# Exemplo: ./run.sh frontend

TARGET=$1

if [ "$TARGET" == "frontend" ]; then
    echo "Rodando verificação de tipagem TypeScript (Strict Mode)..."
    docker exec -it sigi-frontend-dev npm run typecheck
    echo "Rodando ESLint..."
    docker exec -it sigi-frontend-dev npm run lint
elif [ "$TARGET" == "backend" ]; then
    echo "Rodando formatação Black e Ruff..."
    docker exec -it sigi-backend poetry run ruff check . --fix
    docker exec -it sigi-backend poetry run black .
else
    echo "Erro: Target inválido."
fi