#!/bin/bash
# Script de Instalação Maestro - Antigravity Framework
# Refactored for Rule 11 Compliance

set -e

echo "🚀 Iniciando instalação completa (Rule 11 Compliance)..."

# 0. Check Directories
if [ ! -d "backend" ] || [ ! -d "frontend" ]; then
    echo "❌ Estrutura de pastas incorreta. Certifique-se de que 'backend' e 'frontend' existem."
    exit 1
fi

# 1. Configuração do Backend
echo "📦 Configurando Backend (Python 3.12)..."
cd backend
if [ ! -d ".venv" ]; then
    python3.12 -m venv .venv
fi
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cd ..

# 2. Configuração do Frontend
echo "⚛️ Configurando Frontend (React + Vite + TS)..."
cd frontend
if [ -f "package.json" ]; then
    npm install
else
    echo "⚠️ package.json não encontrado no frontend!"
fi
cd ..

# 3. Environment Variables
echo "� Gerando arquivos de ambiente..."
if [ ! -f ".env" ]; then
    if [ -f ".env-example" ]; then
        cp .env-example .env
        echo "✅ .env criado a partir de .env-example"
    else
        echo "⚠️ .env-example não encontrado. Criando .env vazio."
        touch .env
    fi
else
    echo "ℹ️ .env já existe."
fi

echo "✅ Instalação concluída com sucesso!"
echo "➡️  Para iniciar o projeto: docker compose up --build"