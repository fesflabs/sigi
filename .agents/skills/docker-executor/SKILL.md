---
name: docker-executor
description: "Sempre utilize esta skill quando precisar instalar pacotes (npm, poetry, pip), rodar testes ou executar ferramentas de CLI (ex: npx shadcn) no projeto. Ela garante que o comando rodará de forma isolada dentro do container correto."
---

# Docker Executor Skill

Esta skill roteia comandos de desenvolvimento para os containers apropriados, respeitando a Rule 04 de Infraestrutura.

## Implementação (`run.sh`)
O agente deve executar o script bash local passando o serviço alvo e o comando.
Alvos permitidos: `frontend`, `backend`.