# Project Rules

## Development Server Recovery
Whenever the agent receives a system notice that subagents or background tasks were stopped due to a server restart, OR when the user reports a "localhost refused to connect" error, the agent MUST proactively restart the Next.js frontend (`npm run dev` in `/frontend`) and the FastAPI backend (`uvicorn app.main:app --reload` in `/backend`) without waiting for explicit user instructions to do so.
