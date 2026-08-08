"use client";

import { useState, useEffect } from "react";
import { useForm, Controller } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { 
  getProfile, 
  updateProfile, 
  DeveloperProfile 
} from "@/lib/api-client";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { TagInput } from "@/components/ui/tag-input";
import { Loader2, CheckCircle2, XCircle, Clock, Link as LinkIcon, DownloadCloud, Github, Box, Settings, HardDrive, Cpu, Shield, Globe, TerminalSquare } from "lucide-react";

// Helper function for converting arrays to JSONB compatible dicts
const toDict = (arr: string[]) => arr.reduce((acc, val) => ({ ...acc, [val]: true }), {});
const fromDict = (dict?: Record<string, any>) => dict ? Object.keys(dict) : [];

const profileSchema = z.object({
  first_name: z.string().optional(),
  last_name: z.string().optional(),
  display_name: z.string().optional(),
  username: z.string().optional(),
  phone_number: z.string().optional(),
  country: z.string().optional(),
  bio: z.string().optional(),
  location: z.string().optional(),
  timezone: z.string().optional(),
  primary_language: z.string().optional(),
  
  company: z.string().optional(),
  organization: z.string().optional(),
  department: z.string().optional(),
  designation: z.string().optional(),
  primary_role: z.string().optional(),
  experience_years: z.number().min(0).max(50).optional().or(z.nan()),
  employment_type: z.string().optional(),
  current_team: z.string().optional(),
  manager: z.string().optional(),
  
  github_username: z.string().optional(),
  twitter_username: z.string().optional(),
  linkedin_url: z.string().url("Must be a valid URL").optional().or(z.literal("")),
  portfolio_url: z.string().url("Must be a valid URL").optional().or(z.literal("")),
  website: z.string().url("Must be a valid URL").optional().or(z.literal("")),
  
  // Handled by controller/TagInput
  tech_stack: z.array(z.string()).optional(),
  frameworks: z.array(z.string()).optional(),
  databases: z.array(z.string()).optional(),
  cloud_platforms: z.array(z.string()).optional(),
  devops_tools: z.array(z.string()).optional(),
  ai_ml_technologies: z.array(z.string()).optional(),
  operating_systems: z.array(z.string()).optional(),
  version_control: z.array(z.string()).optional(),
  areas_of_expertise: z.array(z.string()).optional(),
});

type ProfileFormValues = z.infer<typeof profileSchema>;

export default function ProfileDashboard() {
  const queryClient = useQueryClient();
  const [isEditing, setIsEditing] = useState(false);

  const { data, isLoading } = useQuery({
    queryKey: ["profile"],
    queryFn: getProfile,
    retry: false,
  });

  const {
    register,
    handleSubmit,
    reset,
    control,
    formState: { errors },
  } = useForm<ProfileFormValues>({
    resolver: zodResolver(profileSchema),
  });

  useEffect(() => {
    if (data?.profile) {
      const p = data.profile;
      reset({
        first_name: p.first_name || "",
        last_name: p.last_name || "",
        display_name: p.display_name || "",
        username: p.username || "",
        phone_number: p.phone_number || "",
        country: p.country || "",
        bio: p.bio || "",
        location: p.location || "",
        timezone: p.timezone || "",
        primary_language: p.primary_language || "",
        
        company: p.company || "",
        organization: p.organization || "",
        department: p.department || "",
        designation: p.designation || "",
        primary_role: p.primary_role || "",
        experience_years: p.experience_years || undefined,
        employment_type: p.employment_type || "",
        current_team: p.current_team || "",
        manager: p.manager || "",
        
        github_username: p.github_username || "",
        twitter_username: p.twitter_username || "",
        linkedin_url: p.linkedin_url || "",
        portfolio_url: p.portfolio_url || "",
        website: p.website || "",
        
        tech_stack: fromDict(p.tech_stack),
        frameworks: fromDict(p.frameworks),
        databases: fromDict(p.databases),
        cloud_platforms: fromDict(p.cloud_platforms),
        devops_tools: fromDict(p.devops_tools),
        ai_ml_technologies: fromDict(p.ai_ml_technologies),
        operating_systems: fromDict(p.operating_systems),
        version_control: fromDict(p.version_control),
        areas_of_expertise: fromDict(p.areas_of_expertise),
      });
    }
  }, [data, reset]);

  const mutation = useMutation({
    mutationFn: async (formData: ProfileFormValues) => {
      const payload: DeveloperProfile = {
        ...formData,
        experience_years: isNaN(formData.experience_years as number) ? undefined : formData.experience_years,
        tech_stack: toDict(formData.tech_stack || []),
        frameworks: toDict(formData.frameworks || []),
        databases: toDict(formData.databases || []),
        cloud_platforms: toDict(formData.cloud_platforms || []),
        devops_tools: toDict(formData.devops_tools || []),
        ai_ml_technologies: toDict(formData.ai_ml_technologies || []),
        operating_systems: toDict(formData.operating_systems || []),
        version_control: toDict(formData.version_control || []),
        areas_of_expertise: toDict(formData.areas_of_expertise || []),
      };
      
      return updateProfile(payload);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["profile"] });
      setIsEditing(false);
    },
  });

  if (isLoading || !data) {
    return (
      <div className="flex h-full items-center justify-center">
        <Loader2 className="h-6 w-6 animate-spin text-muted-foreground" />
      </div>
    );
  }

  const { profile, account, stats, connected_accounts } = data;

  const Field = ({ label, value, name, type = "text" }: { label: string, value: string | number | undefined, name: keyof ProfileFormValues, type?: string }) => {
    if (!isEditing) {
      return (
        <div className="py-2 border-b border-white/5 last:border-0 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-1 sm:gap-4">
          <span className="text-sm font-medium text-muted-foreground w-1/3">{label}</span>
          <span className="text-sm text-foreground flex-1 truncate">{value || <span className="text-muted-foreground/40 italic">Not specified</span>}</span>
        </div>
      );
    }
    return (
      <div className="py-2 flex flex-col gap-1">
        <Label className="text-xs text-muted-foreground">{label}</Label>
        <Input 
          type={type}
          {...register(name, type === "number" ? { valueAsNumber: true } : {})}
          className="bg-black/50 border-white/10 h-8 text-sm" 
          placeholder={label}
        />
        {errors[name] && <span className="text-[10px] text-destructive">{errors[name]?.message as string}</span>}
      </div>
    );
  };

  const TagField = ({ label, name }: { label: string, name: any }) => {
    if (!isEditing) {
      const tags = fromDict((profile as any)[name]);
      return (
        <div className="py-3 border-b border-white/5 last:border-0">
          <span className="text-sm font-medium text-muted-foreground block mb-2">{label}</span>
          {tags.length > 0 ? (
            <div className="flex flex-wrap gap-2">
              {tags.map((t, i) => (
                <span key={i} className="px-2 py-0.5 text-xs font-medium rounded bg-white/5 border border-white/10 text-white">{t}</span>
              ))}
            </div>
          ) : (
             <span className="text-sm text-muted-foreground/40 italic">Not specified</span>
          )}
        </div>
      );
    }
    return (
      <div className="py-2 flex flex-col gap-1">
        <Label className="text-xs text-muted-foreground">{label}</Label>
        <Controller
          name={name}
          control={control}
          render={({ field }) => (
            <TagInput
              placeholder={`Add ${label.toLowerCase()} (press Enter)`}
              tags={field.value || []}
              setTags={field.onChange}
            />
          )}
        />
      </div>
    );
  };

  const ReadOnlyField = ({ label, value }: { label: string, value: any }) => (
    <div className="py-2 border-b border-white/5 last:border-0 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-1 sm:gap-4">
      <span className="text-sm font-medium text-muted-foreground w-1/3">{label}</span>
      <span className="text-sm text-foreground flex-1 truncate">{value || "-"}</span>
    </div>
  );

  return (
    <div className="max-w-6xl mx-auto p-4 sm:p-6 lg:p-8 space-y-8 animate-in fade-in duration-500">
      
      {/* HEADER SECTION */}
      <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4 pb-6 border-b border-white/10">
        <div className="flex items-center gap-4">
          <div className="w-16 h-16 rounded bg-primary/20 flex items-center justify-center text-primary text-2xl font-bold border border-primary/30">
            {profile.display_name?.charAt(0) || account.email.charAt(0).toUpperCase()}
          </div>
          <div>
            <h1 className="text-2xl font-bold text-white leading-tight">
              {profile.display_name || profile.first_name || "Enterprise User"}
            </h1>
            <p className="text-sm text-muted-foreground">
              {profile.designation || "Developer"} at {profile.company || account.workspace_name || "ELARA"}
            </p>
          </div>
        </div>
        <div className="flex items-center gap-4 w-full md:w-auto">
          <div className="flex flex-col items-end hidden md:flex">
            <span className="text-xs text-muted-foreground uppercase tracking-wider mb-1">Completion</span>
            <span className="text-sm font-medium text-white">{profile.profile_completion_percentage || 0}%</span>
          </div>
          <div className="w-full md:w-32 h-1.5 bg-white/10 rounded-full overflow-hidden">
            <div 
              className="h-full bg-primary transition-all duration-1000"
              style={{ width: `${profile.profile_completion_percentage || 0}%` }}
            />
          </div>
          <Button 
            variant={isEditing ? "default" : "secondary"}
            className="w-full md:w-auto"
            onClick={handleSubmit((data) => {
              if (isEditing) {
                onSubmit(data);
              } else {
                setIsEditing(true);
              }
            })}
            disabled={mutation.isPending}
          >
            {mutation.isPending ? <Loader2 className="w-4 h-4 mr-2 animate-spin" /> : null}
            {isEditing ? "Save Profile" : "Edit Profile"}
          </Button>
          {isEditing && (
             <Button variant="ghost" onClick={() => { setIsEditing(false); reset(); }}>Cancel</Button>
          )}
        </div>
      </div>

      <div className="grid grid-cols-1 xl:grid-cols-3 gap-8">
        
        {/* LEFT COLUMN */}
        <div className="xl:col-span-2 space-y-8">
          
          {/* SECTION 1: BASIC INFORMATION */}
          <section>
            <h2 className="text-lg font-semibold text-white mb-4 flex items-center gap-2">
              <Box className="w-4 h-4 text-muted-foreground" /> Basic Information
            </h2>
            <div className="bg-black/20 border border-white/5 rounded-lg p-4 sm:p-6 grid grid-cols-1 md:grid-cols-2 gap-x-8">
              <div className="space-y-0">
                <Field label="First Name" name="first_name" value={profile.first_name} />
                <Field label="Last Name" name="last_name" value={profile.last_name} />
                <Field label="Display Name" name="display_name" value={profile.display_name} />
                <Field label="Username" name="username" value={profile.username} />
              </div>
              <div className="space-y-0">
                <ReadOnlyField label="Email Address" value={account.email} />
                <Field label="Phone Number" name="phone_number" value={profile.phone_number} />
                <Field label="Location" name="location" value={profile.location} />
                <Field label="Country" name="country" value={profile.country} />
              </div>
              <div className="col-span-1 md:col-span-2 mt-4 pt-4 border-t border-white/5">
                {isEditing ? (
                  <div className="space-y-1">
                    <Label className="text-xs text-muted-foreground">Bio</Label>
                    <textarea 
                      {...register("bio")}
                      rows={3}
                      className="flex w-full rounded-md border border-white/10 bg-black/50 px-3 py-2 text-sm placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-primary resize-none"
                    />
                  </div>
                ) : (
                  <div>
                    <span className="text-sm font-medium text-muted-foreground block mb-1">Bio</span>
                    <p className="text-sm text-foreground leading-relaxed">{profile.bio || <span className="text-muted-foreground/40 italic">No bio provided.</span>}</p>
                  </div>
                )}
              </div>
            </div>
          </section>

          {/* SECTION 2: PROFESSIONAL INFORMATION */}
          <section>
            <h2 className="text-lg font-semibold text-white mb-4 flex items-center gap-2">
              <Briefcase className="w-4 h-4 text-muted-foreground" /> Professional Information
            </h2>
            <div className="bg-black/20 border border-white/5 rounded-lg p-4 sm:p-6 grid grid-cols-1 md:grid-cols-2 gap-x-8">
              <div className="space-y-0">
                <Field label="Current Company" name="company" value={profile.company} />
                <Field label="Organization" name="organization" value={profile.organization} />
                <Field label="Department" name="department" value={profile.department} />
                <Field label="Current Team" name="current_team" value={profile.current_team} />
                <Field label="Manager" name="manager" value={profile.manager} />
              </div>
              <div className="space-y-0">
                <Field label="Designation" name="designation" value={profile.designation} />
                <Field label="Primary Role" name="primary_role" value={profile.primary_role} />
                <Field label="Years of Experience" name="experience_years" type="number" value={profile.experience_years} />
                <Field label="Employment Type" name="employment_type" value={profile.employment_type} />
              </div>
            </div>
          </section>

          {/* SECTION 3: TECHNICAL PROFILE */}
          <section>
            <h2 className="text-lg font-semibold text-white mb-4 flex items-center gap-2">
              <TerminalSquare className="w-4 h-4 text-muted-foreground" /> Technical Profile
            </h2>
            <div className="bg-black/20 border border-white/5 rounded-lg p-4 sm:p-6 grid grid-cols-1 md:grid-cols-2 gap-x-8">
              <div className="space-y-0">
                <TagField label="Programming Languages" name="tech_stack" />
                <TagField label="Frameworks" name="frameworks" />
                <TagField label="Databases" name="databases" />
                <TagField label="Cloud Platforms" name="cloud_platforms" />
                <TagField label="DevOps Tools" name="devops_tools" />
              </div>
              <div className="space-y-0">
                <TagField label="AI / ML Technologies" name="ai_ml_technologies" />
                <TagField label="Operating Systems" name="operating_systems" />
                <TagField label="Version Control" name="version_control" />
                <TagField label="Areas of Expertise" name="areas_of_expertise" />
                <TagField label="Skills" name="skills" />
              </div>
            </div>
          </section>

        </div>

        {/* RIGHT COLUMN */}
        <div className="space-y-8">

          {/* SECTION 8: QUICK STATS */}
          <section>
            <h2 className="text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-4 flex items-center gap-2">
              Quick Stats
            </h2>
            <div className="bg-black/20 border border-white/5 rounded-lg divide-y divide-white/5">
              <div className="p-4 flex justify-between items-center">
                <span className="text-sm text-muted-foreground">Repositories Connected</span>
                <span className="text-sm font-medium text-white">{stats.repositories_connected}</span>
              </div>
              <div className="p-4 flex justify-between items-center">
                <span className="text-sm text-muted-foreground">Bugs Assigned</span>
                <span className="text-sm font-medium text-white">{stats.bugs_assigned}</span>
              </div>
              <div className="p-4 flex justify-between items-center">
                <span className="text-sm text-muted-foreground">AI Recs Received</span>
                <span className="text-sm font-medium text-white">{stats.ai_recommendations_received}</span>
              </div>
              <div className="p-4 flex justify-between items-center">
                <span className="text-sm text-muted-foreground">Recent Activity</span>
                <span className="text-sm font-medium text-white">{stats.recent_activity_count}</span>
              </div>
            </div>
          </section>

          {/* SECTION 5: ACCOUNT INFORMATION */}
          <section>
            <h2 className="text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-4 flex items-center gap-2">
               Account Details
            </h2>
            <div className="bg-black/20 border border-white/5 rounded-lg p-4 space-y-0">
              <ReadOnlyField label="User ID" value={<span className="font-mono text-[10px] bg-white/5 px-1 py-0.5 rounded text-muted-foreground truncate max-w-[120px] block">{account.user_id}</span>} />
              <ReadOnlyField label="Account Type" value={account.account_type} />
              <ReadOnlyField label="Auth Method" value={<span className="capitalize">{account.auth_method}</span>} />
              <ReadOnlyField label="Workspace" value={account.workspace_name} />
              <ReadOnlyField label="Role" value={account.workspace_role} />
              <ReadOnlyField label="Plan" value={account.subscription_plan} />
              <ReadOnlyField label="Last Login" value={account.last_login ? new Date(account.last_login).toLocaleDateString() : "Never"} />
              <ReadOnlyField label="Status" value={
                <span className="inline-flex items-center gap-1.5 text-emerald-400 text-xs">
                  <div className="w-1.5 h-1.5 rounded-full bg-emerald-400" /> {account.account_status}
                </span>
              } />
            </div>
          </section>

          {/* SECTION 4: SOCIAL LINKS */}
          <section>
            <h2 className="text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-4 flex items-center gap-2">
               Social & Links
            </h2>
            <div className="bg-black/20 border border-white/5 rounded-lg p-4 space-y-0">
              <Field label="GitHub" name="github_username" value={profile.github_username} />
              <Field label="LinkedIn" name="linkedin_url" value={profile.linkedin_url} />
              <Field label="Twitter/X" name="twitter_username" value={profile.twitter_username} />
              <Field label="Portfolio" name="portfolio_url" value={profile.portfolio_url} />
              <Field label="Website" name="website" value={profile.website} />
            </div>
          </section>

          {/* SECTION 6: CONNECTED ACCOUNTS */}
          <section>
            <h2 className="text-xs font-semibold text-muted-foreground uppercase tracking-wider mb-4 flex items-center gap-2">
               Connected Services
            </h2>
            <div className="bg-black/20 border border-white/5 rounded-lg divide-y divide-white/5">
              <div className="p-4 flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-md bg-white/5 border border-white/10 flex items-center justify-center">
                    <Globe className="w-4 h-4 text-white" />
                  </div>
                  <div>
                    <div className="text-sm font-medium text-white">Google</div>
                    <div className="text-xs text-muted-foreground">{connected_accounts.google_connected ? "Connected" : "Not connected"}</div>
                  </div>
                </div>
                {connected_accounts.google_connected ? (
                  <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                ) : (
                  <Button variant="outline" size="sm" className="h-7 text-xs">Connect</Button>
                )}
              </div>
              
              <div className="p-4 flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-md bg-white/5 border border-white/10 flex items-center justify-center">
                    <Github className="w-4 h-4 text-white" />
                  </div>
                  <div>
                    <div className="text-sm font-medium text-white">GitHub</div>
                    <div className="text-xs text-muted-foreground">{connected_accounts.github_connected ? "Connected" : "Not connected"}</div>
                  </div>
                </div>
                {connected_accounts.github_connected ? (
                  <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                ) : (
                  <Button variant="outline" size="sm" className="h-7 text-xs">Connect</Button>
                )}
              </div>
            </div>
          </section>
          
        </div>
      </div>
    </div>
  );
}