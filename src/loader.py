import os

def load_documents(file_path: str):
    
    if not os.path.exists(file_path):
        raise FileNotFoundError("speech.txt NOT FOUND!")

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    return [{"text": text}]
