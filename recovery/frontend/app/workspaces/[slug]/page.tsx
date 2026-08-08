"use client";

import { useWorkspace } from "@/contexts/workspace-context";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Users, GitPullRequest, FolderGit2, Cpu } from "lucide-react";

export default function WorkspaceDashboardPage() {
  const { workspace, isLoading, error } = useWorkspace();

  if (isLoading) {
    return <div className="p-8 text-center text-muted-foreground animate-pulse">Loading workspace...</div>;
  }

  if (error || !workspace) {
    return <div className="p-8 text-center text-red-500">Error loading workspace</div>;
  }

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">{workspace.name}</h1>
          <p className="text-muted-foreground mt-2">
            {workspace.description || "Manage your repositories, team, and settings."}
          </p>
        </div>
      </div>

      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
        <Card className="bg-white/5 border-white/10 backdrop-blur-sm">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">Projects</CardTitle>
            <FolderGit2 className="h-4 w-4 text-emerald-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-white">{workspace.projects_count}</div>
            <p className="text-xs text-muted-foreground mt-1">Active projects</p>
          </CardContent>
        </Card>

        <Card className="bg-white/5 border-white/10 backdrop-blur-sm">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">Repositories</CardTitle>
            <GitPullRequest className="h-4 w-4 text-blue-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-white">{workspace.repositories_count}</div>
            <p className="text-xs text-muted-foreground mt-1">Connected repos</p>
          </CardContent>
        </Card>

        <Card className="bg-white/5 border-white/10 backdrop-blur-sm">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">Team Members</CardTitle>
            <Users className="h-4 w-4 text-amber-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-white">{workspace.members_count}</div>
            <p className="text-xs text-muted-foreground mt-1">Active users</p>
          </CardContent>
        </Card>

        <Card className="bg-white/5 border-white/10 backdrop-blur-sm">
          <CardHeader className="flex flex-row items-center justify-between pb-2">
            <CardTitle className="text-sm font-medium text-muted-foreground">AI Credits</CardTitle>
            <Cpu className="h-4 w-4 text-purple-500" />
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-white">{workspace.ai_credits_remaining.toLocaleString()}</div>
            <p className="text-xs text-muted-foreground mt-1">Units available</p>
          </CardContent>
        </Card>
      </div>
      
      {/* Recent Activity placeholder could go here */}
      <Card className="bg-white/5 border-white/10 backdrop-blur-sm">
        <CardHeader>
          <CardTitle>Recent Activity</CardTitle>
          <CardDescription>Activity log will appear here</CardDescription>
        </CardHeader>
        <CardContent className="h-32 flex items-center justify-center text-muted-foreground">
          No recent activity found.
        </CardContent>
      </Card>
    </div>
  );
}