"use client";

import { useWorkspace } from "@/contexts/workspace-context";
import { useQuery } from "@tanstack/react-query";
import { fetcher } from "@/lib/api-client";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Plus, Users } from "lucide-react";

export default function WorkspaceTeamsPage() {
  const { workspace } = useWorkspace();
  
  const { data: teams, isLoading } = useQuery<any[]>({
    queryKey: ["workspace_teams", workspace?.id],
    queryFn: () => fetcher(`/api/v1/workspaces/${workspace?.id}/teams`),
    enabled: !!workspace?.id,
  });

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">Teams</h1>
          <p className="text-muted-foreground mt-2">
            Organize members into functional teams.
          </p>
        </div>
        <Button className="gap-2">
          <Plus className="w-4 h-4" />
          Create Team
        </Button>
      </div>

      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        {isLoading ? (
          <div className="col-span-full p-8 text-center text-muted-foreground animate-pulse">Loading teams...</div>
        ) : teams?.map((team: any) => (
          <Card key={team.id} className="bg-white/5 border-white/10 backdrop-blur-sm hover:border-primary/50 transition-colors">
            <CardHeader className="pb-3">
              <CardTitle>{team.name}</CardTitle>
              <CardDescription className="line-clamp-2 mt-1 h-10">
                {team.description || "No description provided."}
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="flex items-center justify-between text-sm">
                <div className="flex items-center gap-2 text-muted-foreground">
                  <Users className="w-4 h-4" />
                  {team.members_count} members
                </div>
                {team.lead_name && (
                  <div className="text-muted-foreground">
                    Lead: <span className="text-foreground">{team.lead_name}</span>
                  </div>
                )}
              </div>
            </CardContent>
          </Card>
        ))}
        
        {!isLoading && !teams?.length && (
          <div className="col-span-full p-12 text-center border rounded-lg border-dashed border-white/20 text-muted-foreground">
            No teams created yet. Create a team to get started.
          </div>
        )}
      </div>
    </div>
  );
}