"use client";

import { useWorkspace } from "@/contexts/workspace-context";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";

export default function WorkspaceSettingsPage() {
  const { workspace, currentMember } = useWorkspace();

  const isOwner = currentMember?.role === 'OWNER';

  return (
    <div className="space-y-6 max-w-4xl">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">Workspace Settings</h1>
          <p className="text-muted-foreground mt-2">
            Manage your workspace configuration and preferences.
          </p>
        </div>
      </div>

      <Card className="bg-white/5 border-white/10 backdrop-blur-sm">
        <CardHeader>
          <CardTitle>General Information</CardTitle>
          <CardDescription>Basic details about this workspace</CardDescription>
        </CardHeader>
        <CardContent className="space-y-4">
          <div className="space-y-2">
            <label className="text-sm font-medium">Workspace Name</label>
            <Input defaultValue={workspace?.name} disabled={!isOwner} />
          </div>
          
          <div className="space-y-2">
            <label className="text-sm font-medium">Workspace URL Slug</label>
            <Input defaultValue={workspace?.slug} disabled={!isOwner} />
          </div>

          <div className="space-y-2">
            <label className="text-sm font-medium">Description</label>
            <Textarea defaultValue={workspace?.description || ""} disabled={!isOwner} />
          </div>

          {isOwner && (
            <div className="pt-4">
              <Button>Save Changes</Button>
            </div>
          )}
        </CardContent>
      </Card>

      <Card className="bg-white/5 border-red-500/20 backdrop-blur-sm">
        <CardHeader>
          <CardTitle className="text-red-500">Danger Zone</CardTitle>
          <CardDescription>Irreversible and destructive actions</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="flex items-center justify-between p-4 rounded-lg border border-red-500/20 bg-red-500/5">
            <div>
              <div className="font-medium text-white">Archive Workspace</div>
              <div className="text-sm text-muted-foreground mt-1">
                Archiving a workspace prevents all access and suspends billing. It can be restored later by contacting support.
              </div>
            </div>
            <Button variant="destructive" disabled={!isOwner}>
              Archive
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}