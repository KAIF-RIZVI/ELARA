"use client";

import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { api } from '@/lib/api-client';

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
      const listResponse = await api.get('/workspaces');
      const wsInfo = listResponse.data.find((w: any) => w.slug === slug);
      
      if (!wsInfo) {
        throw new Error('Workspace not found');
      }

      // Fetch overview
      const overviewResponse = await api.get(`/workspaces/${wsInfo.id}`);
      setWorkspace(overviewResponse.data);

      // Fetch current member (we can fetch all and find current, or we need a specific endpoint, let's fetch all)
      const membersResponse = await api.get(`/workspaces/${wsInfo.id}/members`);
      // Just mock current member for now until we have me endpoint
      // Actually, we can get current user from a user context if available.
      // Assuming members list is returned, we take the first matching or just store the list.
      // Let's store the first one for now or fetch /users/me
      const meResponse = await api.get('/users/me');
      const me = membersResponse.data.find((m: any) => m.user_id === meResponse.data.id);
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
