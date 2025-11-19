from models.model_loader import load_local_llm
from src.loader import load_documents
from src.splitter import split_documents
from src.embedder import load_embedder, create_embeddings
from src.vectorstore_handler import build_vectorstore, search
from src.qa_engine import generate_answer
from src.ui import print_header, pretty_answer

def setup():
    docs = load_documents("data/speech.txt")
    chunks = split_documents(docs)
    embedder = load_embedder()
    vectors = create_embeddings(embedder, chunks)
    store = build_vectorstore(chunks, vectors)
    return chunks, embedder, store


def main():
    chunks, embedder, store = setup()
    llm = load_local_llm()

    print_header()

    while True:
        query = input("\nYour question > ")

        if query.lower() == "/exit":
            break

        q_vec = embedder.encode(query)
        result = search(store, q_vec)
        retrieved = result["documents"][0]

        answer = generate_answer(llm, query, retrieved)
        pretty_answer(answer)


if __name__ == "__main__":
    main()
