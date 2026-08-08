"use client";

import { useWorkspace } from "@/contexts/workspace-context";
import { useQuery } from "@tanstack/react-query";
import { fetcher } from "@/lib/api-client";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Plus, FolderGit2, GitPullRequest } from "lucide-react";
import { Badge } from "@/components/ui/badge";

export default function WorkspaceProjectsPage() {
  const { workspace } = useWorkspace();
  
  const { data: projects, isLoading } = useQuery({
    queryKey: ["workspace_projects", workspace?.id],
    queryFn: () => fetcher(`/api/v1/workspaces/${workspace?.id}/projects`),
    enabled: !!workspace?.id,
  });

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">Projects</h1>
          <p className="text-muted-foreground mt-2">
            Manage projects and their associated repositories.
          </p>
        </div>
        <Button className="gap-2">
          <Plus className="w-4 h-4" />
          Create Project
        </Button>
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        {isLoading ? (
          <div className="col-span-full p-8 text-center text-muted-foreground animate-pulse">Loading projects...</div>
        ) : projects?.map((project: any) => (
          <Card key={project.id} className="bg-white/5 border-white/10 backdrop-blur-sm hover:border-primary/50 transition-colors">
            <CardHeader className="pb-3">
              <div className="flex justify-between items-start">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded bg-primary/20 flex items-center justify-center text-primary">
                    <FolderGit2 className="w-5 h-5" />
                  </div>
                  <div>
                    <CardTitle>{project.name}</CardTitle>
                    <Badge variant={project.status === 'ACTIVE' ? 'default' : 'secondary'} className="mt-1">
                      {project.status}
                    </Badge>
                  </div>
                </div>
              </div>
              <CardDescription className="line-clamp-2 mt-4">
                {project.description || "No description provided."}
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="flex justify-between items-center text-sm border-t border-white/5 pt-4">
                <div className="flex items-center gap-4">
                  <div className="flex items-center gap-1.5 text-muted-foreground">
                    <GitPullRequest className="w-4 h-4" />
                    <span>{project.repositories_count} Repositories</span>
                  </div>
                </div>
                {project.owner_name && (
                  <div className="text-muted-foreground">
                    Owner: {project.owner_name}
                  </div>
                )}
              </div>
            </CardContent>
          </Card>
        ))}
        
        {!isLoading && !projects?.length && (
          <div className="col-span-full p-12 text-center border rounded-lg border-dashed border-white/20 text-muted-foreground">
            No projects found. Create a project to start grouping repositories.
          </div>
        )}
      </div>
    </div>
  );
}