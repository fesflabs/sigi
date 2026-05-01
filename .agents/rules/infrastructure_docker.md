---
trigger: glob
globs: "Dockerfile, docker-compose*.yml, .env*, app/core/configs.py, backend/**/*.py, package.json"
---

---
trigger: glob
globs: "Dockerfile, docker-compose*.yml, .env*, app/core/configs.py, backend/**/*.py, package.json, .github/**/*.yml"
description: "Governança sobre Docker, variáveis de ambiente, pipelines CI/CD e segurança para o SIGI."
---

# Rule: Infraestrutura, Docker e Segurança

## 1. Protocolo Docker e Isolamento
- **Execução Confinada:** Proibido rodar CLI/instalações (`npm`, `poetry`) no host. Use `docker exec`. Reinicie o container em caso de falha de cache de módulo.
- **Bancos Isolados:** Dev, Homolog e Prod têm bancos separados. 
- **Comportamento SQLAlchemy:** Em Development, use `echo=True` (debug). Em Prod, `echo=False` com logs estruturados.
- **Restart Policy:** Containers em servidores usam `restart: always` ou `unless-stopped`.

## 2. CI/CD e Secrets Management
- Zero chaves no código (`.env` local, Pydantic em backend, `NEXT_PUBLIC_` em frontend).
- Testes rodam no **GitHub Actions** antes do merge.
- O **Alembic** (migrations) deve rodar automaticamente na pipeline de deploy.

## 3. Hardening e Sessão
- **Backend:** Senhas sofrem hash (`passlib[bcrypt]`). JWT de ciclo curto protegido por Refresh Token.
- **Frontend:** Proteção nativa contra XSS (Proibido `dangerouslySetInnerHTML` cego).