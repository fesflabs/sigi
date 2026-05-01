# Spec: UX, Heurísticas e Acessibilidade (WCAG 2.2)

## 1. Conformidade Técnica Estrita (WCAG 2.2)
[cite_start]Toda a interface gerada deve ser "Programmaticamente Determinada" para tecnologias assistivas[cite: 20].
- [cite_start]**Target Size (2.5.8):** Os alvos de clique DEVEM ter no mínimo `24x24 CSS pixels`[cite: 28, 34]. [cite_start]Se forem menores, aplique a Exceção de Espaçamento (nenhum outro alvo num raio de 24px)[cite: 35].
- [cite_start]**Focus Appearance (2.4.13):** O indicador de foco (ex: `ring` do Tailwind) deve ter contraste $\ge$ 3:1 em relação ao estado não focado e uma área $\ge$ perímetro de 2 CSS pixels[cite: 25, 26, 39, 40].
- [cite_start]**Focus Not Obscured (2.4.11/12):** Elementos em foco NUNCA podem ser ocultados por *sticky headers* ou modais[cite: 23, 24].
- [cite_start]**Dragging Movements (2.5.7):** Funcionalidades de arrasto (ex: Kanban) devem ter alternativas de clique único (menus de contexto)[cite: 27, 36].
- [cite_start]**Reflow (1.4.10):** A interface deve suportar zoom de 400% (largura de 320px) sem rolagem bidimensional[cite: 41, 78].
- [cite_start]**Accessible Auth:** Proibido exigir cálculos ou memorização complexa no login; suporte pleno a preenchimento automático[cite: 31, 44].

## 2. Heurísticas de Nielsen Implementadas no Código
- [cite_start]**Visibilidade do Estado:** Use `aria-live="polite"` ou `role="status"` para mensagens dinâmicas sem interromper o utilizador.
- [cite_start]**Controlo e Liberdade (Pointer Cancellation):** Ações só ocorrem no `up-event` (`onMouseUp`/`onClick`), permitindo que o utilizador cancele arrastando para fora[cite: 49, 50].
- [cite_start]**Recuperação de Erros:** Erros de formulário devem focar o campo problemático e sugerir a correção em texto (WCAG 3.3.1 / 3.3.3)[cite: 56].
- [cite_start]**Estética Minimalista:** Maximize o *Data Ink Ratio* (remova decorações inúteis)[cite: 55].

## 3. Visualização de Dados (Dashboards)
[cite_start]Dashboards são fontes de "verdade única"[cite: 59]. [cite_start]Aplique a regra **3-30-300**[cite: 60]:
- [cite_start]**3 Segundos:** KPI principal altamente visível (Headline)[cite: 61]. [cite_start]Colocado no *Top-Left* (Eyeflow natural)[cite: 69].
- [cite_start]**30 Segundos:** Tendências fáceis via gráficos de linhas/barras[cite: 62].
- [cite_start]**300 Segundos:** Tabelas detalhadas e *drill-throughs*[cite: 63].
- [cite_start]**Data Quality Score:** Exiba a completude e atraso dos dados (ex: "Dados com 24h de atraso")[cite: 67].
- [cite_start]**Progressive Disclosure:** Esconda dados secundários em *Rich Tooltips*, mantendo o ecrã limpo[cite: 68]. [cite_start]Evite casas decimais irrelevantes[cite: 65].

## 4. Breakpoints e Mobile-First
- [cite_start]**Breakpoints Tailwind:** `sm: 640px`, `md: 768px`, `lg: 1024px`, `xl: 1280px`[cite: 77].
- [cite_start]**Mobile-First Real:** Elimine a dependência de estados `hover` para ações críticas (impossíveis em *touch*)[cite: 83].
- [cite_start]**Onboarding:** Utilize *AI-driven role-based onboarding* para reduzir o *time-to-value*[cite: 80, 81, 82].