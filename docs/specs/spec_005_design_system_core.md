# Feature Spec: Design System e Arquitetura de UI (Core)

## 1. Contexto e Objetivo
Esta especificação define a "Fonte da Verdade" (Single Source of Truth) para a implementação visual e arquitetural de todas as telas do sistema. O objetivo é garantir consistência em tipografia, espaçamento, componentes e gerenciamento de estado.

## 2. Arquitetura de Layout (Macro)
O sistema adota um padrão responsivo (Mobile-first) em 3 painéis usando Flexbox e CSS Grid:
- **Global Container:** `flex h-screen w-full bg-[#F8FAFC] overflow-hidden`
- **Left Sidebar:** `w-20 lg:w-64 flex-shrink-0 bg-slate-900 text-slate-400`
- **Main Content:** `flex-1 flex flex-col overflow-y-auto px-8 py-6`
- **Right Panel:** `w-80 flex-shrink-0 border-l bg-white flex flex-col p-4`

## 3. Tipografia e Escala Visual
O mapeamento estrito de classes Tailwind deve ser respeitado:
- **Hero Title:** `text-3xl font-medium text-[#1E293B]`
- **Hero Subtitle:** `text-lg font-normal text-slate-500`
- **Card Titles:** `text-xl font-medium text-slate-800`
- **Card Body:** `text-sm font-normal text-slate-500 leading-relaxed`
- **Micro-copy:** `text-xs font-medium text-blue-500 hover:text-blue-700 transition-colors`
- **Notification Title:** `text-sm font-semibold text-slate-800`

## 4. Componentes e Segredos Visuais
- **Stack UI:** Uso estrito do Shadcn UI (Card, Input, Avatar, ScrollArea, Badge, Calendar) e Lucide React para ícones.
- **Hero Banners:** Nunca usar cor sólida. Utilizar gradientes sutis: `bg-gradient-to-r from-blue-50/50 to-slate-100 rounded-2xl`.
- **Watermarks (Marcas d'água):** Cards devem conter ícones de fundo com baixa opacidade em posição absoluta: `absolute -bottom-4 -right-4 text-slate-100 w-32 h-32 -z-10`.
- **Bordas e Sombras:** O padrão global para cards brancos é `border border-slate-100 shadow-sm rounded-xl bg-white`.

## 5. Gestão de Estado e Contratos
- O estado global é gerenciado pelo **Zustand**.
- O estado local (`useState`) é restrito a micro-interações (ex: toggles, datas no Calendar).
- Todo dado consumido por componentes UI DEVE ser validado via **Zod Schema**.