"use client";

import { useState } from "react";
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { fetcher, Workspace, Repository } from "@/lib/api-client";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Loader2, GitPullRequest, Search, Plus, ExternalLink, RefreshCw, Trash2, CheckCircle2, XCircle } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog";

export default function RepositoriesPage() {
  const queryClient = useQueryClient();
  const [isConnectOpen, setIsConnectOpen] = useState(false);
  const [connectUrl, setConnectUrl] = useState("");
  
  const { data: workspaces } = useQuery<Workspace[]>({
    queryKey: ["workspaces"],
    queryFn: () => fetcher("/api/v1/workspaces"),
  });
  const activeWorkspaceId = workspaces?.[0]?.id;

  const { data: repositories, isLoading } = useQuery<Repository[]>({
    queryKey: ["workspace", activeWorkspaceId, "repositories"],
    queryFn: () => fetcher(`/api/v1/repositories?workspace_id=${activeWorkspaceId}`),
    enabled: !!activeWorkspaceId,
  });

  const connectMutation = useMutation({
    mutationFn: async (url: string) => {
      // Very basic URL parser for github.com/owner/repo
      const match = url.match(/github\.com\/([^/]+)\/([^/.]+)/);
      if (!match) throw new Error("Invalid GitHub URL");
      
      const res = await fetch("/api/v1/repositories", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({
          workspace_id: activeWorkspaceId,
          provider: "github",
          full_name: `${match[1]}/${match[2]}`,
          external_id: `${match[1]}-${match[2]}`.toLowerCase(), // Fake external ID for MVP
          default_branch: "main"
        })
      });
      if (!res.ok) throw new Error(await res.text());
      return res.json();
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["workspace", activeWorkspaceId, "repositories"] });
      setIsConnectOpen(false);
      setConnectUrl("");
    }
  });

  const syncMutation = useMutation({
    mutationFn: async (repoId: string) => {
      const res = await fetch(`/api/v1/repositories/${repoId}/sync?workspace_id=${activeWorkspaceId}`, {
        method: "POST",
        credentials: "include",
      });
      if (!res.ok) throw new Error(await res.text());
    },
    onSuccess: () => {
      // In a real app, you might optimistically update or refetch
    }
  });

  const deleteMutation = useMutation({
    mutationFn: async (repoId: string) => {
      const res = await fetch(`/api/v1/repositories/${repoId}?workspace_id=${activeWorkspaceId}`, {
        method: "DELETE",
        credentials: "include",
      });
      if (!res.ok) throw new Error(await res.text());
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["workspace", activeWorkspaceId, "repositories"] });
    }
  });

  return (
    <div className="flex flex-col gap-8 pb-8">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight text-white mb-2">Repositories</h1>
          <p className="text-muted-foreground">Manage connected codebases and AI index status.</p>
        </div>
        
        <Dialog open={isConnectOpen} onOpenChange={setIsConnectOpen}>
          <DialogTrigger 
            render={
              <Button className="bg-primary text-primary-foreground hover:bg-primary/90">
                <Plus className="w-4 h-4 mr-2" />
                Connect Repository
              </Button>
            }
          />
          <DialogContent className="bg-zinc-950 border-white/10 text-white sm:max-w-[425px]">
            <DialogHeader>
              <DialogTitle>Connect Repository</DialogTitle>
              <DialogDescription className="text-muted-foreground">
                Enter the GitHub URL of the repository you want ELARA to analyze.
              </DialogDescription>
            </DialogHeader>
            <div className="grid gap-4 py-4">
              <div className="flex flex-col gap-2">
                <Input 
                  placeholder="https://github.com/facebook/react" 
                  value={connectUrl}
                  onChange={(e) => setConnectUrl(e.target.value)}
                  className="bg-zinc-900 border-white/10 text-white"
                />
              </div>
              {connectMutation.isError && (
                <div className="text-sm text-destructive font-medium">
                  Failed to connect: {connectMutation.error.message}
                </div>
              )}
            </div>
            <DialogFooter>
              <Button variant="outline" onClick={() => setIsConnectOpen(false)} className="bg-zinc-900 border-white/10 text-white hover:bg-white/10 hover:text-white">
                Cancel
              </Button>
              <Button 
                onClick={() => connectMutation.mutate(connectUrl)} 
                disabled={!connectUrl || connectMutation.isPending}
                className="bg-primary text-primary-foreground hover:bg-primary/90"
              >
                {connectMutation.isPending ? <Loader2 className="w-4 h-4 mr-2 animate-spin" /> : "Connect"}
              </Button>
            </DialogFooter>
          </DialogContent>
        </Dialog>
      </div>

      <Card className="bg-zinc-950/50 border-white/5 backdrop-blur-sm overflow-hidden">
        <div className="p-4 border-b border-white/5 flex items-center gap-4">
          <div className="relative flex-1 max-w-sm">
            <Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
            <Input
              type="search"
              placeholder="Search repositories..."
              className="w-full bg-zinc-900 border-white/10 pl-9 text-white focus-visible:ring-primary"
            />
          </div>
        </div>
        
        <div className="overflow-x-auto">
          <table className="w-full text-sm text-left">
            <thead className="text-xs text-muted-foreground uppercase bg-zinc-900/50 border-b border-white/5">
              <tr>
                <th className="px-6 py-4 font-medium">Repository</th>
                <th className="px-6 py-4 font-medium">Status</th>
                <th className="px-6 py-4 font-medium">Last Indexed</th>
                <th className="px-6 py-4 font-medium text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-white/5">
              {isLoading ? (
                <tr>
                  <td colSpan={4} className="px-6 py-12 text-center">
                    <Loader2 className="w-6 h-6 animate-spin text-muted-foreground mx-auto" />
                  </td>
                </tr>
              ) : !repositories || repositories.length === 0 ? (
                <tr>
                  <td colSpan={4} className="px-6 py-16 text-center">
                    <GitPullRequest className="w-12 h-12 text-muted-foreground/30 mx-auto mb-4" />
                    <h3 className="text-lg font-medium text-white mb-1">No repositories connected</h3>
                    <p className="text-muted-foreground mb-4">Connect a Git repository to start analyzing code and fixing bugs.</p>
                    <Button onClick={() => setIsConnectOpen(true)} className="bg-white text-black hover:bg-white/90">
                      Connect your first repo
                    </Button>
                  </td>
                </tr>
              ) : (
                repositories.map((repo) => (
                  <tr key={repo.id} className="bg-transparent hover:bg-white/[0.02] transition-colors">
                    <td className="px-6 py-4">
                      <div className="flex items-center gap-3">
                        <div className="w-8 h-8 rounded-full bg-zinc-800 flex items-center justify-center flex-shrink-0">
                          {/* We can put github icon here, using GitPullRequest for now */}
                          <GitPullRequest className="w-4 h-4 text-white/70" />
                        </div>
                        <div>
                          <div className="font-medium text-white flex items-center gap-2">
                            {repo.full_name}
                            <a href={`https://github.com/${repo.full_name}`} target="_blank" rel="noreferrer" className="text-muted-foreground hover:text-white transition-colors">
                              <ExternalLink className="w-3 h-3" />
                            </a>
                          </div>
                          <div className="text-xs text-muted-foreground">Default branch: {repo.default_branch}</div>
                        </div>
                      </div>
                    </td>
                    <td className="px-6 py-4">
                      {repo.sync_status === 'COMPLETED' ? (
                        <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                          <CheckCircle2 className="w-3.5 h-3.5" />
                          Indexed
                        </div>
                      ) : repo.sync_status === 'FAILED' ? (
                        <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-rose-500/10 text-rose-400 border border-rose-500/20">
                          <XCircle className="w-3.5 h-3.5" />
                          Failed
                        </div>
                      ) : repo.sync_status === 'SYNCING' ? (
                        <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-blue-500/10 text-blue-400 border border-blue-500/20">
                          <Loader2 className="w-3.5 h-3.5 animate-spin" />
                          Syncing
                        </div>
                      ) : (
                        <div className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-zinc-500/10 text-zinc-400 border border-zinc-500/20">
                          Pending
                        </div>
                      )}
                    </td>
                    <td className="px-6 py-4 text-muted-foreground">
                      {repo.last_synced_at ? new Date(repo.last_synced_at).toLocaleString() : 'Never'}
                    </td>
                    <td className="px-6 py-4 text-right">
                      <div className="flex items-center justify-end gap-2">
                        <Button 
                          variant="ghost" 
                          size="icon"
                          title="Force Sync"
                          onClick={() => syncMutation.mutate(repo.id)}
                          disabled={syncMutation.isPending || repo.sync_status === 'SYNCING'}
                          className="text-muted-foreground hover:text-white hover:bg-white/10"
                        >
                          <RefreshCw className={`w-4 h-4 ${syncMutation.isPending ? 'animate-spin' : ''}`} />
                        </Button>
                        <Button 
                          variant="ghost" 
                          size="icon" 
                          title="Disconnect"
                          onClick={() => {
                            if(confirm(`Are you sure you want to disconnect ${repo.full_name}?`)) {
                              deleteMutation.mutate(repo.id);
                            }
                          }}
                          disabled={deleteMutation.isPending}
                          className="text-muted-foreground hover:text-rose-500 hover:bg-rose-500/10"
                        >
                          <Trash2 className="w-4 h-4" />
                        </Button>
                      </div>
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