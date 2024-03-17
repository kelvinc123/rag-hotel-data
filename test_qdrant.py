import os
from dotenv import load_dotenv
from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer

load_dotenv()
HOST = os.getenv("QDRANT_HOST")
PORT = os.getenv("QDRANT_PORT")
DB_NAME = os.getenv("QDRANT_DB_NAME")
encoder = SentenceTransformer("all-MiniLM-L6-v2")
qdrant = QdrantClient(HOST, port=PORT)
hits = qdrant.search(
    collection_name=DB_NAME,
    query_vector=encoder.encode("I'm looking for a luxurious hotel with a spa in the city center at San Francisco").tolist(),
    limit=3,
)
for hit in hits:
    print(hit.payload, "score:", hit.score)