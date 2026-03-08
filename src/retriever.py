import faiss
import joblib
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index("models/index.faiss")
docs = joblib.load("models/docs.pkl")

def retrieve(query, top_k=5):
    query_vec = model.encode([query]).astype("float32")

    _, idx = index.search(query_vec, top_k)

    results = []
    for i in idx[0]:
        d = docs[i]

        results.append({
            "call_id": d["call_id"],
            "conversation": d["conversation"]
        })

    return results
