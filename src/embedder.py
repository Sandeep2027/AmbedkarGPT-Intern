from sentence_transformers import SentenceTransformer
import numpy as np

def load_embedder():
    print("[Embedder] Loading sentence-transformers/all-MiniLM-L6-v2 ...")
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def create_embeddings(embedder, chunks):
    vectors = embedder.encode(chunks)
    return np.array(vectors)
