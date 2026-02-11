import os
import tempfile
from pathlib import Path
from typing import List

from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_core.documents import Document

from estel.constants import PERSIST_DIR, MODEL_NAME, EMBEDDING_MODEL


def load_documents(uploaded_files) -> List[Document]:
    """Loads and parses uploaded files into LangChain Documents."""
    docs = []
    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = Path(tmp.name)

        try:
            if uploaded_file.name.endswith(".pdf"):
                loader = PyPDFLoader(str(tmp_path))
            else:
                loader = TextLoader(str(tmp_path))
            file_docs = loader.load()
            docs.extend(file_docs)
        except Exception as e:
            print(f"❌ Error loading {uploaded_file.name}: {e}")
        finally:
            tmp_path.unlink(missing_ok=True)

    return docs


def create_vectorstore(documents: List[Document]):
    """Creates and persists a FAISS vectorstore from a list of Documents."""
    if not documents:
        raise ValueError("⚠️ No documents to index. Upload valid files.")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(documents)

    if not splits:
        raise ValueError("No document chunks were created. Please check the uploaded files for content.")

    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    vectordb = FAISS.from_documents(splits, embeddings)
    vectordb.save_local(PERSIST_DIR)
    return vectordb


def load_vectorstore(persist_path: str = PERSIST_DIR):
    """Loads the FAISS vectorstore from disk."""
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    faiss_index_file = Path(persist_path) / "index.faiss"

    if not faiss_index_file.exists():
        raise FileNotFoundError(f"No vectorstore found at {faiss_index_file}. Please upload documents first.")

    return FAISS.load_local(persist_path, embeddings, allow_dangerous_deserialization=True)
