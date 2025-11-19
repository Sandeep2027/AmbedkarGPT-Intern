def build_prompt(question, context):
    return f"""
You are an expert question-answering AI. 
Base your answer STRICTLY on the context below. 
If the answer is not in the context, reply: "I could not find this information in the speech."

Context:
{context}

Question: {question}

Answer:
"""


def generate_answer(llm, question, retrieved_chunks):
    context = "\n\n".join(retrieved_chunks)
    prompt = build_prompt(question, context)
    response = llm(prompt)[0]["generated_text"]
    return response.strip()
