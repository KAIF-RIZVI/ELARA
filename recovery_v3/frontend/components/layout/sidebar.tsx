"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { 
  LayoutDashboard, 
  GitPullRequest, 
  Bug, 
  Users, 
  Settings,
  FolderGit2,
  Users2,
  Terminal,
  Loader2,
  ChevronDown,
  LogOut
} from "lucide-react";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@/components/ui/dropdown-menu";
import { Separator } from "@/components/ui/separator";
import { useQuery } from "@tanstack/react-query";
import { fetcher, User, Workspace } from "@/lib/api-client";

const getNavigation = (basePath: string) => [
  { name: "Overview", href: `${basePath}`, icon: LayoutDashboard },
  { name: "Projects", href: `${basePath}/projects`, icon: FolderGit2 },
  { name: "Repositories", href: `${basePath}/repos`, icon: GitPullRequest },
  { name: "Bug Triage", href: `${basePath}/bugs`, icon: Bug },
  { name: "Members", href: `${basePath}/team`, icon: Users },
  { name: "Teams", href: `${basePath}/teams`, icon: Users2 },
  { name: "Settings", href: `${basePath}/settings`, icon: Settings },
];

export function Sidebar({ onClose, workspaceSlug }: { onClose?: () => void, workspaceSlug?: string }) {
  const pathname = usePathname();

  const { data: user, isLoading: userLoading } = useQuery<User>({
    queryKey: ["user", "me"],
    queryFn: () => fetcher("/api/v1/users/me"),
  });

  const { data: workspaces, isLoading: workspacesLoading } = useQuery<Workspace[]>({
    queryKey: ["workspaces"],
    queryFn: () => fetcher("/api/v1/workspaces"),
  });

  const activeWorkspace = workspaceSlug ? workspaces?.find(w => w.slug === workspaceSlug) : workspaces?.[0];
  
  const basePath = activeWorkspace ? `/workspaces/${activeWorkspace.slug}` : "/dashboard";
  const navigation = getNavigation(basePath);

  return (
    <div className="flex h-full flex-col bg-zinc-950 border-r border-white/5">
      {/* Workspace Switcher */}
      <div className="p-4">
        {workspacesLoading ? (
          <div className="flex items-center justify-center p-4">
            <Loader2 className="w-5 h-5 animate-spin text-muted-foreground" />
          </div>
        ) : (
          <DropdownMenu>
            <DropdownMenuTrigger className="flex items-center justify-between w-full p-2 bg-zinc-900/50 hover:bg-zinc-800 rounded-lg border border-white/5 transition-colors group">
              <div className="flex items-center gap-3">
                <div className="w-8 h-8 rounded bg-primary/20 flex items-center justify-center text-primary">
                  <Terminal className="w-5 h-5" />
                </div>
                <div className="flex flex-col items-start text-sm overflow-hidden">
                  <span className="font-medium text-foreground group-hover:text-white transition-colors truncate max-w-[130px]">
                    {activeWorkspace?.name || "No Workspace"}
                  </span>
                  <span className="text-xs text-muted-foreground truncate w-full">Free Plan</span>
                </div>
              </div>
              <ChevronDown className="w-4 h-4 text-muted-foreground flex-shrink-0" />
            </DropdownMenuTrigger>
            <DropdownMenuContent className="w-56" align="start">
              {workspaces?.map((w) => (
                <Link key={w.id} href={`/workspaces/${w.slug}`}>
                  <DropdownMenuItem className="cursor-pointer">{w.name}</DropdownMenuItem>
                </Link>
              ))}
              <Separator className="my-1" />
              <DropdownMenuItem>Create Workspace</DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        )}
      </div>

      <Separator className="bg-white/5" />

      {/* Navigation Links */}
      <nav className="flex-1 space-y-1 p-4 overflow-y-auto">
        {navigation.map((item) => {
          const isActive = pathname === item.href || pathname.startsWith(item.href + '/');
          const Icon = item.icon;
          
          return (
            <Link
              key={item.name}
              href={item.href}
              onClick={onClose}
              className={`
                group flex items-center gap-3 rounded-md px-3 py-2 text-sm font-medium transition-all
                ${isActive 
                  ? "bg-primary/10 text-primary" 
                  : "text-muted-foreground hover:bg-white/5 hover:text-white"
                }
              `}
            >
              <Icon className={`w-5 h-5 transition-colors ${isActive ? "text-primary" : "text-muted-foreground group-hover:text-white"}`} />
              {item.name}
            </Link>
          );
        })}
      </nav>

      <Separator className="bg-white/5" />

      {/* User Profile Footer */}
      <div className="p-4">
        {userLoading ? (
          <div className="flex items-center justify-center p-4">
            <Loader2 className="w-5 h-5 animate-spin text-muted-foreground" />
          </div>
        ) : (
          <DropdownMenu>
            <DropdownMenuTrigger className="flex items-center justify-between w-full p-2 hover:bg-white/5 rounded-lg transition-colors group outline-none">
              <div className="flex items-center gap-3">
                <Avatar className="w-9 h-9 border border-white/10">
                  <AvatarImage src={user?.avatar_url || ""} alt={user?.full_name || user?.email || "User avatar"} />
                  <AvatarFallback className="bg-primary/20 text-primary font-medium">
                    {user?.full_name?.charAt(0).toUpperCase() || user?.email?.charAt(0).toUpperCase() || "U"}
                  </AvatarFallback>
                </Avatar>
                <div className="flex flex-col items-start text-sm overflow-hidden">
                  <span className="font-medium text-foreground group-hover:text-white truncate max-w-[130px]">
                    {user?.full_name || user?.email?.split('@')[0] || "User"}
                  </span>
                  <span className="text-xs text-muted-foreground truncate w-full">
                    {user?.email || "Unknown"}
                  </span>
                </div>
              </div>
            </DropdownMenuTrigger>
            <DropdownMenuContent className="w-56" align="end" side="top">
              <Link href={`${basePath}/profile`}>
                <DropdownMenuItem className="cursor-pointer">Profile Settings</DropdownMenuItem>
              </Link>
              <DropdownMenuItem className="text-destructive focus:text-destructive focus:bg-destructive/10 cursor-pointer">
                <LogOut className="w-4 h-4 mr-2" />
                Log out
              </DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        )}
      </div>
    </div>
  );
}
