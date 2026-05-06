import React, { Suspense } from "react";
import { BentoGrid } from "@/components/dashboard/BentoGrid";
import { ActivityChart } from "@/components/dashboard/ActivityChart";
import { RecentActions } from "@/components/dashboard/RecentActions";

export default function Home() {
  return (
    <>
      {/* Page Header */}
      <div className="flex justify-between items-end mb-8">
        <div>
          <h2 className="font-heading-start text-heading-start text-text-heading mb-1">
            Dashboard Geral
          </h2>
          <p className="font-text-muted text-text-muted text-outline">
            Visão consolidada de todos os módulos de gestão.
          </p>
        </div>
        <div className="text-sm font-body-main text-on-surface-variant bg-surface-container-low px-4 py-2 rounded-lg border border-outline-variant/30">
          Última atualização: Hoje, 09:42
        </div>
      </div>

      {/* Bento Grid Summary */}
      <BentoGrid />

      {/* Recent Activity & Chart Area */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-grid-gutter mt-8">
        <Suspense fallback={<div className="lg:col-span-2 h-[300px] bg-surface rounded-xl animate-pulse" />}>
          <ActivityChart />
        </Suspense>

        <Suspense fallback={<div className="h-[300px] bg-surface rounded-xl animate-pulse" />}>
          <RecentActions />
        </Suspense>
      </div>
    </>
  );
}
