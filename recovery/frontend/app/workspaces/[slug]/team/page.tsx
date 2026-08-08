"use client";

import { useWorkspace } from "@/contexts/workspace-context";
import { useQuery } from "@tanstack/react-query";
import { fetcher } from "@/lib/api-client";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { UserPlus, Loader2 } from "lucide-react";

export default function WorkspaceTeamPage() {
  const { workspace } = useWorkspace();
  
  const { data: members, isLoading } = useQuery({
    queryKey: ["workspace_members", workspace?.id],
    queryFn: () => fetcher(`/api/v1/workspaces/${workspace?.id}/members`),
    enabled: !!workspace?.id,
  });

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">Team Members</h1>
          <p className="text-muted-foreground mt-2">
            Manage your workspace team members and roles.
          </p>
        </div>
        <Button className="gap-2">
          <UserPlus className="w-4 h-4" />
          Invite Member
        </Button>
      </div>

      <Card className="bg-white/5 border-white/10 backdrop-blur-sm">
        <CardHeader>
          <CardTitle>Members</CardTitle>
          <CardDescription>{members?.length || 0} members in {workspace?.name}</CardDescription>
        </CardHeader>
        <CardContent>
          {isLoading ? (
            <div className="flex justify-center p-8">
              <Loader2 className="w-6 h-6 animate-spin text-muted-foreground" />
            </div>
          ) : (
            <div className="space-y-4">
              {members?.map((member: any) => (
                <div key={member.id} className="flex items-center justify-between p-4 rounded-lg bg-white/5 border border-white/5">
                  <div className="flex items-center gap-4">
                    <Avatar>
                      <AvatarImage src={member.avatar_url || ""} />
                      <AvatarFallback>{member.full_name?.[0] || member.email[0].toUpperCase()}</AvatarFallback>
                    </Avatar>
                    <div>
                      <div className="font-medium">{member.full_name || "Unknown"}</div>
                      <div className="text-sm text-muted-foreground">{member.email}</div>
                    </div>
                  </div>
                  <div className="flex items-center gap-4">
                    <Badge variant={member.role === 'OWNER' ? 'default' : 'secondary'}>
                      {member.role}
                    </Badge>
                    <Badge variant="outline" className={member.status === 'ACTIVE' ? 'text-emerald-500 border-emerald-500/20 bg-emerald-500/10' : ''}>
                      {member.status}
                    </Badge>
                  </div>
                </div>
              ))}
              
              {!members?.length && (
                <div className="text-center p-8 text-muted-foreground">
                  No members found.
                </div>
              )}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
}