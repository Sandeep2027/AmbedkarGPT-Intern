import chromadb

def build_vectorstore(chunks, embeddings):
    client = chromadb.Client()
    collection = client.get_or_create_collection("speech_collection")

    for i, (chunk, vec) in enumerate(zip(chunks, embeddings)):
        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[vec.tolist()]
        )

    return collection


def search(collection, query_vec, top_k=3):
    results = collection.query(
        query_embeddings=[query_vec.tolist()],
        n_results=top_k
    )
    return results
