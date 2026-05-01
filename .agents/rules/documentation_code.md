---
trigger: model_decision
description: "Regras aplicadas ao escrever docstrings, interfaces TypeScript e OpenAPI."
---

---
trigger: model_decision
description: "Regras aplicadas ao escrever docstrings, interfaces TypeScript e OpenAPI no projeto SIGI."
---

# Rule: Documentação como Código

1. **Python / FastAPI:**
   - Funções públicas e Endpoints exigem Docstrings detalhadas (args, returns, raises).
   - Use os parâmetros dos decoradores do FastAPI (`summary`, `description`) para enriquecer automaticamente o Swagger/OpenAPI.
2. **TypeScript:**
   - Tipagem e Interfaces são a documentação primária. 
   - Sempre nomeie e exporte as interfaces para *props* e DTOs, documentando atributos opcionais e obrigatórios claramente via *JSDoc comments* se houver lógica atrelada.