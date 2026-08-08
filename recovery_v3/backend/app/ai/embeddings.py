from sentence_transformers import SentenceTransformer
import logging

logger = logging.getLogger(__name__)

class EmbeddingService:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        logger.info(f"Loading SentenceTransformer model: {model_name}...")
        # Using a lightweight model for fast CPU generation
        self.model = SentenceTransformer(model_name)
        logger.info("Model loaded successfully.")
        
    def embed_text(self, text: str) -> list[float]:
        """
        Converts text (bug report or code chunk) into a dense vector embedding.
        """
        # Encode returns a numpy array, we convert to a python list of floats
        vector = self.model.encode(text).tolist()
        return vector

# Singleton instance
embedding_service = EmbeddingService()