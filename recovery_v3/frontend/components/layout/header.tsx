"use client";

import { Menu, Search, Bell } from "lucide-react";
import { usePathname } from "next/navigation";
import { Button } from "@/components/ui/button";
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb";
import React from "react";

export function Header({ onMenuClick }: { onMenuClick: () => void }) {
  const pathname = usePathname();
  
  // Generate breadcrumbs from pathname
  const segments = pathname.split('/').filter(Boolean);
  
  return (
    <header className="sticky top-0 z-30 flex h-16 shrink-0 items-center gap-x-4 border-b border-white/5 bg-zinc-950/80 backdrop-blur-md px-4 shadow-sm sm:gap-x-6 sm:px-6 lg:px-8">
      <Button
        variant="ghost"
        size="icon"
        className="-m-2.5 p-2.5 text-muted-foreground hover:text-white md:hidden"
        onClick={onMenuClick}
      >
        <span className="sr-only">Open sidebar</span>
        <Menu className="h-6 w-6" aria-hidden="true" />
      </Button>

      {/* Separator for mobile */}
      <div className="h-6 w-px bg-white/10 md:hidden" aria-hidden="true" />

      <div className="flex flex-1 gap-x-4 self-stretch lg:gap-x-6">
        <div className="flex flex-1 items-center">
          {/* Breadcrumbs */}
          <Breadcrumb className="hidden sm:flex">
            <BreadcrumbList>
              {segments.map((segment, index) => {
                const isLast = index === segments.length - 1;
                const path = `/${segments.slice(0, index + 1).join('/')}`;
                const title = segment.charAt(0).toUpperCase() + segment.slice(1);
                
                return (
                  <React.Fragment key={path}>
                    <BreadcrumbItem>
                      {isLast ? (
                        <BreadcrumbPage className="font-medium text-foreground">{title}</BreadcrumbPage>
                      ) : (
                        <BreadcrumbLink href={path} className="text-muted-foreground hover:text-white transition-colors">
                          {title}
                        </BreadcrumbLink>
                      )}
                    </BreadcrumbItem>
                    {!isLast && <BreadcrumbSeparator className="text-muted-foreground/50" />}
                  </React.Fragment>
                );
              })}
            </BreadcrumbList>
          </Breadcrumb>
        </div>
        
        <div className="flex items-center gap-x-4 lg:gap-x-6">
          {/* Global Search (Command Palette Trigger) */}
          <Button variant="outline" className="hidden lg:flex w-64 justify-between bg-black/20 border-white/10 text-muted-foreground hover:text-white hover:bg-white/5">
            <span className="flex items-center">
              <Search className="w-4 h-4 mr-2" />
              Search...
            </span>
            <kbd className="pointer-events-none inline-flex h-5 select-none items-center gap-1 rounded border border-white/20 bg-zinc-900 px-1.5 font-mono text-[10px] font-medium text-muted-foreground">
              <span className="text-xs">⌘</span>K
            </kbd>
          </Button>

          <Button variant="ghost" size="icon" className="text-muted-foreground hover:text-white lg:hidden">
            <Search className="w-5 h-5" />
          </Button>

          <Button variant="ghost" size="icon" className="relative text-muted-foreground hover:text-white">
            <span className="absolute top-2 right-2 w-2 h-2 rounded-full bg-primary" />
            <Bell className="w-5 h-5" />
          </Button>
        </div>
      </div>
    </header>
  );
}
