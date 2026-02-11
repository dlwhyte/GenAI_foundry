"""
Estel RAG Chat Module
=====================

A simple RAG (Retrieval-Augmented Generation) chat assistant.
Upload documents, index them with FAISS, and ask questions
grounded in your own content.

Ported from CyberForge (tidalpoint/cyberforge) for the
GenAI Foundry course hub.
"""

from .rag_utils import load_documents, create_vectorstore, load_vectorstore
from .chat_utils import get_chain
from .constants import PERSIST_DIR, MODEL_NAME, EMBEDDING_MODEL

__all__ = [
    "load_documents",
    "create_vectorstore",
    "load_vectorstore",
    "get_chain",
    "PERSIST_DIR",
    "MODEL_NAME",
    "EMBEDDING_MODEL",
]
