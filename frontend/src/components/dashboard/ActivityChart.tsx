import React from "react";

export function ActivityChart() {
  return (
    <div className="lg:col-span-2 bg-surface rounded-xl border border-outline-variant/30 p-6 flex flex-col min-h-[300px]">
      <div className="flex justify-between items-center mb-6">
        <h3 className="font-heading-modal text-heading-modal text-on-surface">Visão Geral de Atividades</h3>
        <select 
          className="bg-surface-container-low border border-outline-variant/50 rounded-md text-sm font-body-main px-3 py-1.5 focus:ring-primary focus:border-primary text-on-surface"
          aria-label="Selecionar período do gráfico"
        >
          <option>Últimos 7 dias</option>
          <option>Últimos 30 dias</option>
          <option>Este ano</option>
        </select>
      </div>

      {/* Chart Area */}
      <div className="flex-1 flex items-center justify-center border-b border-l border-outline-variant/30 relative">
        <p className="text-text-muted font-text-muted text-sm">
          Os dados do gráfico serão carregados aqui.
        </p>
      </div>
    </div>
  );
}
