# app.py
"""
Task 4: Streamlit Chat Interface (Web Deployment)
Objective:
Create a public, student-friendly chat interface for the Bootstrap RAG system.
"""

import streamlit as st
from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate

from transformers import pipeline

# ==============================
# Page Configuration
# ==============================
st.set_page_config(
    page_title="Bootstrap 5 Assistant",
    page_icon="📘",
    layout="wide",
)

st.title("📘 Bootstrap 5 Learning Assistant")

# DEBUG: confirm app is rendering
st.write("✅ App loaded successfully")
("📘 Bootstrap 5 Learning Assistant")
st.markdown(
    "Ask questions about **Bootstrap 5**. Answers are generated *only* from the provided course materials."  
)

# ==============================
# Configuration
# ==============================
VECTORSTORE_DIR = Path("vectorstore")
TOP_K = 5

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL_NAME = "google/flan-t5-small"

# ==============================
# Prompt Template
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
# Cached Loaders (Performance)
# ==============================
@st.cache_resource(show_spinner=True)
def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    return FAISS.load_local(
        str(VECTORSTORE_DIR),
        embeddings,
        allow_dangerous_deserialization=True,
    )



from transformers import pipeline

# Cache the pipeline for Streamlit performance
@st.cache_resource(show_spinner=True)
def load_llm():
    # FLAN-T5 small model
    return pipeline(
        task="text2text-generation",
        model="google/flan-t5-small",
        max_length=512,
    )

llm = load_llm()




vectorstore = load_vectorstore()
retriever = vectorstore.as_retriever(search_kwargs={"k": TOP_K})
llm = load_llm()

# ==============================
# Session State
# ==============================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ==============================
# UI Controls
# ==============================
question = st.text_input(
    "Enter your question about Bootstrap 5:",
    placeholder="e.g. What does col-md-6 mean in Bootstrap?"
)


col1, col2 = st.columns([1, 1])
with col1:
    ask_clicked = st.button("Ask")
with col2:
    clear_clicked = st.button("Clear Chat")

if clear_clicked:
    st.session_state.chat_history = []
    question = ""  # reset input
    st.write("Chat cleared! ✅")


# ==============================
# RAG Logic
# ==============================
if ask_clicked and question.strip():
    docs = retriever.invoke(question)

    context = "\n\n".join(
        f"Source: {d.metadata.get('source_file')} | "
        f"Section: {d.metadata.get('section_heading')}\n"
        f"{d.page_content}"
        for d in docs
    )

    final_prompt = prompt.format(context=context, question=question)
    # final_prompt is the full prompt with context + question
    answer = llm(final_prompt)[0]['generated_text']


    st.session_state.chat_history.append(
        {
            "question": question,
            "answer": answer,
            "sources": docs,
        }
    )

# ==============================
# Display Chat
# ==============================
for chat in reversed(st.session_state.chat_history):
    st.markdown("---")
    st.markdown(f"**Question:** {chat['question']}")
    st.markdown("**Answer:**")
    st.markdown(chat["answer"])

    st.markdown("**Sources:**")
    for doc in chat["sources"]:
        st.markdown(
            f"- **{doc.metadata.get('source_file')}**  \n"
            f"  `{doc.page_content[:200]}...`"
        )
