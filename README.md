# AmbedkarGPT-Intern
**Kalpit Pvt Ltd — AI Intern (Phase 1) — AmbedkarGPT (Ollama replaced by HuggingFace Flan-T5)**

## Summary
This updated version replaces Ollama/Mistral with a local HuggingFace Seq2Seq model (Flan-T5) so you can run everything using Python libraries and no external LLM servers. It still uses LangChain + ChromaDB + HuggingFaceEmbeddings.

## Key changes
- Replaced Ollama with HuggingFace `transformers` using `google/flan-t5-base` by default.
- The system constructs a prompt that includes retrieved context and runs the Flan-T5 model locally to generate answers.
- No Ollama installation required.

## Model notes
- Default model: `google/flan-t5-base`. This model will be automatically downloaded from the Hugging Face Hub on first run. If you have limited RAM or want faster startup, change to `google/flan-t5-small` in `src/config.py`.
- Running on CPU is supported but may be slower. If you have a CUDA GPU, ensure PyTorch is installed with CUDA support for much faster inference.

## Setup Instructions
1. Extract the ZIP to a folder, for example:
   - Windows: `C:\Users\<you>\Desktop\AmbedkarGPT-Intern-Task-Updated`
   - Linux: `/home/<you>/AmbedkarGPT-Intern-Task-Updated`
2. Create and activate a virtual environment:
   - Windows:
     ```powershell
     python -m venv venv
     venv\Scripts\activate
     ```
   - Linux/macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app from project root (IMPORTANT - run from project root where `src/` is located):
   ```bash
   cd AmbedkarGPT-Intern-Task-Updated
   python -m src.main
   ```

## Commands inside the CLI
- Type any natural-language question about the speech.
- `/help` - show help
- `/preview` - preview stored chunks
- `/reset` - rebuild the vector store
- `/exit` - quit the app

## Sample Questions to Try
- What is the real remedy according to the speech?
- What does the author say is the real enemy?
- Is the problem of caste a problem of social reform?
- Did Ambedkar mention education reforms in this speech? (expected: not found)

## Submission Instructions
1. Create a public GitHub repo named `AmbedkarGPT-Intern-Task` (or use the original name they requested).
2. Push all files: `data/speech.txt`, `src/` folder, `README.md`, `requirements.txt`.
3. Email the repo URL to `kalpiksingh2005@gmail.com` or submit via the portal as instructed.

## Troubleshooting
- If you run out of RAM with the base model, switch to `google/flan-t5-small` in `src/config.py`.
- If Chroma DB errors occur, delete `chroma_db/` and restart to rebuild.
