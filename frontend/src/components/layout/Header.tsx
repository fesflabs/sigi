import React from "react";
import Image from "next/image";
import { Search, Bell, History, HelpCircle } from "lucide-react";

export function Header() {
  return (
    <header className="sticky top-0 right-0 flex justify-between items-center px-6 py-3 w-full z-30 bg-white/80 backdrop-blur-md dark:bg-slate-950/80 border-b border-slate-200 dark:border-slate-800">
      <div className="text-xl font-black text-slate-800 dark:text-slate-100 font-manrope">
        ERP Modular
      </div>

      <div className="flex-1 max-w-md mx-6 ml-auto">
        <div className="relative focus-within:ring-2 focus-within:ring-blue-500/20 rounded-lg">
          <Search
            size={18}
            className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"
            aria-hidden="true"
          />
          <input
            type="text"
            className="w-full bg-surface-container pl-10 pr-4 py-2 rounded-lg border-0 text-sm font-manrope font-medium text-slate-800 dark:text-slate-200 dark:bg-slate-900 focus:ring-0 placeholder:text-text-placeholder transition-colors"
            placeholder="Buscar no sistema..."
            aria-label="Buscar no sistema"
          />
        </div>
      </div>

      <div className="flex items-center gap-4">
        <button
          className="p-1 text-slate-500 dark:text-slate-400 hover:text-blue-700 dark:hover:text-blue-300 transition-colors rounded-full focus:ring-2 focus:ring-blue-500/20"
          aria-label="Notificações"
        >
          <Bell size={20} />
        </button>
        <button
          className="p-1 text-slate-500 dark:text-slate-400 hover:text-blue-700 dark:hover:text-blue-300 transition-colors rounded-full focus:ring-2 focus:ring-blue-500/20"
          aria-label="Histórico de Ações"
        >
          <History size={20} />
        </button>
        <button
          className="p-1 text-slate-500 dark:text-slate-400 hover:text-blue-700 dark:hover:text-blue-300 transition-colors rounded-full focus:ring-2 focus:ring-blue-500/20"
          aria-label="Ajuda"
        >
          <HelpCircle size={20} />
        </button>
        
        {/* Placeholder Avatar para manter a independência de pacote */}
        <div className="w-8 h-8 rounded-full ml-2 border border-slate-200 bg-primary/20 flex items-center justify-center overflow-hidden shrink-0">
           <span className="text-xs font-bold text-primary">US</span>
        </div>
      </div>
    </header>
  );
}
