"use client";

import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Terminal, Github, Bot } from "lucide-react";
import { motion } from "framer-motion";

export default function Home() {
  return (
    <main className="min-h-screen flex flex-col items-center justify-center p-8 relative overflow-hidden">
      
      {/* Background Grid Pattern for "Neural Grid" Vibe */}
      <div className="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]"></div>
      
      <div className="absolute left-0 right-0 top-0 -z-10 m-auto h-[310px] w-[310px] rounded-full bg-primary opacity-20 blur-[100px]"></div>

      <motion.div 
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, ease: "easeOut" }}
        className="z-10 flex flex-col items-center gap-6 max-w-2xl text-center"
      >
        <div className="inline-flex items-center justify-center p-3 bg-zinc-900/50 rounded-2xl border border-white/5 ring-1 ring-white/10 shadow-2xl mb-4">
          <Terminal className="w-8 h-8 text-primary" />
        </div>
        
        <h1 className="text-5xl font-bold tracking-tight lg:text-6xl text-balance">
          The Intelligence Layer for <span className="text-primary drop-shadow-[0_0_15px_rgba(139,92,246,0.5)]">Software Teams</span>
        </h1>
        
        <p className="text-lg text-muted-foreground max-w-xl text-balance">
          ELARA connects directly to your repositories, analyzes every line of code, and automatically assigns bugs to the perfect developer.
        </p>

        <Card className="w-full max-w-md mt-8 bg-zinc-950/50 backdrop-blur-xl border-white/10 shadow-2xl">
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Bot className="w-5 h-5 text-primary" />
              Sign in to ELARA
            </CardTitle>
            <CardDescription>
              Enterprise authentication required.
            </CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="email" className="text-left block w-full">Work Email</Label>
              <Input id="email" type="email" placeholder="cto@enterprise.com" className="bg-black/50 border-white/10" />
            </div>
          </CardContent>
          <CardFooter className="flex flex-col gap-3">
            <Button className="w-full bg-primary text-primary-foreground hover:bg-primary/90 font-medium">
              Continue with Email
            </Button>
            <div className="relative w-full text-center text-sm after:absolute after:inset-0 after:top-1/2 after:block after:h-px after:-translate-y-1/2 after:bg-border">
              <span className="relative z-10 bg-zinc-950 px-2 text-muted-foreground">Or</span>
            </div>
            <Button variant="outline" className="w-full border-white/10 bg-transparent hover:bg-white/5">
              <Github className="mr-2 h-4 w-4" />
              Continue with GitHub
            </Button>
          </CardFooter>
        </Card>
      </motion.div>
    </main>
  );
}
