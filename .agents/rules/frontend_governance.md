---
trigger: model_decision
description: description: "Regras rígidas de Design System, consumo de estado e construção de telas em Next.js/React."
---

---
trigger: model_decision
description: "Regras rígidas de Design System, consumo de estado, acessibilidade WCAG 2.2 e construção de ecrãs no Next.js para o SIGI."
globs: "frontend/**/*.tsx, frontend/**/*.ts"
---

# Rule: Governança Frontend (UI/UX e Acessibilidade)

## 1. Strict Compliance com Design System e Acessibilidade
- Consulte as specs `design_system_mapping.md` e `ux_accessibility_guidelines.md` ANTES de criar interfaces.
- **Radix/Shadcn (ARIA):** Confie nos componentes base para gerir estados como `aria-expanded` nativamente. 
- **Target Size e Hover:** Garanta que alvos de clique têm no mínimo `24x24px`. NUNCA esconda ações críticas apenas atrás de eventos de `hover` (Mobile-First).

## 2. Scaffolding de Ecrã e Layout Adaptativo
- **Root Wrapper:** O contentor pai da página deve usar `max-w-7xl mx-auto w-full pb-20`.
- **Reflow e Responsividade:** Teste mentalmente se o seu layout sobrevive a 320px sem rolagem horizontal.
- Para *Dashboards*, a métrica principal (KPI) deve estar sempre no *Top-Left*.

## 3. Gestão de Estado e Prevenção de Erros
- Utilize `Zustand` para estado partilhado.
- **Validação:** Qualquer submissão de formulário tem de ser validada pelo `Zod` e usar `react-hook-form`. O erro deve focar o campo para o utilizador.
- Ações destrutivas requerem modais de confirmação (Error Prevention).