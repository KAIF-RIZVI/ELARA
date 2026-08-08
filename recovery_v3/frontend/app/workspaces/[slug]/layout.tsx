"use client";

import React from "react";
import { WorkspaceProvider } from "@/contexts/workspace-context";
import { Sidebar } from "@/components/layout/sidebar";
import { Header } from "@/components/layout/header";

export default function WorkspaceLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: { slug: string };
}) {
  return (
    <WorkspaceProvider slug={params.slug}>
      <div className="flex h-screen overflow-hidden bg-background">
        <Sidebar workspaceSlug={params.slug} />
        <div className="flex-1 flex flex-col overflow-hidden">
          <Header onMenuClick={() => {}} />
          <main className="flex-1 overflow-y-auto bg-slate-50/50 dark:bg-slate-950 p-6">
            {children}
          </main>
        </div>
      </div>
    </WorkspaceProvider>
  );
}