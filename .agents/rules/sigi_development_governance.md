---
trigger: always_on
---

# Governança de Ambiente, Infraestrutura e Segurança do SIGI

Você é o agente responsável pelo ecossistema do projeto SIGI (Sistemas Integrados de Gestão Interna). Este projeto opera sob uma arquitetura estritamente conteinerizada (Docker) e com segredos isolados. Seu mindset deve ser governado pelas seguintes leis de infraestrutura e segurança.

## 1. Framework de Decisão para Dependências e Docker

O ambiente é fisicamente dividido em dois contêineres principais: `frontend` (React/Node) e `backend` (FastAPI/Python). Ao analisar solicitações para instalar, atualizar ou remover pacotes, ou caso identifique imports não resolvidos:

*   **Proibição de Execução Local:** NUNCA execute gerenciadores de pacote (como `npm install`, `yarn add`, `pip install`, `poetry add`) soltos na raiz do projeto ou na máquina host. Isso corrompe a paridade do ambiente conteinerizado.
*   **Intervenção Backend (Python):** Se o pacote pertencer à stack de backend, a ação deve ocorrer obrigatoriamente dentro do contêiner correspondente utilizando o **Poetry**. Ao gerar comandos, use o padrão: `docker compose exec backend poetry add [nome-do-pacote]`. NUNCA use `pip` ou sugira `requirements.txt`. Todo o controle é feito via `pyproject.toml` e `poetry.lock`.
*   **Intervenção Frontend (React/Node):** Se o pacote pertencer à stack de frontend, a ação deve ocorrer obrigatoriamente dentro do contêiner correspondente. Ao gerar comandos, use o padrão: `docker compose exec frontend npm install [nome-do-pacote]`.

## 2. Framework de Decisão para Segredos e Variáveis de Ambiente

Ao gerar código, configurar integrações (como conexões de banco de dados PostgreSQL) ou criar arquivos de configuração:

*   **Isolamento de Credenciais (Zero Hardcode):** NUNCA faça hardcode de senhas, URIs de banco de dados, chaves de API ou tokens de acesso diretamente no código-fonte (.py, .ts, etc.) ou no `docker-compose.yml`.
*   **Uso Obrigatório do Padrão ENV:** Toda e qualquer variável sensível ou dependente de ambiente deve ser extraída estritamente de um arquivo `.env`.
*   **Manutenção de Templates (.env.example):** Ao identificar a necessidade de uma nova variável de sistema, você é obrigado a registrar a chave no arquivo `.env.example` utilizando um valor fictício/dummy (ex: `POSTGRES_PASSWORD=sua_senha_aqui`). O `.env.example` deve sempre refletir a estrutura exata do `.env`, mas sem os dados reais.
*   **Proteção de Repositório (.gitignore):** O arquivo `.env` é sagrado e estritamente local. NUNCA altere o `.gitignore` de forma a permitir o rastreamento (tracking) do arquivo `.env` pelo Git. O bloqueio deve ser mantido.

## 3. Resolução de Conflitos
*   Se o usuário solicitar "instale a biblioteca X", não presuma o ambiente local. Aplique a lei da **Intervenção** (Frontend ou Backend via Docker Compose).
*   Se o usuário compartilhar uma credencial no chat para ser usada no projeto, direcione-o a colocá-la no `.env` e atualize apenas a documentação/código para consumir essa variável.