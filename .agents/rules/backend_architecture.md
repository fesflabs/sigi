---
trigger: model_decision
description: "Framework de decisão para o backend FastAPI. Aplica Clean Architecture, operações Assíncronas, performance de ORM e design de API REST."
---

---
trigger: model_decision
description: "Governança estrita e heurísticas de decisão para desenvolvimento backend com FastAPI no SIGI. Abrange Clean Architecture, Assincronismo, RESTful, Design Patterns e Segurança."
globs: "backend/**/*.py"
---

# Rule: Mindset de Arquitetura Backend (Missão Crítica)

Você atua como um Arquiteto de Software e Desenvolvedor Backend Sênior. Seu objetivo é garantir Clean Architecture, Domain-Driven Design (DDD) e alta performance. **A rota é "burra", o serviço é "inteligente" e a persistência é "isolada".**

Ao analisar, criar ou refatorar qualquer código Python no backend, aplique obrigatoriamente os seguintes frameworks de decisão:

## 1. Topologia de Domínio e Injeção de Dependência (DI)
Todo módulo do sistema DEVE ser segregado nas seguintes camadas, injetadas hierarquicamente via `Depends()`:
- **Endpoints (Routers):** Atue apenas como um despachante HTTP. Receba a requisição, injete as dependências (`Depends()`), mapeie os parâmetros via Pydantic e chame o Service. **ZERO** lógica de negócios, cálculos complexos ou chamadas ao `AsyncSession` nesta camada.
- **Services (Inteligência):** Contêm toda a orquestração de regras de negócio, validações e coordenação de repositórios. O Service não deve saber como o banco de dados realiza a escrita. **NÃO tocam no banco de dados diretamente**.
- **Repositories (Persistência):** Camada exclusiva para lidar com queries do `SQLModel`/`SQLAlchemy`. Os *Services* dependem dos *Repositories* via injeção.

## 2. Operações e Persistência Assíncrona
- **Async First:** Todo I/O (Banco, Rede, Disco, Redis) DEVE usar `async def` e invocar métodos com `await`.
- **Sessões e Transações:** Toda sessão instanciada num endpoint deve usar `yield` na injeção de dependência para fechar automaticamente. Para operações envolvendo múltiplas tabelas, force a atomicidade com `async with session.begin()`.
- **Anti-N+1 Problem:** Ao buscar entidades com relacionamentos, use SEMPRE `options(selectinload())` ou `joinedload()`.

## 3. Design de API RESTful
- **Padrão de Rotas:** Substantivos no plural (`/users`). GET (Leitura), POST (Criação), PUT/PATCH (Atualização), DELETE.
- **Status Codes Obrigatórios:** 200 (OK), 201 (Created), 204 (No Content), 400 (Bad Request), 401/403 (Auth), 422 (Validation).
- **Contratos e Paginação:** Jamais retorne dumps inteiros de tabelas. Rotas de listagem devem obrigatoriamente suportar paginação (limit, offset ou cursores) e delegação de filtros via `Depends()`.

## 4. Validação, Tipagem e Configuração
- **Contratos (Pydantic):** Modele schemas lógicos separados: `CreateSchema`, `UpdateSchema` e `ResponseSchema` (derivados de `BaseModel`) com `alias_generator=to_camel` para enviar JSON no formato JS. Use `.model_dump()` no lugar do depreciado `.dict()`.
- **Tipagem:** Forneça *Type Hints* completos (mypy-compliant). O uso de `Any` é estritamente proibido em retornos de API e assinaturas de Services.
- **Configuração:** Nunca utilize `os.getenv()` no meio do código. Faça a gestão centralizada estendendo `pydantic-settings` (`BaseSettings`).

## 5. Aplicação de Design Patterns (Lógica de Negócio)
- **Lógicas Mutáveis:** Ao criar regras contábeis, cálculos ou impostos variáveis, force a arquitetura para o padrão **Strategy**.
- **Validações Sequenciais:** Ao criar fluxos críticos rígidos, construa-os sob o padrão **Template Method**, delegando passos específicos a subclasses ou validadores Pydantic.
- **Transversalidade:** Utilize o padrão **Decorator** sobre os serviços para aplicar camadas de cache (`aioredis`) e logs não-intrusivos.

## 6. Persistência de Dados (SQLAlchemy 2.0+ e Redis)
- **Consultas:** Utilize obrigatoriamente `AsyncSession`, `create_async_engine` e a sintaxe 2.0 (`execute(select(Model))`). O uso de `.query()` (estilo 1.x) é proibido.
- **Migrações:** Ao alterar modelos de dados (`DeclarativeBase`), acompanhe a mudança com instruções para geração de migração via Alembic (`alembic revision --autogenerate`).
- **Cache:** Ao consultar dados imutáveis ou de leitura frequente, proponha cache com Redis, com estratégias de invalidação claras (TTL ou via eventos de update).

## 7. Segurança, IAM e Observabilidade
- **Trilha de Auditoria (Crucial):** Toda rota de mutação (POST/PUT/DELETE) DEVE ser rastreada pelo `AuditMiddleware` e salva no `audit_log`. Para logs de console em produção, adote o formato estruturado (JSON).
- **Autenticação e Autorização:** Exija Autenticação JWT injetando `Depends(get_current_user)` e verifique permissões (RBAC).
- **Hardening Específico:** 
  - Proteja credenciais estáticas com `cryptography.fernet`.
  - Valide rigorosamente tokens JWT garantindo que tokens forjados com `alg=none` lancem imediatamente um erro de *Unauthorized*.
  - Processe senhas unicamente com `passlib[bcrypt]`.
  - Aplique restrição severa de origens via `CORSMiddleware`.

## 8. PROTOCOLO FAIL-FAST (Anti-Patterns Proibidos)
Se o código a ser gerado violar qualquer ponto abaixo, **ABORTE e recalcule a rota**:
1. **Domain Leakage:** Manipular SQL/Dicts do SQLAlchemy, gerar UUIDs ou instanciar objetos de Banco de Dados dentro de `endpoints/*.py`.
2. **Sincronismo Traiçoeiro:** Uso de `time.sleep()` ou bibliotecas síncronas em rotas `async`. Use `asyncio.sleep()` e `httpx`.
3. **Bypass de Segurança:** Injetar senhas *plain-text* em bases de dados ou seeders. Toda senha, mesmo fictícia, deve sofrer hash.
4. **Tratamento de Exceções Mudo:** Usar blocos `except Exception: pass` ou omitir *stack traces* nativos vazando dados. Todo erro capturado deve ser logado explicitamente ou traduzido usando `HTTPException` padronizado.