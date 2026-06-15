from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.custom_exceptions import CustomException
from utils.logger import get_logger



logging = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self,persis_dir="chroma_db"):
        try:
            logger.info("Initializing Recommendation Pipeline")
            vector_builder=VectorStoreBuilder(csv_path="",persist_dir=persist_dir)

            retriever = VectorStoreBuilder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever,GROQ_API_KEY,MODEL_NAME)

            logger.info("Pipeline Initialized Successfully")
        except Exception as e:
            logger.error(f"Faild to initialize pipeline: {str(e)}")
            raise CustomException("Error during pipeline",e)


    def recommend(self,query:str) -> str:
        try:
            logger.info("Received a query {query}")
            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommendation generated successfully")
            return recommendation
        
        except Exception as e:
            logger.error(f"Faild to get recommendation: {e}")
            raise CustomException("error during recommendation",e)
        


