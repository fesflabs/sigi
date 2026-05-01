---
trigger: model_decision
description: "Framework de decisão para criação de Testes Automatizados no SIGI. Exige uso de Pytest, SQLite em memória (aiosqlite), Dependency Overrides, httpx.AsyncClient e tratamento do Celery."
globs: backend/tests/**/*.py
---

---
trigger: model_decision
description: "Framework de decisão para criação de Testes Automatizados no SIGI. Exige uso de Pytest, SQLite em memória (aiosqlite), Dependency Overrides, httpx.AsyncClient e tratamento do Celery."
globs: "backend/tests/**/*.py"
---

# Rule: Mindset de Testes Automatizados (Pytest)

Ao escrever, refatorar ou analisar testes para o backend, VOCÊ DEVE OBRIGATORIAMENTE seguir estas heurísticas:

## 1. Setup de Fixtures e Banco de Dados
- NUNCA conecte ao PostgreSQL em testes.
- A *fixture* de banco de dados DEVE instanciar o `create_async_engine` utilizando OBRIGATORIAMENTE a string `sqlite+aiosqlite:///:memory:` e `poolclass=StaticPool`.

## 2. Sobrescrita de Injeção de Dependência (DI)
- Ao testar uma rota FastAPI, injete a sessão em memória no início do teste via `app.dependency_overrides[get_db_session] = override_get_db` e limpe com `.clear()` ao final.

## 3. Clientes HTTP
- Teste rotas assíncronas OBRIGATORIAMENTE instanciando `httpx.AsyncClient(app=app, base_url="http://test")` e marcando a função com `@pytest.mark.asyncio`.
- Use o `fastapi.testclient.TestClient` APENAS para testes lógicos 100% síncronos.

## 4. Tratamento do Celery
- Para testes unitários normais, assuma que a configuração `task_always_eager = True` fará o trabalho.
- Se a *task* do Celery chamada na rota for intencionalmente bloqueante ou tiver *sleeps* longos, VOCÊ DEVE mockar o método `.run()` via `unittest.mock.patch` para evitar o congelamento da suíte.
- Para testar a fila real, crie uma app Celery de teste apontando para o Redis do docker-compose e decore o teste com `@pytest.mark.integration`.