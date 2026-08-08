"use client";

import { useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { fetcher, Workspace, Bug } from "@/lib/api-client";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Loader2, Bug as BugIcon, AlertCircle, AlertTriangle, Info, ShieldAlert, CheckCircle2 } from "lucide-react";
import { Button } from "@/components/ui/button";
import { motion } from "framer-motion";

export default function BugsPage() {
  const { data: workspaces } = useQuery<Workspace[]>({
    queryKey: ["workspaces"],
    queryFn: () => fetcher("/api/v1/workspaces"),
  });
  const activeWorkspaceId = workspaces?.[0]?.id;

  const { data: bugs, isLoading } = useQuery<Bug[]>({
    queryKey: ["workspace", activeWorkspaceId, "bugs"],
    queryFn: () => fetcher(`/api/v1/bugs?workspace_id=${activeWorkspaceId}`),
    enabled: !!activeWorkspaceId,
  });

  const getSeverityIcon = (severity: string) => {
    switch (severity) {
      case 'CRITICAL': return <ShieldAlert className="w-4 h-4 text-rose-500" />;
      case 'HIGH': return <AlertTriangle className="w-4 h-4 text-orange-500" />;
      case 'MEDIUM': return <AlertCircle className="w-4 h-4 text-amber-500" />;
      case 'LOW': return <Info className="w-4 h-4 text-blue-500" />;
      default: return <Info className="w-4 h-4 text-zinc-500" />;
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'OPEN': return 'bg-rose-500/10 text-rose-400 border-rose-500/20';
      case 'TRIAGED': return 'bg-amber-500/10 text-amber-400 border-amber-500/20';
      case 'IN_PROGRESS': return 'bg-blue-500/10 text-blue-400 border-blue-500/20';
      case 'RESOLVED': return 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20';
      case 'CLOSED': return 'bg-zinc-500/10 text-zinc-400 border-zinc-500/20';
      default: return 'bg-zinc-500/10 text-zinc-400 border-zinc-500/20';
    }
  };

  return (
    <div className="flex flex-col gap-8 pb-8">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight text-white mb-2">Bug Triage</h1>
          <p className="text-muted-foreground">Review, assign, and auto-remediate issues detected in your repositories.</p>
        </div>
        <Button className="bg-primary text-primary-foreground hover:bg-primary/90">
          Run System Scan
        </Button>
      </div>

      <Card className="bg-zinc-950/50 border-white/5 backdrop-blur-sm overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-sm text-left">
            <thead className="text-xs text-muted-foreground uppercase bg-zinc-900/50 border-b border-white/5">
              <tr>
                <th className="px-6 py-4 font-medium">Issue</th>
                <th className="px-6 py-4 font-medium">Severity</th>
                <th className="px-6 py-4 font-medium">Status</th>
                <th className="px-6 py-4 font-medium">Created</th>
                <th className="px-6 py-4 font-medium text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-white/5">
              {isLoading ? (
                <tr>
                  <td colSpan={5} className="px-6 py-12 text-center">
                    <Loader2 className="w-6 h-6 animate-spin text-muted-foreground mx-auto" />
                  </td>
                </tr>
              ) : !bugs || bugs.length === 0 ? (
                <tr>
                  <td colSpan={5} className="px-6 py-16 text-center">
                    <CheckCircle2 className="w-12 h-12 text-emerald-500/30 mx-auto mb-4" />
                    <h3 className="text-lg font-medium text-white mb-1">Inbox Zero</h3>
                    <p className="text-muted-foreground mb-4">No active bugs found in your connected repositories.</p>
                  </td>
                </tr>
              ) : (
                bugs.map((bug) => (
                  <tr key={bug.id} className="bg-transparent hover:bg-white/[0.02] transition-colors">
                    <td className="px-6 py-4">
                      <div className="flex items-center gap-3">
                        <div className="w-8 h-8 rounded-lg bg-zinc-900 flex items-center justify-center border border-white/5 flex-shrink-0">
                          <BugIcon className="w-4 h-4 text-white/50" />
                        </div>
                        <div>
                          <div className="font-medium text-white">{bug.title}</div>
                          <div className="text-xs text-muted-foreground truncate max-w-md">
                            {bug.description || "No description provided."}
                          </div>
                        </div>
                      </div>
                    </td>
                    <td className="px-6 py-4">
                      <div className="flex items-center gap-1.5">
                        {getSeverityIcon(bug.severity)}
                        <span className="text-xs font-medium text-zinc-300">{bug.severity}</span>
                      </div>
                    </td>
                    <td className="px-6 py-4">
                      <div className={`inline-flex items-center px-2.5 py-1 rounded-full text-xs font-medium border ${getStatusColor(bug.status)}`}>
                        {bug.status}
                      </div>
                    </td>
                    <td className="px-6 py-4 text-muted-foreground text-xs">
                      {new Date(bug.created_at).toLocaleDateString()}
                    </td>
                    <td className="px-6 py-4 text-right">
                      <Button variant="outline" size="sm" className="bg-zinc-900 border-white/10 hover:bg-primary/20 hover:text-primary transition-colors">
                        Auto-Fix
                      </Button>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </Card>
    </div>
  );
}