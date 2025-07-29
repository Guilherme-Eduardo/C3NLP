import os
import sys
from pathlib import Path

from loguru import logger


class Config:
    SEED = 42
    ALLOWED_FILE_EXTENSIONS = {".pdf", ".md", ".txt"}

    class Model:
        NAME = "deepseek-r1:14b"
        TEMPERATURE = 0.6

    class Preprocessing:
        CHUNK_SIZE = 2048
        CHUNK_OVERLAP = 128
        EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"
        RERANKER = "ms-marco-MiniLM-L-12-v2"
        LLM = "llama3"
        CONTEXTUALIZE_CHUNKS = True
        N_SEMANTIC_RESULTS = 5
        N_BM25_RESULTS = 5

    class Chatbot:
        N_CONTEXT_RESULTS = 3

    class Path:
        APP_HOME = Path(os.getenv("APP_HOME", Path(__file__).parent.parent))
        DATA_DIR = APP_HOME / "data"
        
def configure_logging():
    logger.remove()
    logger.add(
        sys.stdout,
        colorize=True,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>",
        level="INFO"
    )
    logger.add(
        Config.Path.LOGS_DIR / "app.log",
        rotation="500 KB",
        retention="7 days",
        level="DEBUG",
        encoding="utf-8"
    )
    logger.info("Logging configured.")
