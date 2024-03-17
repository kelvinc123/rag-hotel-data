import os
from qdrant_client.http.models import Distance, VectorParams
from qdrant_client import models, QdrantClient
from sentence_transformers import SentenceTransformer
import json

encoder = SentenceTransformer("all-MiniLM-L6-v2")

HOST = os.getenv("QDRANT_HOST")
PORT = os.getenv("QDRANT_PORT")
DB_NAME = os.getenv("QDRANT_DB_NAME")
qdrant = QdrantClient(HOST, port=PORT)
qdrant.recreate_collection(
    collection_name=DB_NAME,
    vectors_config=models.VectorParams(
        size=encoder.get_sentence_embedding_dimension(),  # Vector size is defined by used model
        distance=models.Distance.COSINE,
    ),
)

# Load dataset
with open("documents.json", "r") as f:
    documents = json.load(f)

qdrant.upload_points(
    collection_name=DB_NAME,
    points=[
        models.PointStruct(
            id=idx, vector=encoder.encode(doc["combined_description"]).tolist(), payload=doc
        )
        for idx, doc in enumerate(documents)
    ],
)