"use client";

import React, { useState } from "react";
import { Sidebar } from "./Sidebar";
import { Header } from "./Header";
import { cn } from "@/lib/utils";

export function DashboardLayout({ children }: { children: React.ReactNode }) {
  const [isCollapsed, setIsCollapsed] = useState(true);

  return (
    <div className="flex h-screen overflow-hidden bg-background font-body-main text-on-background antialiased">
      {/* Sidebar gets the state and setter */}
      <Sidebar isCollapsed={isCollapsed} setIsCollapsed={setIsCollapsed} />
      
      {/* Main Content Area adapts to the sidebar width */}
      <div 
        className={cn(
          "flex-1 flex flex-col min-w-0 transition-all duration-300",
          isCollapsed ? "ml-20" : "ml-64"
        )}
      >
        <Header />
        <main className="flex-1 overflow-y-auto p-section-padding">
          <div className="max-w-7xl mx-auto space-y-container-gap">
            {children}
          </div>
        </main>
      </div>
    </div>
  );
}
