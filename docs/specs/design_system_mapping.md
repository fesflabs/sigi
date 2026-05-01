# Spec: Design System & UI Mapping

## 1. Visão Geral
Este documento é a "Fonte da Verdade" (SSOT) para a tradução de protótipos visuais (Figma) em código Frontend. Ele mapeia cores hexadecimais (Magic Strings) para os Design Tokens oficiais do Tailwind CSS. O Agente IA deve consultar esta Spec toda vez que for estilizar um novo componente, não importando a feature.

## 2. Dicionário de Cores (De -> Para)

### Fundos e Superfícies
| Figma (Proibido) | Tailwind Token (Obrigatório) | Contexto de Uso |
| :--- | :--- | :--- |
| `bg-[#798DDE]/15` | `bg-primary/15` | Fundos baseados na cor primária (Cards, destaques). |
| `bg-[#F7F9FC]` | `bg-white` ou `bg-surface` | Fundos de contêineres e formulários. |
| `bg-[#EBEBEB]` | `bg-surface` | Fundos cinzas para áreas de arquivos/anexos. |
| `bg-[#EDEDED]/50` | `bg-background` | Fundo base de páginas ou seções inativas. |
| `bg-[#E2E8F0]` | `bg-input-disabledBg` | Fundo exclusivo para Inputs desabilitados. |

### Textos e Tipografia
| Figma (Proibido) | Tailwind Token (Obrigatório) | Contexto de Uso |
| :--- | :--- | :--- |
| `#4B5563`, `#5D5D5D`| `text-text-heading` / `text-heading-start`| Títulos principais e cabeçalhos escuros. |
| `#8A8A8A`, `#919191`| `text-text-muted` | Textos auxiliares e rótulos neutros. (Nota: Se `#8A8A8A` estiver sobre fundo branco, use `#4E5969` para contraste WCAG). |
| `#B7B7B7`, `#CDCDCD`| `text-text-placeholder` | Placeholders de input e textos secundários. |
| `#4E5969/70` | `placeholder:text-text-main/70` | Textos de inputs padrão. |

### Bordas e Divisores
| Figma (Proibido) | Tailwind Token (Obrigatório) | Contexto de Uso |
| :--- | :--- | :--- |
| `border-[#59BCD6]` | `border-status-info` | Borda principal (ex: Valor total do contrato). |
| `border-[#7A8CDE]` | `border-status-accent` | Borda secundária (ex: Valor alocado). |
| `border-[#4E5969]` | `border-status-dark` | Borda de dados neutros (ex: Valor não utilizado). |
| `border-[#5279AF]` | `border-heading-end` ou `primary` | Bordas de cabeçalhos de Modais. |
| `border-[#8A8A8A]`, `#D9D9D9/30` | `border-border` ou `border-action-cancel` | Bordas de inputs e separadores padrão. |

### Botões e Interações
| Ação / Intenção | Classes Tailwind Obrigatórias |
| :--- | :--- |
| **Ação Positiva / Salvar**| `bg-action-save hover:bg-action-saveHover text-white` (Substitui `#89D4E1` e `#72bccc`) |
| **Ação Secundária / Subitem**| `bg-status-info hover:bg-status-info/90 text-white` (Substitui `#89D4E1`) |
| **Cancelar / Excluir (Neutro)**| `bg-border hover:bg-text-muted text-white` (Substitui `#939393` / `#8A8A8A`) |

---

## 3. Comportamento Canônico de Componentes

### A. Estrutura de Layout e Responsividade
- **Proibição de Absolute:** É estritamente proibido o uso de `position: absolute` associado a coordenadas fixas (ex: `left: 167px`, `top: 150px`) copiadas do Figma.
- **Grids e Flexbox:** Utilize CSS Grid (12 colunas) ou `flex flex-col` com `gap` para listagens e dashboards (ex: `ContractGridCard`).
- **Scroll e Overflow:** Não utilize `overflow-y: scroll` puro. Para listas de rolagem, envolva o conteúdo no componente `<ScrollArea>` do Shadcn UI. Oculte barras de rolagem nativas (`::-webkit-scrollbar { display: none; }`) se inevitável.

### B. Modais (Dialog) e Badges
- **Modais Shadcn:** O `DialogContent` deve sempre conter a classe base: `border-0 shadow-2xl backdrop-blur-sm bg-modal-bg`.
- **Status Badges:** Baseados puramente em booleanos (`isActive`).
  - *Ativo:* `bg-status-activeBg text-status-activeText`.
  - *Inativo:* `bg-status-inactiveBg text-status-inactiveText`.

### C. Acessibilidade (WCAG)
- Indicadores visuais não-textuais (como bolinhas de status) devem conter `aria-hidden="true"`.
- Respeite o contraste mínimo. Cores como `#8A8A8A` sob fundos brancos devem ser escurecidas para `text-[#4E5969]` ou mapeadas para `text-text-muted` caso o token já contemple a correção.