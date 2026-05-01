---
description: description: Inicializa a arquitetura dockerizada do SIGI, implementando segurança de segredos (.env) e expondo as portas designadas pela spec de bootstrap.
---

1. Leia minuciosamente o arquivo `docs/specs/sigi_bootstrap_architecture.md` para carregar as definições de portas, infraestrutura e governança.

2. Crie o arquivo base de segredos `.env.example` definindo as variáveis necessárias para o PostgreSQL.
// turbo
echo "POSTGRES_USER=postgres\nPOSTGRES_PASSWORD=hmetal85\nPOSTGRES_DB=sigi_db" > .env.example

3. Torne o script da skill de gerenciamento de ambiente executável e invoque-a para proteger o projeto.
// turbo
chmod +x .agent/skills/env-manager/sync.sh && bash .agent/skills/env-manager/sync.sh

4. Crie a estrutura de diretórios do ecossistema.
// turbo
mkdir -p frontend backend

5. Gere os arquivos `Dockerfile` dentro de `/backend` (configurado para expor a porta 8000) e de `/frontend` (configurado para expor a porta 3000).

6. Gere o `docker-compose.yml` mapeando as portas definidas (8000:8000, 3000:3000, 5434:5434) e configurando os serviços para consumir os dados sensíveis via `env_file: - .env`.

7. Torne o script da skill de pacotes (previamente definido) executável.
// turbo
chmod +x .agent/skills/container-package-manager/install.sh

8. Suba os contêineres construindo as imagens em background.
// turbo
docker compose up -d --build

9. Valide o processo e informe ao usuário que as frentes do SIGI estão operando nas portas correspondentes e com os segredos blindados.