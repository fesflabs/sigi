---
description: description: Inicializa a arquitetura dockerizada do SIGI, implementando segurança de segredos (.env) e expondo as portas designadas pela spec de bootstrap.
---

---
description: Inicializa a arquitetura dockerizada do SIGI, configurando pastas, banco, segurança de ambiente e contêineres.
---

1. Leia o arquivo `docs/specs/sigi_bootstrap_architecture.md` para carregar as definições de infraestrutura e portas.

2. Crie a estrutura de diretórios base.
// turbo
mkdir -p frontend backend

3. Configure o arquivo `.gitignore` para bloquear credenciais e arquivos de ambiente do agente.
// turbo
echo -e "\n# Variaveis de Ambiente\n.env\n# Agentes\n.agent/" >> .gitignore

4. Crie o template de segredos para o banco de dados.
// turbo
echo -e "POSTGRES_USER=postgres\nPOSTGRES_PASSWORD=hmetal85\nPOSTGRES_DB=sigi_db" > .env.example && cp .env.example .env

5. Gere os arquivos `Dockerfile` dentro de `/backend` (porta 8000) e `/frontend` (porta 3000) baseados na spec.

6. Gere o `docker-compose.yml` mapeando os serviços e as portas correspondentes.

7. Conceda permissão de execução à skill de gerenciamento de pacotes.
// turbo
chmod +x .agent/skills/container-package-manager/install.sh

8. Suba o ecossistema completo em background.
// turbo
docker compose up -d --build

9. Valide se os serviços estão rodando e informe ao usuário a conclusão do bootstrap.