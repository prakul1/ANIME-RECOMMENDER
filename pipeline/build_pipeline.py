from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from utils.custom_exceptions import CustomException
from dotenv import load_dotenv
from utils.logger import get_logger

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting build pipeline")

        loader = AnimeDataLoader("/Users/prakuldhiman/Desktop/udemy/ANIME-RECOMMENDER/data/anime_with_synopsis.csv","/Users/prakuldhiman/Desktop/udemy/ANIME-RECOMMENDER/data/anime_updated.csv")
        processed_csv = loader.load_and_process()

        logger.info("data loaded and processed")

        vector_builder=VectorStoreBuilder(processed_csv)
        vector_builder.build_save_vector_store()

        logger.info("vector store built and saved successfully")

        logger.info("Pipeline Built Successfully")
    except Exception as e:
        logger.error(f"Faild to initialize pipeline: {str(e)}")
        raise CustomException("Error during pipeline",e)
    
if __name__ == "__main__":
    main()