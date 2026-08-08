"use client";

import { useState, useEffect } from "react";
import { useForm, Controller } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";
import * as z from "zod";
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { 
  getProfile, 
  updateProfile, 
  disconnectGitHubProfile,
  DeveloperProfile 
} from "@/lib/api-client";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { TagInput } from "@/components/ui/tag-input";
import { Loader2, CheckCircle2, XCircle, Clock, Link as LinkIcon, DownloadCloud, Box, Settings, HardDrive, Cpu, Shield, Globe, TerminalSquare, Briefcase, ExternalLink, RefreshCw, Unlink } from "lucide-react";

// Custom scalable GitHub SVG icon to replace missing Lucide export
const GitHubIcon = ({ className }: { className?: string }) => (
  <svg className={className} viewBox="0 0 24 24" fill="currentColor">
    <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
  </svg>
);

// Helper function for converting arrays to JSONB compatible dicts
const toDict = (arr: string[]) => arr.reduce((acc, val) => ({ ...acc, [val]: true }), {});
const fromDict = (dict?: Record<string, any>) => dict ? Object.keys(dict) : [];

const profileSchema = z.object({
  first_name: z.any().optional(),
  last_name: z.any().optional(),
  display_name: z.any().optional(),
  username: z.any().optional(),
  bio: z.any().optional(),
  location: z.any().optional(),
  timezone: z.any().optional(),
  primary_language: z.any().optional(),
  
  company: z.any().optional(),
  organization: z.any().optional(),
  designation: z.any().optional(),
  primary_role: z.any().optional(),
  experience_years: z.any().optional(),
  
  github_username: z.any().optional(),
  twitter_username: z.any().optional(),
  linkedin_url: z.any().optional(),
  portfolio_url: z.any().optional(),
  website: z.any().optional(),
  
  // Handled by controller/TagInput
  tech_stack: z.any().optional(),
  frameworks: z.any().optional(),
  databases: z.any().optional(),
  cloud_platforms: z.any().optional(),
  devops_tools: z.any().optional(),
  ai_ml_technologies: z.any().optional(),
  areas_of_expertise: z.any().optional(),
  skills: z.any().optional(),
});

type ProfileFormValues = z.infer<typeof profileSchema>;

const COMMON_SUGGESTIONS: Record<string, string[]> = {
  tech_stack: ["JavaScript", "TypeScript", "Python", "Go", "Rust", "Java", "C++", "Ruby", "PHP"],
  frameworks: ["React", "Next.js", "Vue", "Angular", "FastAPI", "Django", "Spring Boot", "Express"],
  databases: ["PostgreSQL", "MySQL", "MongoDB", "Redis", "Elasticsearch", "Cassandra", "DynamoDB"],
  cloud_platforms: ["AWS", "Google Cloud", "Azure", "Vercel", "Heroku", "DigitalOcean", "Cloudflare"],
  devops_tools: ["Docker", "Kubernetes", "GitHub Actions", "GitLab CI", "Terraform", "Ansible", "Jenkins"],
  ai_ml_technologies: ["PyTorch", "TensorFlow", "Scikit-Learn", "Hugging Face", "LangChain", "OpenAI API", "Pandas"],
  areas_of_expertise: ["Frontend", "Backend", "Full Stack", "DevOps", "Machine Learning", "Data Engineering", "Security", "System Design"],
  skills: ["System Architecture", "Leadership", "Agile", "Code Review", "Problem Solving", "CI/CD", "Security", "Testing"],
};

const TIMEZONE_OPTIONS = [
  { label: "UTC (Coordinated Universal Time)", value: "UTC" },
  { label: "(GMT-08:00) Pacific Time (US & Canada)", value: "America/Los_Angeles" },
  { label: "(GMT-07:00) Mountain Time (US & Canada)", value: "America/Denver" },
  { label: "(GMT-06:00) Central Time (US & Canada)", value: "America/Chicago" },
  { label: "(GMT-05:00) Eastern Time (US & Canada)", value: "America/New_York" },
  { label: "(GMT-04:00) Atlantic Time (Canada)", value: "America/Halifax" },
  { label: "(GMT-03:00) Brasilia / Sao Paulo", value: "America/Sao_Paulo" },
  { label: "(GMT+00:00) London / Edinburgh", value: "Europe/London" },
  { label: "(GMT+01:00) Paris / Berlin / Rome", value: "Europe/Paris" },
  { label: "(GMT+01:00) Amsterdam / Stockholm", value: "Europe/Amsterdam" },
  { label: "(GMT+02:00) Cairo / Athens / Helsinki", value: "Europe/Helsinki" },
  { label: "(GMT+02:00) Johannesburg / South Africa", value: "Africa/Johannesburg" },
  { label: "(GMT+03:00) Moscow / Istanbul", value: "Europe/Moscow" },
  { label: "(GMT+04:00) Dubai / Abu Dhabi", value: "Asia/Dubai" },
  { label: "(GMT+05:30) India Standard Time (Kolkata / Mumbai)", value: "Asia/Kolkata" },
  { label: "(GMT+07:00) Bangkok / Hanoi / Jakarta", value: "Asia/Bangkok" },
  { label: "(GMT+08:00) Singapore / Hong Kong / Taipei", value: "Asia/Singapore" },
  { label: "(GMT+08:00) China Standard Time (Beijing / Shanghai)", value: "Asia/Shanghai" },
  { label: "(GMT+09:00) Japan Standard Time (Tokyo)", value: "Asia/Tokyo" },
  { label: "(GMT+09:00) Korea Standard Time (Seoul)", value: "Asia/Seoul" },
  { label: "(GMT+10:00) Australian Eastern Standard Time (Sydney / Melbourne)", value: "Australia/Sydney" },
  { label: "(GMT+12:00) New Zealand Standard Time (Auckland / Wellington)", value: "Pacific/Auckland" },
];

interface FieldProps {
  label: string;
  value?: string | number | null;
  name: keyof ProfileFormValues;
  type?: string;
  options?: { label: string; value: string }[];
  isEditing: boolean;
  register: any;
  errors: any;
}

const Field = ({ label, value, name, type = "text", options, isEditing, register, errors }: FieldProps) => {
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
      {options ? (
        <select
          defaultValue={value ?? ""}
          {...register(name)}
          className="bg-black/50 border border-white/10 rounded-md h-8 px-2.5 text-sm text-foreground focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-primary w-full transition-colors"
        >
          <option value="" className="bg-neutral-900 text-muted-foreground">Select {label}...</option>
          {options.map((opt) => (
            <option key={opt.value} value={opt.value} className="bg-neutral-900 text-foreground">
              {opt.label}
            </option>
          ))}
          {value && !options.some(o => o.value === value) && (
            <option value={value as string} className="bg-neutral-900 text-foreground">{value as string}</option>
          )}
        </select>
      ) : (
        <Input 
          type={type}
          defaultValue={value ?? ""}
          {...register(name, type === "number" ? { valueAsNumber: true } : {})}
          className="bg-black/50 border-white/10 h-8 text-sm" 
          placeholder={label}
        />
      )}
      {errors[name] && <span className="text-[10px] text-destructive">{errors[name]?.message as string}</span>}
    </div>
  );
};

interface TagFieldProps {
  label: string;
  name: string;
  isEditing: boolean;
  profile: any;
  control: any;
}

const TagField = ({ label, name, isEditing, profile, control }: TagFieldProps) => {
  if (!isEditing) {
    const tags = fromDict((profile as any)?.[name]);
    return (
      <div className="py-3 border-b border-white/5 last:border-0">
        <span className="text-sm font-medium text-muted-foreground block mb-2">{label}</span>
        {tags.length > 0 ? (
          <div className="flex flex-wrap gap-2">
            {tags.map((t: string, i: number) => (
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
        name={name as any}
        control={control}
        render={({ field }) => (
          <TagInput
            placeholder={`Add ${label.toLowerCase()} (press Enter)`}
            tags={field.value || []}
            setTags={field.onChange}
            suggestions={COMMON_SUGGESTIONS[name] || []}
          />
        )}
      />
    </div>
  );
};

const ReadOnlyField = ({ label, value }: { label: string, value: any }) => (
  <div className="py-2 border-b border-white/5 last:border-0 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-1 sm:gap-4">
    <span className="text-sm font-medium text-muted-foreground w-1/3">{label}</span>
    <span className="text-sm text-foreground flex-1 truncate">{value}</span>
  </div>
);

export default function ProfileDashboard() {
  const queryClient = useQueryClient();
  const [isEditing, setIsEditing] = useState(false);

  const { data, isLoading, isError, refetch } = useQuery({
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
    shouldUnregister: false,
  });

  useEffect(() => {
    if (data?.profile) {
      const p = data.profile;
      reset({
        first_name: p.first_name || "",
        last_name: p.last_name || "",
        display_name: p.display_name || "",
        username: p.username || "",
        bio: p.bio || "",
        location: p.location || "",
        timezone: p.timezone || "",
        primary_language: p.primary_language || "",
        
        company: p.company || "",
        organization: p.organization || "",
        designation: p.designation || "",
        primary_role: p.primary_role || "",
        experience_years: p.experience_years || undefined,
        
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
        areas_of_expertise: fromDict(p.areas_of_expertise),
        skills: fromDict(p.skills),
      });
    }
  }, [data, reset]);

  const mutation = useMutation({
    mutationFn: async (formData: ProfileFormValues) => {
      const payload: DeveloperProfile = {
        ...formData,
        experience_years: (formData.experience_years === "" || formData.experience_years === undefined || isNaN(Number(formData.experience_years))) ? undefined : Number(formData.experience_years),
        tech_stack: toDict(formData.tech_stack || []),
        frameworks: toDict(formData.frameworks || []),
        databases: toDict(formData.databases || []),
        cloud_platforms: toDict(formData.cloud_platforms || []),
        devops_tools: toDict(formData.devops_tools || []),
        ai_ml_technologies: toDict(formData.ai_ml_technologies || []),
        areas_of_expertise: toDict(formData.areas_of_expertise || []),
        skills: toDict(formData.skills || []),
      };
      
      return updateProfile(payload);
    },
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ["profile"] });
      await refetch();
      setIsEditing(false);
    },
  });

  const disconnectMutation = useMutation({
    mutationFn: disconnectGitHubProfile,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ["profile"] });
      await refetch();
    },
  });

  const connectGitHub = () => {
    window.location.href = "/api/v1/profiles/github/authorize";
  };

  const onSubmit = (formData: ProfileFormValues) => {
    mutation.mutate(formData);
  };

  if (isLoading) {
    return (
      <div className="flex h-full min-h-[400px] items-center justify-center">
        <Loader2 className="h-6 w-6 animate-spin text-muted-foreground" />
      </div>
    );
  }

  if (isError || !data) {
    return (
      <div className="flex flex-col h-full min-h-[400px] items-center justify-center gap-4">
        <XCircle className="h-10 w-10 text-destructive/80" />
        <div className="text-center">
          <h3 className="text-lg font-semibold text-white">Failed to load profile</h3>
          <p className="text-sm text-muted-foreground mt-1">There was an issue communicating with the server.</p>
        </div>
        <Button variant="outline" onClick={() => refetch()} className="mt-2">
          Try Again
        </Button>
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

  const COMMON_SUGGESTIONS: Record<string, string[]> = {
    tech_stack: ["JavaScript", "TypeScript", "Python", "Go", "Rust", "Java", "C++", "Ruby", "PHP"],
    frameworks: ["React", "Next.js", "Vue", "Angular", "FastAPI", "Django", "Spring Boot", "Express"],
    databases: ["PostgreSQL", "MySQL", "MongoDB", "Redis", "Elasticsearch", "Cassandra", "DynamoDB"],
    cloud_platforms: ["AWS", "Google Cloud", "Azure", "Vercel", "Heroku", "DigitalOcean", "Cloudflare"],
    devops_tools: ["Docker", "Kubernetes", "GitHub Actions", "GitLab CI", "Terraform", "Ansible", "Jenkins"],
    ai_ml_technologies: ["PyTorch", "TensorFlow", "Scikit-Learn", "Hugging Face", "LangChain", "OpenAI API", "Pandas"],
    areas_of_expertise: ["Frontend", "Backend", "Full Stack", "DevOps", "Machine Learning", "Data Engineering", "Security", "System Design"],
    skills: ["System Architecture", "Leadership", "Agile", "Code Review", "Problem Solving", "CI/CD", "Security", "Testing"],
  };

  const TagField = ({ label, name }: { label: string, name: keyof typeof COMMON_SUGGESTIONS | any }) => {
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
              suggestions={COMMON_SUGGESTIONS[name] || []}
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
            onClick={() => {
              if (isEditing) {
                handleSubmit(
                  (formData) => {
                    mutation.mutate(formData);
                  },
                  (errors) => {
                    console.error("Validation errors:", errors);
                    alert("Unable to save profile: please review form inputs.");
                  }
                )();
              } else {
                setIsEditing(true);
              }
            }}
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
                <Field label="First Name" name="first_name" value={profile.first_name} isEditing={isEditing} register={register} errors={errors} />
                <Field label="Last Name" name="last_name" value={profile.last_name} isEditing={isEditing} register={register} errors={errors} />
                <Field label="Display Name" name="display_name" value={profile.display_name} isEditing={isEditing} register={register} errors={errors} />
                <Field label="Username" name="username" value={profile.username} isEditing={isEditing} register={register} errors={errors} />
              </div>
              <div className="space-y-0">
                <ReadOnlyField label="Email Address" value={account.email} />
                <Field label="Location" name="location" value={profile.location} isEditing={isEditing} register={register} errors={errors} />
                <Field label="Timezone" name="timezone" options={TIMEZONE_OPTIONS} value={profile.timezone} isEditing={isEditing} register={register} errors={errors} />
                <Field label="Primary Language" name="primary_language" value={profile.primary_language} isEditing={isEditing} register={register} errors={errors} />
              </div>
              <div className="col-span-1 md:col-span-2 mt-4 pt-4 border-t border-white/5">
                {isEditing ? (
                  <div className="space-y-1">
                    <Label className="text-xs text-muted-foreground">Bio</Label>
                    <textarea 
                      defaultValue={profile.bio || ""}
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
                <Field label="Current Company" name="company" value={profile.company} isEditing={isEditing} register={register} errors={errors} />
                <Field label="Organization" name="organization" value={profile.organization} isEditing={isEditing} register={register} errors={errors} />
              </div>
              <div className="space-y-0">
                <Field label="Designation" name="designation" value={profile.designation} isEditing={isEditing} register={register} errors={errors} />
                <Field label="Primary Role" name="primary_role" value={profile.primary_role} isEditing={isEditing} register={register} errors={errors} />
                <Field label="Years of Experience" name="experience_years" type="number" value={profile.experience_years} isEditing={isEditing} register={register} errors={errors} />
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
                <TagField label="Programming Languages" name="tech_stack" isEditing={isEditing} profile={profile} control={control} />
                <TagField label="Frameworks" name="frameworks" isEditing={isEditing} profile={profile} control={control} />
                <TagField label="Databases" name="databases" isEditing={isEditing} profile={profile} control={control} />
                <TagField label="Cloud Platforms" name="cloud_platforms" isEditing={isEditing} profile={profile} control={control} />
                <TagField label="DevOps Tools" name="devops_tools" isEditing={isEditing} profile={profile} control={control} />
              </div>
              <div className="space-y-0">
                <TagField label="AI / ML Technologies" name="ai_ml_technologies" isEditing={isEditing} profile={profile} control={control} />
                <TagField label="Areas of Expertise" name="areas_of_expertise" isEditing={isEditing} profile={profile} control={control} />
                <TagField label="Skills" name="skills" isEditing={isEditing} profile={profile} control={control} />
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
              <Field label="GitHub" name="github_username" value={profile.github_username} isEditing={isEditing} register={register} errors={errors} />
              <Field label="LinkedIn" name="linkedin_url" value={profile.linkedin_url} isEditing={isEditing} register={register} errors={errors} />
              <Field label="Twitter/X" name="twitter_username" value={profile.twitter_username} isEditing={isEditing} register={register} errors={errors} />
              <Field label="Portfolio" name="portfolio_url" value={profile.portfolio_url} isEditing={isEditing} register={register} errors={errors} />
              <Field label="Website" name="website" value={profile.website} isEditing={isEditing} register={register} errors={errors} />
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
              
              <div className="p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-lg bg-white/5 border border-white/10 overflow-hidden flex items-center justify-center shrink-0">
                    {connected_accounts.github_connected && profile.github_avatar_url ? (
                      <img src={profile.github_avatar_url} alt="GitHub Avatar" className="w-full h-full object-cover" />
                    ) : (
                      <GitHubIcon className="w-5 h-5 text-white" />
                    )}
                  </div>
                  <div className="space-y-0.5">
                    <div className="flex items-center gap-2 flex-wrap">
                      <span className="text-sm font-medium text-white">GitHub</span>
                      {connected_accounts.github_connected && profile.github_username && (
                        <span className="text-xs font-mono text-muted-foreground bg-white/5 px-1.5 py-0.2 rounded border border-white/5">
                          @{profile.github_username}
                        </span>
                      )}
                      {connected_accounts.github_connected && typeof profile.github_public_repos === "number" && (
                        <span className="px-2 py-0.5 text-[10px] font-medium rounded-full bg-indigo-500/10 border border-indigo-500/20 text-indigo-300">
                          {profile.github_public_repos} Public Repos
                        </span>
                      )}
                    </div>
                    <div className="flex items-center gap-2 text-xs text-muted-foreground">
                      {connected_accounts.github_connected ? (
                        <span className="text-emerald-400 font-medium flex items-center gap-1">
                          <CheckCircle2 className="w-3.5 h-3.5 inline" /> Connected
                        </span>
                      ) : (
                        <span>Not connected</span>
                      )}
                      {connected_accounts.github_connected && profile.github_profile_url && (
                        <>
                          <span>•</span>
                          <a 
                            href={profile.github_profile_url} 
                            target="_blank" 
                            rel="noopener noreferrer" 
                            className="text-primary hover:underline flex items-center gap-1 font-medium transition-colors"
                          >
                            View Profile <ExternalLink className="w-3 h-3 inline" />
                          </a>
                        </>
                      )}
                    </div>
                  </div>
                </div>
                
                <div className="flex items-center gap-2 shrink-0 self-end sm:self-center">
                  {connected_accounts.github_connected ? (
                    <>
                      <Button 
                        variant="outline" 
                        size="sm" 
                        onClick={connectGitHub} 
                        className="h-8 px-3 text-xs bg-white/5 hover:bg-white/10 border-white/10 text-white flex items-center gap-1.5 transition-all"
                      >
                        <RefreshCw className="w-3 h-3" /> Reconnect
                      </Button>
                      <Button 
                        variant="outline" 
                        size="sm" 
                        onClick={() => disconnectMutation.mutate()} 
                        disabled={disconnectMutation.isPending} 
                        className="h-8 px-3 text-xs border-red-500/20 text-red-400 hover:bg-red-500/10 hover:text-red-300 flex items-center gap-1.5 transition-all"
                      >
                        {disconnectMutation.isPending ? <Loader2 className="w-3 h-3 animate-spin" /> : <Unlink className="w-3 h-3" />} Disconnect
                      </Button>
                    </>
                  ) : (
                    <Button 
                      variant="outline" 
                      size="sm" 
                      onClick={connectGitHub} 
                      className="h-8 px-3 text-xs bg-indigo-600/20 hover:bg-indigo-600/30 border-indigo-500/30 text-indigo-300 hover:text-indigo-200 flex items-center gap-1.5 font-medium shadow-sm transition-all"
                    >
                      <GitHubIcon className="w-3.5 h-3.5 text-indigo-400" /> Connect GitHub
                    </Button>
                  )}
                </div>
              </div>
            </div>
          </section>
          
        </div>
      </div>
    </div>
  );
}