# src/rag_pipeline.py
"""
Task 3: RAG Core Logic (Retrieval + Generation)
Objective:
Retrieve relevant Markdown chunks and generate answers strictly
from the provided context.
"""

import os
from pathlib import Path
from typing import List, Tuple

from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFacePipeline
from langchain.schema import Document
from langchain.prompts import PromptTemplate
from transformers import pipeline

# ==============================
# Configuration
# ==============================
VECTORSTORE_DIR = Path("vectorstore")
TOP_K = 5

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL_NAME = "google/flan-t5-small"  # Streamlit-friendly

# ==============================
# Prompt Template (STRICT RAG)
# ==============================
PROMPT_TEMPLATE = """
You are an educational assistant for web development students.

Your task is to answer questions about Bootstrap 5 using ONLY the information
provided in the Context section below.

Rules:
- Use ONLY the given context.
- Do NOT use outside knowledge.
- Do NOT guess or invent information.
- If the answer is not explicitly found in the context, respond exactly with:
  "I cannot find this information in the provided materials."
- Explain concepts in simple, student-friendly language.
- Use Markdown formatting.
- When code is relevant, include it inside proper code blocks.
- When explaining HTML or Bootstrap classes, clearly describe what each part does.

Context:
{context}

Question:
{question}

Answer:
"""

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=PROMPT_TEMPLATE,
)

# ==============================
# Load Vector Store
# ==============================
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

vectorstore = FAISS.load_local(
    str(VECTORSTORE_DIR),
    embeddings,
    allow_dangerous_deserialization=True,
)

retriever = vectorstore.as_retriever(search_kwargs={"k": TOP_K})

# ==============================
# Load Lightweight LLM
# ==============================
text2text_pipeline = pipeline(
    "text2text-generation",
    model=LLM_MODEL_NAME,
    max_length=512,
)

llm = HuggingFacePipeline(pipeline=text2text_pipeline)

# ==============================
# RAG Answer Function
# ==============================

def answer_question(question: str) -> Tuple[str, List[Document]]:
    """
    Retrieve relevant chunks and generate an answer strictly from context.
    Returns:
        - answer text
        - retrieved source documents
    """
    # LangChain >= 0.1 uses invoke() instead of get_relevant_documents()
    docs = retriever.invoke(question)

    context = "\n\n".join(
        f"Source: {d.metadata.get('source_file')} | Section: {d.metadata.get('section_heading')}\n{d.page_content}"
        for d in docs
    )

    final_prompt = prompt.format(context=context, question=question)
    # LangChain >= 0.1 uses invoke() for LLM calls
    answer = llm.invoke(final_prompt)

    return answer, docs

# ==============================
# Example Usage (Manual Test)
# ==============================
if __name__ == "__main__":
    sample_question = "What does col-md-6 mean in Bootstrap?"
    response, sources = answer_question(sample_question)

    print("Answer:\n", response)
    print("\nRetrieved Sources:")
    for s in sources:
        print("-", s.metadata)
