"use client";

import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { fetcher } from '@/lib/api-client';

export type MemberRole = 'OWNER' | 'ADMIN' | 'MANAGER' | 'DEVELOPER' | 'SUPPORT' | 'VIEWER';

export interface WorkspaceOverview {
  id: string;
  name: string;
  slug: string;
  description: string | null;
  logo_url: string | null;
  status: string;
  settings: Record<string, any>;
  members_count: number;
  projects_count: number;
  repositories_count: number;
  ai_credits_remaining: number;
}

export interface WorkspaceMemberInfo {
  id: string;
  workspace_id: string;
  user_id: string;
  role: MemberRole;
  full_name: string;
  email: string;
  avatar_url: string | null;
}

interface WorkspaceContextType {
  workspace: WorkspaceOverview | null;
  currentMember: WorkspaceMemberInfo | null;
  isLoading: boolean;
  error: string | null;
  refreshWorkspace: () => Promise<void>;
}

const WorkspaceContext = createContext<WorkspaceContextType | undefined>(undefined);

export function WorkspaceProvider({ children, slug }: { children: ReactNode, slug: string }) {
  const [workspace, setWorkspace] = useState<WorkspaceOverview | null>(null);
  const [currentMember, setCurrentMember] = useState<WorkspaceMemberInfo | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const fetchWorkspaceData = async () => {
    setIsLoading(true);
    setError(null);
    try {
      // Find workspace ID by slug from list, or add an endpoint for slug lookup
      // For now, let's assume we can fetch list and find it
      const listResponse = await fetcher<any[]>('/api/v1/workspaces');
      const wsInfo = listResponse.find((w: any) => w.slug === slug);
      
      if (!wsInfo) {
        throw new Error('Workspace not found');
      }

      // Fetch overview
      const overviewResponse = await fetcher<any>(`/api/v1/workspaces/${wsInfo.id}`);
      setWorkspace(overviewResponse);

      // Fetch current member
      const membersResponse = await fetcher<any[]>(`/api/v1/workspaces/${wsInfo.id}/members`);
      const meResponse = await fetcher<any>('/api/v1/users/me');
      const me = membersResponse.find((m: any) => m.user_id === meResponse.id);
      setCurrentMember(me || null);
      
    } catch (err: any) {
      console.error(err);
      setError(err.response?.data?.detail || err.message || 'Failed to load workspace');
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchWorkspaceData();
  }, [slug]);

  return (
    <WorkspaceContext.Provider value={{ workspace, currentMember, isLoading, error, refreshWorkspace: fetchWorkspaceData }}>
      {children}
    </WorkspaceContext.Provider>
  );
}

export function useWorkspace() {
  const context = useContext(WorkspaceContext);
  if (context === undefined) {
    throw new Error('useWorkspace must be used within a WorkspaceProvider');
  }
  return context;
}
