# Spec: Arquitetura Backend de Missão Crítica (SaaS Financeiro)

## 1. Persistência e Validação Antecipada (SQLModel + Pydantic)
- **Integração Profunda:** O SQLModel é o ORM padrão. Ele unifica a tipagem do Pydantic com o SQLAlchemy.
- **Validação Antecipada (Shielding):** O Pydantic atua como um escudo, realizando a validação automática e rigorosa de esquemas JSON complexos na porta de entrada. Isso mitiga falhas de integridade antes mesmo que os dados alcancem a camada de persistência.

## 2. Padrões de Projeto (Design Patterns) Obrigatórios
O ecossistema rejeita código acoplado e blocos `if/else` intermináveis. A inteligência do negócio deve ser guiada pelos seguintes padrões:
- **Strategy:** Utilizado obrigatoriamente para encapsular algoritmos variáveis, como cálculos de impostos e lógicas de amortização. Em Python, trate essas funções como objetos de primeira classe, tornando os regimes tributários intercambiáveis.
- **Template Method:** Mandatório para fluxos de processos rígidos (ex: 1. Verificar saldo -> 2. Validar assinatura -> 3. Persistir). Subclasses ou validadores podem sobrescrever etapas, mas nunca o fluxo macro. Deve ser integrado aos *hooks* do SQLModel ou validadores do Pydantic.
- **Decorator:** Uso obrigatório de decoradores customizados para isolar preocupações transversais (*cross-cutting concerns*), como auditoria financeira, validação de permissões granulares e camadas de cache via `aioredis`.
- **Command e Pub/Sub:** Operações de longa duração (fechamento de folha, conciliação) devem ser desacopladas via mensageria. O FastAPI age como Produtor e o Celery/Redis como Consumidor.
- **Factory Method:** Utilizado através do `sessionmaker` do SQLAlchemy para instanciar conexões seguras, isolando segredos de infraestrutura.

## 3. Padrões de Estrutura e Dados
- **Injeção de Dependência (DI):** O uso do `Depends` no FastAPI é a espinha dorsal e o padrão estrutural mandatório. É terminantemente proibido criar instâncias manuais de serviços nos endpoints. Use DI para gerenciar sessões assíncronas de banco (`get_db_session`), validação de segurança JWT e RBAC, garantindo testabilidade.
- **Sanduíche de Unicode:** Em todas as entradas/saídas (ex: exportações contábeis), separe explicitamente dados brutos de strings.
- **Bancos de Dados:** O sistema utiliza PostgreSQL em Produção (garantindo transações ACID) e SQLite em memória para testes (garantindo rapidez e isolamento).

## 4. Diretriz Crítica de Segurança (Zero Trust)
- **CVE-2025-61152 (JWT):** É MANDATÓRIO o uso da biblioteca `PyJWT`. A lógica de validação DEVE rejeitar ativamente tokens forjados com o parâmetro `alg=none` para evitar escalada de privilégios.
- **Criptografia:** Senhas utilizam `passlib` com `bcrypt`. Chaves de API bancárias e dados sensíveis em repouso devem ser criptografados simetricamente usando `cryptography.fernet`.

## 5. Processamento Assíncrono e Resiliência (Celery + Redis)
Gerir tarefas financeiras exige técnicas "battle-tested". Aplicam-se os *Wolt Engineering Standards*:
- **Idempotência e Atomicidade:** Tarefas DEVEM ser projetadas para reexecução sem duplicar lançamentos financeiros. Use SEMPRE `acks_late=True` para que a tarefa só seja confirmada após o sucesso total.
- **Granularidade:** Divida processos monolíticos em tarefas curtas utilizando `chord`.
- **Estratégias de Retry:** Utilize *Exponential Backoff* com *Jitter* nas exceções de rede/API para evitar o efeito manada (*thundering herd*).
- **Isolamento de Filas:** Múltiplas filas (ex: `realtime` vs `batch`). Emita `QueueNotFound` se uma tarefa for roteada incorretamente.
- **Retrocompatibilidade e Signatures:** Use tarefas de *proxy* ou valores padrão para novos argumentos em *signatures* de tasks, evitando quebra de agendamentos durante deploys.
- **Observabilidade:** Uso obrigatório do *Celery Beat* para agendamentos e *Flower* para monitorização em tempo real.