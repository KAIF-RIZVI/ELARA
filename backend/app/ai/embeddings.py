import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel
import logging

logger = logging.getLogger(__name__)

class EmbeddingService:
    def __init__(self, model_name: str = "microsoft/graphcodebert-base"):
        self.model_name = model_name
        self.dimension = 768
        logger.info(f"Loading tokenizer and model: {model_name}...")
        
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name).to(self.device)
        self.model.eval()
        
        logger.info(f"Model {model_name} loaded successfully on {self.device} with dimension {self.dimension}.")
        
    def _mean_pooling(self, model_output, attention_mask):
        """
        Mask-aware mean pooling for GraphCodeBERT.
        """
        token_embeddings = model_output[0] # First element of model_output contains all token embeddings
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
        
        # Sum embeddings and divide by the number of unmasked tokens
        sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
        sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
        
        return sum_embeddings / sum_mask

    def embed_text(self, text: str) -> list[float]:
        """
        Converts text (bug report or code chunk) into a dense 768-dim vector embedding.
        """
        return self.embed_texts([text])[0]

    def embed_texts(self, texts: list[str]) -> list[list[float]]:
        """
        Converts a list of texts into dense vector embeddings using GraphCodeBERT.
        """
        if not texts:
            return []
            
        # Tokenize sentences
        encoded_input = self.tokenizer(
            texts, 
            padding=True, 
            truncation=True, 
            max_length=512, 
            return_tensors='pt'
        ).to(self.device)

        # Compute token embeddings
        with torch.no_grad():
            model_output = self.model(**encoded_input)

        # Perform mask-aware pooling
        sentence_embeddings = self._mean_pooling(model_output, encoded_input['attention_mask'])

        # Normalize embeddings for COSINE distance
        sentence_embeddings = F.normalize(sentence_embeddings, p=2, dim=1)

        return sentence_embeddings.cpu().tolist()

# Singleton instance
embedding_service = EmbeddingService()