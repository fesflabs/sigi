import React from "react";
import { Package, Banknote, Car, Headset, Shapes, Building2, TrendingUp, AlertTriangle } from "lucide-react";

interface KPICardProps {
  title: string;
  icon: React.ReactNode;
  value: string | number;
  subtitle: string;
  trend?: {
    value: string;
    icon: React.ReactNode;
    colorClass: string;
  };
  colorClass: string;
  iconBgClass: string;
}

function KPICard({ title, icon, value, subtitle, trend, colorClass, iconBgClass }: KPICardProps) {
  return (
    <div className="bg-surface rounded-xl p-5 border border-outline-variant/30 relative overflow-hidden group">
      <div className={`absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity ${colorClass}`}>
        {icon}
      </div>
      <div className="flex items-center gap-3 mb-4">
        <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${iconBgClass}`}>
          {icon}
        </div>
        <h3 className="font-heading-modal text-heading-modal text-on-surface">{title}</h3>
      </div>
      <div className="space-y-1">
        <p className="font-text-muted text-text-muted text-outline">{subtitle}</p>
        <div className="flex items-baseline gap-2">
          <span className={`text-3xl font-bold font-heading-start ${colorClass}`}>{value}</span>
          {trend ? (
             <span className={`text-sm font-label-caps text-label-caps flex items-center ${trend.colorClass}`}>
                {trend.icon} <span className="ml-1">{trend.value}</span>
             </span>
          ) : (
            <span className="text-sm font-label-caps text-label-caps text-on-surface-variant">
              ---
            </span>
          )}
        </div>
      </div>
    </div>
  );
}

export function BentoGrid() {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-grid-gutter">
      <KPICard
        title="Almoxarifado"
        icon={<Package size={24} />}
        value="-"
        subtitle="Itens com estoque baixo"
        colorClass="text-error"
        iconBgClass="bg-primary-fixed text-primary-fixed-variant"
        trend={{ value: "+-", icon: <TrendingUp size={16} />, colorClass: "text-error" }}
      />
      <KPICard
        title="Diárias"
        icon={<Banknote size={24} />}
        value="-"
        subtitle="Solicitações pendentes"
        colorClass="text-on-surface"
        iconBgClass="bg-secondary-container text-on-secondary-container"
      />
      <KPICard
        title="Frota"
        icon={<Car size={24} />}
        value="-"
        subtitle="Veículos reservados hoje"
        colorClass="text-on-surface"
        iconBgClass="bg-tertiary-fixed text-on-tertiary-fixed"
      />
      <KPICard
        title="Suporte"
        icon={<Headset size={24} />}
        value="-"
        subtitle="Chamados abertos"
        colorClass="text-on-surface"
        iconBgClass="bg-surface-container-highest text-on-surface-variant"
        trend={{ value: "- Urgentes", icon: <AlertTriangle size={16} />, colorClass: "text-status-info" }}
      />
      <KPICard
        title="Ativos"
        icon={<Shapes size={24} />}
        value="-"
        subtitle="Ativos em manutenção"
        colorClass="text-on-surface"
        iconBgClass="bg-primary/10 text-primary"
      />
      <KPICard
        title="Reserva de Espaço"
        icon={<Building2 size={24} />}
        value="-"
        subtitle="Salas ocupadas hoje"
        colorClass="text-on-surface"
        iconBgClass="bg-status-accent/20 text-status-accent"
      />
    </div>
  );
}
