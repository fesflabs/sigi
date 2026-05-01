---
description: Sequência obrigatória para criação de novas páginas, telas ou componentes visuais complexos no Next.js.
---

# Workflow: Prototipagem de UI Frontend (/ui-prototyping)

**Descrição:** Sequência obrigatória para criação de novas páginas ou ecrãs complexos no Next.js.
**Invocação:** O utilizador aciona via `/ui-prototyping` ou ao pedir explicitamente a criação de um ecrã.

## Passos de Execução (Linear):

1. **Gatekeeper de Insumo Visual:**
   - Verifique os anexos. O utilizador forneceu protótipo/Figma? Se NÃO, bloqueie e peça a imagem. Se SIM, avance.

2. **Consulta à Fonte da Verdade (Specs):**
   - Leia silenciosamente `docs/specs/design_system_mapping.md` e `docs/specs/ux_accessibility_guidelines.md`.

3. **Decomposição Estrutural e Arquitetura de Performance:**
   - Liste para o utilizador os componentes Shadcn UI e ícones Lucide necessários.
   - [cite_start]Planeie onde irá implementar o `<Suspense>` para garantir o *Streaming de HTML* assíncrono das partes não cruciais[cite: 7].

4. **Auditoria Pré-Código (Checklist de Acessibilidade/UX):**
   - [cite_start]Garanta que todos os botões/ícones de ação planeados respeitam o Target Size (24x24px)[cite: 34].
   - [cite_start]Se for um Dashboard, valide mentalmente se o layout atende à regra **3-30-300** (KPI destacado no Top-Left)[cite: 60, 61, 69].
   - [cite_start]Se houver formulário, garanta a integração `react-hook-form` + `Zod`[cite: 11, 13].

5. **Geração e Componentização:**
   - Escreva o código TypeScript/TSX aplicando a Rule 03. 
   - Divida ficheiros com mais de 300 linhas.

6. **Validação Final (Linting):**
   - Invoque a skill `run-code-linter` com o target `frontend` para validação rigorosa.