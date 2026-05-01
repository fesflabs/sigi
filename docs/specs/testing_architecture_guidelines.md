# Spec: Arquitetura de Testes Automatizados (SaaS Financeiro)

## 1. Isolamento Absoluto de Banco de Dados (SQLite Async)
- **Proibição:** Nunca utilizar bancos de dados de Produção ou Desenvolvimento (PostgreSQL) na suíte de testes.
- **Motor de Testes:** Para garantir compatibilidade com o FastAPI assíncrono, utilize obrigatoriamente o SQLite em memória com o driver async: `sqlite+aiosqlite:///:memory:`.
- **Prevenção de Concorrência:** Acople o motor SQLite à configuração `StaticPool` e `check_same_thread=False` para garantir a integridade entre as *threads* de teste.

## 2. Mocking via Injeção de Dependência
- Em testes de integração de API, use SEMPRE a propriedade nativa `app.dependency_overrides` do FastAPI. Substitua a sessão real (`get_db_session`) pela *fixture* do banco em memória, isolando a rota.

## 3. Clientes de Teste (Sync vs Async)
- **Testes Síncronos (Regras Isoladas):** Para testar lógicas puras do FastAPI sem I/O, utilize a classe `TestClient` (do pacote `fastapi.testclient`).
- **Testes Assíncronos (Padrão para Endpoints):** Para rotas que tocam no banco assíncrono, utilize OBRIGATORIAMENTE o `AsyncClient` da biblioteca `httpx` e decore o teste com `@pytest.mark.asyncio`.

## 4. Testando Celery (Background Jobs)
- **Unitários (Rápidos):** Configure o Celery via *fixture* com `task_always_eager = True`. Isso força a execução síncrona no mesmo processo do Pytest. Caso o processo seja intencionalmente bloqueante (ex: loops infinitos ou esperas de rede pesadas), você DEVE mockar o método `.run()` da task utilizando `unittest.mock`.
- **Integração:** Para fluxos longos, codifique a instanciação de um aplicativo Celery de teste independente, apontando para a infraestrutura de fila do Redis.

## 5. Organização e Cobertura
- Os testes devem ficar isolados no diretório `/tests`, com um `pytest.ini` configurando marcadores (ex: `@pytest.mark.integration`).
- É OBRIGATÓRIO o uso do `pytest-cov` para medir a cobertura de código das regras financeiras e garantir a ausência de gargalos sem testes.