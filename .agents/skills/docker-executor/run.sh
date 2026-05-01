#!/bin/bash
# Uso: ./run.sh <target> "<command>"
# Exemplo: ./run.sh frontend "npm install lucide-react"

TARGET=$1
COMMAND=$2

if [ "$TARGET" == "frontend" ]; then
    echo "Executando no Frontend Container..."
    # Ajuste o nome do container frontend conforme seu docker-compose
    docker exec -it sigi-frontend sh -c "$COMMAND"
elif [ "$TARGET" == "backend" ]; then
    echo "Executando no Backend Container..."
    # Ajuste o nome do container backend conforme seu docker-compose
    docker exec -it sigi-backend sh -c "$COMMAND"
else
    echo "Erro: Target inválido. Use 'frontend' ou 'backend'."
    exit 1
fi

echo "Execução concluída. Se foi uma instalação global de módulo, lembre-se de avaliar a necessidade de 'docker restart $TARGET'."