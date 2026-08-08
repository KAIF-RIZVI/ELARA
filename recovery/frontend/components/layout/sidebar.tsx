"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { 
  LayoutDashboard, 
  GitPullRequest, 
  Bug, 
  Users, 
  Settings,
  LogOut,
  ChevronDown,
  Terminal
} from "lucide-react";
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar";
import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from "@/components/ui/dropdown-menu";
import { Separator } from "@/components/ui/separator";

const navigation = [
  { name: "Overview", href: "/dashboard", icon: LayoutDashboard },
  { name: "Repositories", href: "/dashboard/repos", icon: GitPullRequest },
  { name: "Bug Triage", href: "/dashboard/bugs", icon: Bug },
  { name: "Team", href: "/dashboard/team", icon: Users },
  { name: "Settings", href: "/dashboard/settings", icon: Settings },
];

export function Sidebar({ onClose }: { onClose?: () => void }) {
  const pathname = usePathname();

  return (
    <div className="flex h-full flex-col bg-zinc-950 border-r border-white/5">
      {/* Workspace Switcher */}
      <div className="p-4">
        <DropdownMenu>
          <DropdownMenuTrigger className="flex items-center justify-between w-full p-2 bg-zinc-900/50 hover:bg-zinc-800 rounded-lg border border-white/5 transition-colors group">
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 rounded bg-primary/20 flex items-center justify-center text-primary">
                <Terminal className="w-5 h-5" />
              </div>
              <div className="flex flex-col items-start text-sm">
                <span className="font-medium text-foreground group-hover:text-white transition-colors">Default Workspace</span>
                <span className="text-xs text-muted-foreground">Free Plan</span>
              </div>
            </div>
            <ChevronDown className="w-4 h-4 text-muted-foreground" />
          </DropdownMenuTrigger>
          <DropdownMenuContent className="w-56" align="start">
            <DropdownMenuItem>Settings</DropdownMenuItem>
            <DropdownMenuItem>Create Workspace</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
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
        <DropdownMenu>
          <DropdownMenuTrigger className="flex items-center justify-between w-full p-2 hover:bg-white/5 rounded-lg transition-colors group outline-none">
            <div className="flex items-center gap-3">
              <Avatar className="w-9 h-9 border border-white/10">
                <AvatarImage src="" />
                <AvatarFallback className="bg-primary/20 text-primary font-medium">EU</AvatarFallback>
              </Avatar>
              <div className="flex flex-col items-start text-sm">
                <span className="font-medium text-foreground group-hover:text-white">Enterprise User</span>
                <span className="text-xs text-muted-foreground truncate w-28">user@example.com</span>
              </div>
            </div>
          </DropdownMenuTrigger>
          <DropdownMenuContent className="w-56" align="end" side="top">
            <DropdownMenuItem>Profile Settings</DropdownMenuItem>
            <DropdownMenuItem className="text-destructive focus:text-destructive focus:bg-destructive/10 cursor-pointer">
              <LogOut className="w-4 h-4 mr-2" />
              Log out
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
    </div>
  );
}
