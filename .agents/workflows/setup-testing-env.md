---
description: Configuração do Ambiente de Testes (/setup-tests)
---

# Workflow: Configuração do Ambiente de Testes (/setup-tests)

**Descrição:** Orquestra a criação da estrutura base de testes (Fixtures, Markers, Pytest-cov, Configuração Celery Eager) no backend.
**Invocação:** O utilizador aciona via `/setup-tests`.

## Passos de Execução (Linear):

1. **Geração da Estrutura de Diretórios:**
   - Crie a pasta `backend/tests/` e subpastas equivalentes aos módulos (ex: `backend/tests/modules/`).

2. **Configuração Raiz (pytest.ini):**
   - Crie o ficheiro `backend/pytest.ini`. Registe marcadores personalizados (`markers = integration: marcas de testes lentos com redis`). Ative o `asyncio_mode = auto`.

3. **Criação da Fábrica de Fixtures (conftest.py) - O Coração do Teste:**
   - *Ação:* Crie o ficheiro `backend/tests/conftest.py`.
   - *Constraint de Base de Dados:* Implemente a *fixture* usando `create_async_engine("sqlite+aiosqlite:///:memory:", poolclass=StaticPool, connect_args={"check_same_thread": False})`.
   - *Constraint de DI:* Crie a *fixture* do `AsyncClient` (httpx) que faz o `app.dependency_overrides` da sessão do banco.
   - *Constraint do Celery:* Crie uma *fixture* `autouse=True` que force `task_always_eager = True` e `task_eager_propagates = True` na configuração do Celery da aplicação.

4. **Teste de Sanidade:**
   - Crie um teste básico de exemplo em `backend/tests/test_health.py` que invoque uma rota simples utilizando o `AsyncClient`.

5. **Relatório:**
   - Informe ao utilizador que o ambiente hermético foi configurado e lembre-o de que pode invocar a skill `run-code-tests` a qualquer momento para medir o `coverage`.