'''from sentence_transformers import SentenceTransformer
import faiss
import joblib

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_index(transcripts):
    texts = []

    for t in transcripts:
        convo = t.get("conversation", [])
        joined_text = " ".join(
            turn.get("text","") for turn in convo
        )
        texts.append(joined_text)

    embeddings = model.encode(texts)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    faiss.write_index(index, "models/index.faiss")
    joblib.dump(transcripts, "models/docs.pkl")

    print("Index built and saved.")'''

import faiss
import joblib
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

docs = joblib.load("models/docs.pkl")

texts = [d["conversation"] for d in docs]
embeddings = model.encode(texts).astype("float32")

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, "models/index.faiss")
print("Index rebuilt:", index.ntotal)
