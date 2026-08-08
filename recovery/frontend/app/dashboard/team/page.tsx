"use client";

import { useState } from "react";
import { useQuery } from "@tanstack/react-query";
import { fetcher, Workspace, Member } from "@/lib/api-client";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Loader2, Users, Mail, UserPlus, MoreHorizontal, Shield } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@/components/ui/dropdown-menu";

export default function TeamPage() {
  const { data: workspaces } = useQuery<Workspace[]>({
    queryKey: ["workspaces"],
    queryFn: () => fetcher("/api/v1/workspaces"),
  });
  const activeWorkspaceId = workspaces?.[0]?.id;

  // We mock this query since we haven't built the GET /members endpoint in the backend yet,
  // but this is exactly how it will work when wired up.
  const { data: members, isLoading } = useQuery<Member[]>({
    queryKey: ["workspace", activeWorkspaceId, "members"],
    queryFn: () => fetcher(`/api/v1/workspaces/${activeWorkspaceId}/members`).catch(() => [
      {
        id: "1",
        user_id: "user1",
        role: "OWNER",
        joined_at: new Date().toISOString(),
        user: { email: "admin@elara.dev", name: "Admin User" }
      }
    ]),
    enabled: !!activeWorkspaceId,
  });

  const getRoleBadge = (role: string) => {
    switch (role) {
      case 'OWNER': return 'bg-rose-500/10 text-rose-400 border-rose-500/20';
      case 'ADMIN': return 'bg-orange-500/10 text-orange-400 border-orange-500/20';
      case 'MANAGER': return 'bg-blue-500/10 text-blue-400 border-blue-500/20';
      case 'DEVELOPER': return 'bg-zinc-500/10 text-zinc-400 border-zinc-500/20';
      default: return 'bg-zinc-500/10 text-zinc-400 border-zinc-500/20';
    }
  };

  return (
    <div className="flex flex-col gap-8 pb-8">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold tracking-tight text-white mb-2">Team Directory</h1>
          <p className="text-muted-foreground">Manage workspace access, roles, and developer assignments.</p>
        </div>
        <Button className="bg-primary text-primary-foreground hover:bg-primary/90">
          <UserPlus className="w-4 h-4 mr-2" />
          Invite Member
        </Button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2">
          <Card className="bg-zinc-950/50 border-white/5 backdrop-blur-sm overflow-hidden h-full">
            <CardHeader>
              <CardTitle>Active Members</CardTitle>
              <CardDescription>People with access to this workspace</CardDescription>
            </CardHeader>
            <div className="overflow-x-auto border-t border-white/5">
              <table className="w-full text-sm text-left">
                <tbody className="divide-y divide-white/5">
                  {isLoading ? (
                    <tr>
                      <td className="px-6 py-12 text-center">
                        <Loader2 className="w-6 h-6 animate-spin text-muted-foreground mx-auto" />
                      </td>
                    </tr>
                  ) : !members || members.length === 0 ? (
                    <tr>
                      <td className="px-6 py-16 text-center">
                        <Users className="w-12 h-12 text-zinc-500/30 mx-auto mb-4" />
                        <h3 className="text-lg font-medium text-white mb-1">It's quiet in here</h3>
                        <p className="text-muted-foreground mb-4">Invite your team to start collaborating.</p>
                      </td>
                    </tr>
                  ) : (
                    members.map((member) => (
                      <tr key={member.id} className="bg-transparent hover:bg-white/[0.02] transition-colors">
                        <td className="px-6 py-4">
                          <div className="flex items-center gap-4">
                            <Avatar className="w-10 h-10 border border-white/10">
                              <AvatarFallback className="bg-primary/20 text-primary font-medium">
                                {member.user.email.charAt(0).toUpperCase()}
                              </AvatarFallback>
                            </Avatar>
                            <div>
                              <div className="font-medium text-white">{member.user.name}</div>
                              <div className="text-xs text-muted-foreground flex items-center gap-1 mt-0.5">
                                <Mail className="w-3 h-3" />
                                {member.user.email}
                              </div>
                            </div>
                          </div>
                        </td>
                        <td className="px-6 py-4">
                          <div className={`inline-flex items-center px-2.5 py-1 rounded-full text-[10px] font-bold border ${getRoleBadge(member.role)}`}>
                            {member.role === 'OWNER' && <Shield className="w-3 h-3 mr-1" />}
                            {member.role}
                          </div>
                        </td>
                        <td className="px-6 py-4 text-right">
                          <DropdownMenu>
                            <DropdownMenuTrigger asChild>
                              <Button variant="ghost" size="icon" className="text-muted-foreground hover:text-white hover:bg-white/10">
                                <MoreHorizontal className="w-4 h-4" />
                              </Button>
                            </DropdownMenuTrigger>
                            <DropdownMenuContent align="end" className="w-40 bg-zinc-950 border-white/10">
                              <DropdownMenuItem className="text-white hover:bg-white/10">Change Role</DropdownMenuItem>
                              <DropdownMenuItem className="text-destructive hover:bg-destructive/10">Remove User</DropdownMenuItem>
                            </DropdownMenuContent>
                          </DropdownMenu>
                        </td>
                      </tr>
                    ))
                  )}
                </tbody>
              </table>
            </div>
          </Card>
        </div>

        <div>
          <Card className="bg-primary/5 border-primary/20 h-full">
            <CardHeader>
              <CardTitle className="text-primary">Pending Invites</CardTitle>
              <CardDescription>Awaiting confirmation</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="text-center p-6 border border-dashed border-white/10 rounded-lg bg-zinc-950/50">
                <p className="text-sm font-medium text-white mb-1">No pending invites</p>
                <p className="text-xs text-muted-foreground mb-4">Send an invite link to onboard a new developer.</p>
                <div className="flex gap-2">
                  <Input placeholder="developer@acme.com" className="bg-zinc-900 border-white/10 text-white text-xs h-8" />
                  <Button size="sm" className="h-8 text-xs bg-primary text-primary-foreground hover:bg-primary/90">Send</Button>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}