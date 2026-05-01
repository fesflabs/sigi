#!/bin/bash
# Uso: ./run.sh [opcional: caminho_do_teste]
# Exemplo: ./run.sh
# Exemplo 2: ./run.sh tests/modules/finance/test_expenses.py

TARGET_PATH=$1

if [ -z "$TARGET_PATH" ]; then
    echo "Executando suíte completa de testes no Backend..."
    docker exec -it sigi-backend poetry run pytest --cov=app --cov-report=term-missing
else
    echo "Executando testes no caminho: $TARGET_PATH"
    docker exec -it sigs-backend poetry run pytest $TARGET_PATH --cov=app --cov-report=term-missing
fi