---
description: Orquestra a criação de um novo domínio de negócio (Feature) na API FastAPI.
---

# Workflow: Criação de Módulo Backend de Missão Crítica (/scaffold-backend)

**Descrição:** Orquestra a criação de um novo domínio de negócio (Feature) na API FastAPI, garantindo DDD rigoroso, Padrões de Projeto, processamento assíncrono e segurança.
**Invocação:** O utilizador aciona via `/scaffold-backend [nome_do_modulo]`.

## Passos de Execução (Linear):

1. **Geração da Estrutura de Pastas (DDD Rigoroso):**
   - *Ação:* O agente deve planear e criar mentalmente a estrutura exata sob `backend/app/modules/[nome_do_modulo]/`:
     - `/endpoints` (Rotas HTTP FastAPI)
     - `/services` (Lógica de Negócio e Design Patterns)
     - `/repositories` (Acesso a dados isolado)
     - `/models` (Esquemas de Base de Dados)
     - `/schemas` (DTOs Request/Response)
     - `tasks.py` (Background Jobs Celery)
   - *Ação:* Redija um ficheiro `README.md` base explicando o propósito do módulo.

2. **Modelagem de Dados e Contratos (SQLModel + Pydantic):**
   - *Ação:* Crie as classes baseadas no `SQLModel` para a tabela da base de dados.
   - *Constraint:* Crie os schemas Pydantic (Create, Update, Response) garantindo OBRIGATORIAMENTE o uso de `alias_generator=to_camel` para enviar JSON no formato JS.

3. **Desenvolvimento do Repository:**
   - *Ação:* Crie a classe do repositório responsável pelas queries assíncronas do SQLModel.
   - *Constraint:* Garanta que a sessão da base de dados (`AsyncSession`) seja recebida exclusivamente via Injeção de Dependência.

4. **Desenvolvimento do Service e Aplicação de Patterns:**
   - *Ação:* Codifique as regras de negócio nos Services.
   - *Constraint de Arquitetura:* Verifique a natureza da lógica. Tem partes voláteis/mutáveis (como impostos)? Implemente o padrão **Strategy**. Requer passos fixos rígidos? Use **Template Method**.
   - *Constraint de Isolamento:* É estritamente proibido misturar sintaxe de ORM/Base de Dados nesta camada.

5. **Desenvolvimento dos Endpoints:**
   - *Ação:* Faça a amarração conectando as rotas HTTP ao Service via `Depends()`.
   - *Constraint de Segurança:* Aplique controlo de acesso RBAC e lembre-se OBRIGATORIAMENTE de aplicar o `AuditMiddleware` se houver rotas de mutação (POST/PUT/DELETE).

6. **Processamento Assíncrono e Resiliência (Celery):**
   - *Ação:* O módulo realiza operações pesadas ou integrações externas? Se sim, implemente as funções no `tasks.py`.
   - *Constraint:* Use sempre `acks_late=True` para garantir idempotência e aplique `Exponential Backoff` com *Jitter* nas tentativas (retries).

7. **Persistência e Migração (Skills):**
   - *Ação:* Como o modelo da base de dados foi alterado, você **DEVE** invocar a skill `generate-db-migration` passando uma mensagem descritiva (ex: "Criacao do modulo X").

8. **Formatação Automática (Skills):**
   - *Ação:* Para garantir a qualidade e os padrões da equipa, invoque a skill `run-code-linter` com o target `backend` para rodar o Ruff e o Black no código recém-gerado.