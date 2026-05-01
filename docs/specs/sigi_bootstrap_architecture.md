# Spec de Inicialização e Arquitetura Dockerizada do SIGI

## Objetivo
Estruturar o ambiente de desenvolvimento inicial do projeto SIGI (Sistemas Integrados de Gestão Interna), isolando o frontend e o backend em contêineres Docker independentes, garantindo a paridade entre ambientes, isolamento de dependências e segurança rigorosa de credenciais.

## Tech Stack
- **Infraestrutura:** Docker e Docker Compose.
- **Backend (Contêiner `backend`):** Python 3.12, FastAPI 0.112.0, SQLAlchemy. **Porta Exposta: 8000**
- **Frontend (Contêiner `frontend`):** React.js 18.2.0, TypeScript, Zod, Zustand. **Porta Exposta: 3000**
- **Database (Contêiner `db`):** PostgreSQL. **Porta Exposta: 5432**

## Critérios de Aceite
1. O ecossistema deve possuir um arquivo `docker-compose.yml` mapeando os três serviços e suas respectivas portas citadas acima.
2. A gestão de credenciais e variáveis sensíveis (como senhas de DB) deve ser feita exclusivamente via arquivo `.env`.
3. Um arquivo `.env.example` deve existir como template para documentar as chaves necessárias sem expor valores reais.
4. O arquivo `.env` deve ser explicitamente ignorado pelo controle de versão (registrado no `.gitignore`).
5. Todos os comandos de instalação de dependências devem ocorrer estritamente dentro dos contêineres, jamais na máquina host.