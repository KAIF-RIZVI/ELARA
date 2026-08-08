"use client";

import { useQuery } from "@tanstack/react-query";
import { fetcher, Workspace } from "@/lib/api-client";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Loader2, Coins, Key, ShieldAlert } from "lucide-react";
import { Separator } from "@/components/ui/separator";

export default function SettingsPage() {
  const { data: workspaces, isLoading } = useQuery<Workspace[]>({
    queryKey: ["workspaces"],
    queryFn: () => fetcher("/api/v1/workspaces"),
  });
  const activeWorkspace = workspaces?.[0];

  return (
    <div className="flex flex-col gap-8 pb-8 max-w-4xl">
      <div>
        <h1 className="text-3xl font-bold tracking-tight text-white mb-2">Settings</h1>
        <p className="text-muted-foreground">Manage your workspace configuration, API keys, and billing.</p>
      </div>

      {isLoading ? (
        <div className="flex justify-center p-12">
          <Loader2 className="w-8 h-8 animate-spin text-muted-foreground" />
        </div>
      ) : (
        <div className="flex flex-col gap-8">
          {/* General Settings */}
          <Card className="bg-zinc-950/50 border-white/5 backdrop-blur-sm">
            <CardHeader>
              <CardTitle>Workspace Profile</CardTitle>
              <CardDescription>Update your workspace name and identifier.</CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="workspace-name" className="text-white">Workspace Name</Label>
                <Input 
                  id="workspace-name" 
                  defaultValue={activeWorkspace?.name || ""} 
                  className="bg-zinc-900 border-white/10 text-white max-w-md"
                />
              </div>
              <div className="space-y-2">
                <Label htmlFor="workspace-slug" className="text-white">Workspace Slug</Label>
                <div className="flex items-center gap-2 max-w-md">
                  <span className="text-muted-foreground bg-zinc-900 px-3 py-2 rounded-md border border-white/10 text-sm">elara.dev/</span>
                  <Input 
                    id="workspace-slug" 
                    defaultValue={activeWorkspace?.slug || ""} 
                    className="bg-zinc-900 border-white/10 text-white flex-1"
                    disabled
                  />
                </div>
                <p className="text-xs text-muted-foreground mt-1">Slugs cannot be changed after creation.</p>
              </div>
            </CardContent>
            <CardFooter className="border-t border-white/5 pt-4">
              <Button className="bg-primary text-primary-foreground hover:bg-primary/90">Save Changes</Button>
            </CardFooter>
          </Card>

          {/* AI Remediations Wallet */}
          <Card className="bg-zinc-950/50 border-white/5 backdrop-blur-sm">
            <CardHeader className="flex flex-row items-center justify-between pb-2">
              <div className="space-y-1">
                <CardTitle className="flex items-center gap-2">
                  <Coins className="w-5 h-5 text-amber-500" />
                  AI Remediation Wallet
                </CardTitle>
                <CardDescription>Monitor your monthly AI bug-fixing allowance.</CardDescription>
              </div>
              <div className="text-right">
                <div className="text-2xl font-bold text-white">5,000 <span className="text-sm font-normal text-muted-foreground">/ 5,000</span></div>
                <div className="text-xs text-emerald-400">Active (Free Plan)</div>
              </div>
            </CardHeader>
            <CardContent>
              <div className="w-full bg-zinc-900 rounded-full h-2 mt-4">
                <div className="bg-gradient-to-r from-emerald-500 to-amber-500 h-2 rounded-full" style={{ width: "100%" }}></div>
              </div>
              <p className="text-xs text-muted-foreground mt-3">Your wallet recharges on September 1st, 2026.</p>
            </CardContent>
            <CardFooter className="border-t border-white/5 pt-4">
              <Button variant="outline" className="bg-zinc-900 border-white/10 text-white hover:bg-white/10">Upgrade to Pro</Button>
            </CardFooter>
          </Card>

          {/* API Keys */}
          <Card className="bg-zinc-950/50 border-white/5 backdrop-blur-sm">
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Key className="w-5 h-5 text-blue-500" />
                API Keys
              </CardTitle>
              <CardDescription>Generate keys for CI/CD integrations (e.g. GitHub Actions).</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="text-center p-8 border border-dashed border-white/10 rounded-lg">
                <Key className="w-8 h-8 text-zinc-500/50 mx-auto mb-3" />
                <p className="text-sm font-medium text-white mb-1">No API Keys Generated</p>
                <p className="text-xs text-muted-foreground mb-4">You need an API key to run ELARA directly in your CI pipeline.</p>
                <Button className="bg-white text-black hover:bg-white/90">Generate New Key</Button>
              </div>
            </CardContent>
          </Card>

          {/* Danger Zone */}
          <Card className="bg-rose-500/5 border-rose-500/20 backdrop-blur-sm">
            <CardHeader>
              <CardTitle className="flex items-center gap-2 text-rose-500">
                <ShieldAlert className="w-5 h-5" />
                Danger Zone
              </CardTitle>
              <CardDescription className="text-rose-500/70">Irreversible actions for your workspace.</CardDescription>
            </CardHeader>
            <CardContent className="space-y-4">
              <div className="flex items-center justify-between p-4 border border-rose-500/20 rounded-lg bg-rose-500/5">
                <div>
                  <h4 className="font-medium text-white">Delete Workspace</h4>
                  <p className="text-sm text-rose-500/70">Permanently delete this workspace and all of its data. This cannot be undone.</p>
                </div>
                <Button variant="destructive" className="bg-rose-600 hover:bg-rose-700 text-white">Delete Workspace</Button>
              </div>
            </CardContent>
          </Card>
        </div>
      )}
    </div>
  );
}