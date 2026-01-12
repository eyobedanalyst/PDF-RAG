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
    page_title="Mr Eyobed EPT Learning Assistant",
    page_icon="📘",
    layout="wide",
)

st.title("📘 EPT Learning Assistant")

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

Your task is to answer questions about Bootstrap 5.

Answering rules (VERY IMPORTANT):
1. First, check the provided Context for relevant information.
2. If the Context contains the answer, prioritize and align your answer with it.
3. If the Context does NOT contain sufficient information, you may supplement your answer using reliable general knowledge about Bootstrap 5.
4. Do NOT contradict the Context.
5. Avoid guessing; only provide information you are confident about.
6. If neither the Context nor reliable general knowledge provides a clear answer, respond exactly with:
   "I cannot find this information in the provided materials."

Special instructions for lists, examples, and quizzes:
- If the question asks for a list or examples:
    - Extract all items from the Context if present.
    - If the Context contains a definition but no explicit examples, you may generate a reasonable list of common examples based on that definition.
    - If the Context is insufficient and no definition is present, you may supplement with general knowledge.
    - Present items as a numbered or bullet list.
    - If no examples exist in either, respond: "Not enough information."
- If asked to generate multiple-choice questions (MCQs):
    - Use Context first, then general knowledge if needed.
    - Generate 3 questions.
    - Each question must have 4 options labeled A-D.
    - Only one option is correct.
    - Clearly indicate the correct answer.
    - Structure output clearly as numbered lists or JSON.
    - If the Context is insufficient, rely on general knowledge but stay accurate.
- Optional few-shot example:
    - You may follow this format for guidance:
      Context: "A profession is a vocation requiring specialized knowledge and skills."
      Question: "List some examples of professions."
      Answer:
      - Doctor
      - Engineer
      - Teacher
      - Lawyer

Formatting & style rules:
- Explain concepts in simple, student-friendly language.
- Use Markdown formatting.
- When code is relevant, include it inside proper code blocks.
- When explaining HTML or Bootstrap classes, clearly describe what each part does.
- If the Context is long, only use the most relevant top-k chunks to answer the question.

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
        model="google/flan-t5-base",
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
    "Enter your question about Bootstrap 5 and MODULE 3 of Grade 11:",
    placeholder="e.g. What IS Bootstrap? , what is Profession ?"
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
