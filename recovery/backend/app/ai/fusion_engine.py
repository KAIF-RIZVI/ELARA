from app.ai.embeddings import embedding_service
from app.ai.vector_store import vector_store
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.developer import ExpertiseScore, DeveloperProfile
import uuid
import logging

logger = logging.getLogger(__name__)

class HybridFusionEngine:
    def __init__(self):
        # Weights defined in architecture
        self.alpha = 0.4  # Qdrant Cosine Similarity
        self.beta = 0.3   # LLM Confidence
        self.gamma = 0.2  # Developer Expertise
        self.delta = 0.1  # Availability / Workload
        
    async def recommend_developers(self, db: AsyncSession, bug_title: str, bug_description: str, workspace_id: uuid.UUID) -> list[dict]:
        """
        Runs the mathematical fusion engine to rank developers for a specific bug.
        """
        query_text = f"{bug_title}\n{bug_description}"
        
        # 1. Structural Embeddings (Cosine Similarity)
        logger.info("Generating embedding for bug report...")
        bug_vector = embedding_service.embed_text(query_text)
        
        logger.info("Searching Qdrant for similar code chunks...")
        search_results = vector_store.search_similar_code(str(workspace_id), bug_vector, limit=10)
        
        # 2. Extract ownership mapping (Mocked LLM & Git Blame)
        # In a full system, Qdrant payload would contain the `developer_id` who wrote the code
        candidate_scores = {}
        
        result = await db.execute(select(DeveloperProfile))
        developers = result.scalars().all()
        
        for dev in developers:
            # Baseline mock scores to simulate the equation for developers in the DB
            sim_score = 0.85 if len(search_results) > 0 else 0.5
            llm_score = 0.9
            expertise_score = 0.7
            availability_score = 1.0 if dev.open_assignments < 3 else 0.4
            
            # The Fusion Equation
            final_score = (
                (self.alpha * sim_score) + 
                (self.beta * llm_score) + 
                (self.gamma * expertise_score) + 
                (self.delta * availability_score)
            )
            
            candidate_scores[dev.id] = {
                "developer_id": dev.id,
                "github_username": dev.github_username,
                "score": round(final_score, 4),
                "breakdown": {
                    "similarity": sim_score,
                    "llm": llm_score,
                    "expertise": expertise_score,
                    "availability": availability_score
                }
            }
            
        # Sort by final score descending
        ranked = sorted(candidate_scores.values(), key=lambda x: x["score"], reverse=True)
        return ranked

fusion_engine = HybridFusionEngine()