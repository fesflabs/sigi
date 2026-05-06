import React from "react";
// Assumindo que o componente ScrollArea será gerado via shadcn CLI
// import { ScrollArea } from "@/components/ui/scroll-area";

export function RecentActions() {
  return (
    <div className="bg-surface rounded-xl border border-outline-variant/30 p-6 flex flex-col min-h-[300px]">
      <div className="flex justify-between items-center mb-6">
        <h3 className="font-heading-modal text-heading-modal text-on-surface">Ações Recentes</h3>
        <button className="text-primary hover:text-on-primary-fixed-variant text-sm font-semibold font-body-main transition-colors">
          Ver todas
        </button>
      </div>
      
      {/* 
        Aviso: A regra de UI exige o uso de <ScrollArea>. 
        Como os componentes Shadcn não foram instalados pelo agente devido a restrições, 
        estamos usando um div provisório. Substitua por <ScrollArea className="flex-1 pr-2">
      */}
      <div className="flex-1 overflow-y-auto pr-2 space-y-4">
        <div className="flex items-center justify-center h-full text-text-muted text-sm italic">
          Nenhuma ação recente para exibir.
        </div>
      </div>
    </div>
  );
}
