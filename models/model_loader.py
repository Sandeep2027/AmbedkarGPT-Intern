from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

def load_local_llm():
    """
    Loads a lightweight local model for Q&A generation.
    Auto-selects the best model depending on hardware.
    """

    try:
        model_name = "mistralai/Mistral-7B-Instruct-v0.2"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)
        print("[LLM] Loaded Mistral-7B successfully.")
        return pipe
    
    except Exception:
        print("[LLM] Mistral too heavy, switching to FLAN-T5-Base.")
        model_name = "google/flan-t5-base"
        pipe = pipeline("text2text-generation", model=model_name)
        return pipe
