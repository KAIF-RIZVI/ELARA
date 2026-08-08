"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { useQuery } from "@tanstack/react-query";
import { fetcher, Workspace } from "@/lib/api-client";
import { Loader2 } from "lucide-react";

export default function DashboardRedirect() {
  const router = useRouter();
  
  const { data: workspaces, isLoading } = useQuery<Workspace[]>({
    queryKey: ["workspaces"],
    queryFn: () => fetcher("/api/v1/workspaces"),
  });

  useEffect(() => {
    if (!isLoading) {
      if (workspaces && workspaces.length > 0) {
        router.push(`/workspaces/${workspaces[0].slug}`);
      } else {
        // Fallback if no workspace
        console.error("No workspaces found for user.");
      }
    }
  }, [workspaces, isLoading, router]);

  return (
    <div className="flex h-screen w-full items-center justify-center">
      <div className="flex flex-col items-center gap-4">
        <Loader2 className="h-8 w-8 animate-spin text-primary" />
        <p className="text-muted-foreground animate-pulse">Loading your workspace...</p>
      </div>
    </div>
  );
}