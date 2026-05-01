#!/bin/bash
# Ação do Antigravity para gestão de ambiente inicial do SIGI.

# 1. Garante que .env está bloqueado no .gitignore
if ! grep -q "^.env$" .gitignore; then
    echo "" >> .gitignore
    echo "# Ignorar variaveis de ambiente locais" >> .gitignore
    echo ".env" >> .gitignore
    echo "Sucesso: .env adicionado ao controle de bloqueio do .gitignore."
fi

# 2. Cria .env baseado no .env.example se não existir
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Sucesso: Arquivo .env gerado a partir do template."
fi