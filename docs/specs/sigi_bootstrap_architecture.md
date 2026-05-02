# Spec de Inicialização e Arquitetura Dockerizada do SIGI

## Objetivo
Estruturar o ambiente de desenvolvimento inicial do projeto SIGI, garantindo isolamento em contêineres e segurança de credenciais.

## Tech Stack e Portas
- **Infraestrutura:** Docker e Docker Compose.
- **Backend:** Python 3.12, FastAPI 0.112.0, SQLAlchemy. **Porta Exposta: 8000**
- **Frontend:** React.js 18.2.0, TypeScript, Zod, Zustand. **Porta Exposta: 3000**
- **Database:** PostgreSQL. **Porta Exposta: 5434**

## Critérios de Aceite
1. Um único `docker-compose.yml` mapeia os três serviços (`backend`, `frontend`, `db`).
2. Gerenciamento de credenciais via `.env` (com template `.env.example`), com `.env` estritamente ignorado no controle de versão.
3. Instalação de pacotes ocorre unicamente dentro dos contêineres correspondentes.