import re

def semantic_split_text(text):
    
    sentences = re.split(r'(?<=[.!?]) +', text)
    return sentences


def smart_chunker(sentences, chunk_size=5):
    
    chunks = []
    for i in range(0, len(sentences), chunk_size):
        part = " ".join(sentences[i:i + chunk_size])
        chunks.append(part)
    return chunks


def split_documents(documents):
    text = documents[0]["text"]
    sentences = semantic_split_text(text)
    chunks = smart_chunker(sentences)
    return chunks
