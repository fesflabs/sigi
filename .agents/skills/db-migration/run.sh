#!/bin/bash
# Uso: ./run.sh "<mensagem_da_migracao>"
# Exemplo: ./run.sh "add_status_column_to_contracts"

MESSAGE=$1

if [ -z "$MESSAGE" ]; then
  echo "Erro: Forneça uma mensagem para a migração."
  exit 1
fi

echo "Gerando migração Alembic: $MESSAGE"
docker exec -it sigi poetry run alembic revision --autogenerate -m "$MESSAGE"
echo "Migração gerada em backend/alembic/versions/. Revise o arquivo gerado para garantir que não houve vazamento de domínio."