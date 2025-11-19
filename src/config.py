from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
SPEECH_PATH = DATA_DIR / "speech.txt"
CHROMA_DIR = ROOT / "chroma_db"
CHUNK_SIZE = 400
CHUNK_OVERLAP = 50
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K = 3
# Local seq2seq model to use via HuggingFace transformers.
# For lower memory, use 'google/flan-t5-small'
FLAN_MODEL = "google/flan-t5-small"
GENERATION_PARAMS = {"max_length": 128, "do_sample": False, "num_beams": 4}
