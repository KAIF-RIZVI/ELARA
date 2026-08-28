import httpx
import logging
from typing import Optional
from app.core.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()

class LLMClient:
    def __init__(self):
        self.api_key = settings.OPENAI_API_KEY
        self.model = settings.LLM_MODEL
        self.timeout = settings.LLM_TIMEOUT
        
    async def generate_answer(self, system_prompt: str, user_prompt: str) -> str:
        """
        Sends the context-aware prompt to the LLM to generate a grounded answer.
        """
        if not self.api_key:
            logger.error("OpenAI API key is missing.")
            return "LLM integration is currently unconfigured. Missing API key."
            
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.0,  # Deterministic, grounded answers
            "max_tokens": 1024
        }
        
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers=headers,
                    json=payload
                )
                
                if response.status_code != 200:
                    logger.error(f"LLM API returned {response.status_code}: {response.text}")
                    return "Sorry, I am currently unable to reach the reasoning engine."
                    
                data = response.json()
                return data["choices"][0]["message"]["content"]
                
            except httpx.TimeoutException:
                logger.error("LLM API request timed out.")
                return "The reasoning engine took too long to respond. Please try a simpler query."
            except Exception as e:
                logger.error(f"LLM API call failed: {e}")
                return "An unexpected error occurred while generating the answer."

llm_client = LLMClient()
