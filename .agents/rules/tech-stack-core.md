---
trigger: always_on
description: "Constituição Técnica do projeto. Define linguagens, frameworks obrigatórios (Next.js/FastAPI) e a topologia de pastas do monorepo."
---

---
trigger: always_on
description: "Constituição Técnica do projeto SIGI. Define linguagens, frameworks obrigatórios (Next.js/FastAPI) e a topologia de pastas do monorepo."
---

# Rule: Tech Stack Core & Estrutura Monorepo

## 1. Tech Stack Constraints (Imutável)
**Frontend:**
- **Framework:** React 19.2 e Next.js. O uso de **Server Components assíncronos** é o padrão para *data fetching*.
- **Performance (Streaming):** Implemente obrigatoriamente *Streaming* de HTML via `<Suspense>` para garantir interatividade imediata em partes críticas da interface.
- **Linguagem & Segurança:** TypeScript com tipagem e validação estrita via **Zod**. Toda a entrada de API deve ser "parsed".
- **Formulários:** Uso exclusivo de `react-hook-form` acoplado ao Zod para minimizar re-renderizações e garantir erros programaticamente determinados.
- **Stack UI:** Tailwind CSS, Shadcn UI (baseado em Radix UI para ARIA nativo).
- **Estado Global:** Zustand (para dados leves e partilhados, evitando overhead).

**Backend:**
- **Framework:** Python 3.12+ com FastAPI 0.112.0+ (Alta performance).
- **Gerenciador de pacotes:** Poetry
- **ORM & Validação:** **SQLModel** (Unificando Pydantic e SQLAlchemy para tipagem estática e mitigação de falhas de integridade).
- **Background Jobs:** **Celery** com **Redis** (Broker/Backend).
- **Monitorização:** Flower (Tasks) e Celery Beat (Cron).

## 2. Estrutura de Pastas e Isolamento
- **Monorepo:** `backend/` e `frontend/` na raiz.
- **Backend (`app/modules/`):** Padrão Modular (DDD). Cada módulo exige: `endpoints/`, `services/`, `models/` (SQLModel), `schemas/`, `repositories/`, `tasks.py` (Celery) e `README.md`.
- **Frontend (`src/features/`):** Feature-Sliced Design (`api/`, `components/`, `schemas/`, `store/`). Componentes genéricos em `src/shared/components/ui`.