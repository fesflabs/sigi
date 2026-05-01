# Lógica para gerar os arquivos base do projeto
import os

def generate_docker_compose():
    content = """
services:
  db:
    image: postgres:16-alphine
    container_name: maestro-db-dev
    restart: always
    environment:
      POSTGRES_USER: ${DB_USER:-postgres}
      POSTGRES_PASSWORD: ${DB_PASSWORD:-postgres}
      POSTGRES_DB: ${DB_NAME:-maestro_db}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    container_name: maestro-redis-dev
    ports:
      - "6379:6379"

  backend:
    build: 
      context: ./backend
      dockerfile: Dockerfile
    volumes:
      - ./backend:/app
    environment:
      - DATABASE_URL=postgresql+asyncpg://${DB_USER}:${DB_PASSWORD}@db:5432/${DB_NAME}
      - REDIS_URL=redis://redis:6379/0
    depends_on:
      - db
      - redis

volumes:
  postgres_data:
"""
    with open("docker-compose.yml", "w") as f:
        f.write(content.strip())

def generate_env_example():
    content = """
# Database Config (Dev: localhost / Prod: Server IP)
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=maestro_db
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/maestro_db

# Redis
REDIS_URL=redis://localhost:6379/0

# App Settings
APP_ENV=development
SECRET_KEY=change-me-in-production
"""
    with open(".env-example", "w") as f:
        f.write(content.strip())
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write(content.strip())

if __name__ == "__main__":
    generate_docker_compose()
    generate_env_example()
    print("Arquivos de infraestrutura gerados com sucesso!")