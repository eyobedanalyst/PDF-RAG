# src/build_vectorstore.py
"""
Task 2: Text Chunking, Embedding, and Vector Store Creation

Objective:
Convert Markdown documents into semantically meaningful chunks,
embed them, and store them for fast retrieval.
"""

import os
import re
from pathlib import Path
from typing import List

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document





# ==============================
# Configuration
# ==============================
MARKDOWN_DIR = Path("data/markdown_docs")
VECTORSTORE_DIR = Path("vectorstore")
VECTORSTORE_DIR.mkdir(exist_ok=True)

CHUNK_SIZE = 400
CHUNK_OVERLAP = 80

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


# ==============================
# Helper Functions
# ==============================


def contains_code_block(text: str) -> bool:
    """Check whether a chunk contains a fenced code block."""
    return bool(re.search(r"```[\s\S]*?```", text))




def extract_sections_with_headings(text: str):
    """
    Split markdown into (section_heading, section_text) pairs.
    If no heading exists, section_heading is None.
    """
    sections = re.split(r"(?=^#{1,6}\s)", text, flags=re.MULTILINE)
    results = []


    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue


        lines = sec.splitlines()
        if lines[0].startswith("#"):
            heading = lines[0].lstrip("#").strip()
            body = "\n".join(lines[1:]).strip()
        else:
            heading = None
            body = sec


        results.append((heading, body))


    return results
# ==============================
# Load Markdown Documents
# ==============================
from typing import List


documents: List[Document] = []

for md_file in MARKDOWN_DIR.glob("*.md"):
    loader = TextLoader(str(md_file), encoding="utf-8")
    loaded_docs = loader.load()

    for doc in loaded_docs:
        sections = extract_sections_with_headings(doc.page_content)

        for heading, section_text in sections:
            if not section_text.strip():
                continue

            documents.append(
                Document(
                    page_content=section_text,
                    metadata={
                        "source_file": md_file.name,
                        "section_heading": heading,
                    },
                )
            )

print(f"Loaded {len(documents)} section-level documents")

# ==============================
# Chunking Strategy
# ==============================
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
)

chunked_documents: List[Document] = []
for doc in documents:
    chunks = text_splitter.split_text(doc.page_content)
    for chunk in chunks:
        chunked_documents.append(
            Document(
                page_content=chunk,
                metadata={
                    **doc.metadata,
                    "contains_code": contains_code_block(chunk),
                },
            )
        )

print(f"Created {len(chunked_documents)} chunks")

# ==============================
# Embeddings
# ==============================
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)


# ==============================
# Vector Store (FAISS)
# ==============================
vectorstore = FAISS.from_documents(
documents=chunked_documents,
embedding=embeddings,
)


vectorstore.save_local(str(VECTORSTORE_DIR))


print("Vector store successfully saved to 'vectorstore/'")


# ==============================
# Notes
# ==============================
# The saved vector store contains:
# - Embedded chunks
# - Metadata (source_file, section_heading, contains_code)
# - Original chunk text
# Ready for fast semantic retrieval in a RAG pipeline