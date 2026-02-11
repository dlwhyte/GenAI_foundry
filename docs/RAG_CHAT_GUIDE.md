# 🤖 RAG Chat with Estel — How It Works

A deep dive into the architecture and components behind the RAG Chat demo.

---

## What is RAG?

**Retrieval-Augmented Generation (RAG)** is a technique that gives a language model access to your own documents when answering questions. Instead of relying only on what the model learned during training, RAG retrieves relevant passages from your data and includes them in the prompt — grounding the model's response in your content.

This solves two fundamental problems with vanilla LLMs:

1. **Knowledge cutoff** — LLMs don't know about your private documents
2. **Hallucination** — Without context, models may generate plausible but incorrect answers

---

## The RAG Pipeline — Step by Step

Here's what happens when you upload a document and ask a question in Estel:

```
┌──────────────────────────────────────────────────────────────────┐
│                        RAG PIPELINE                              │
│                                                                  │
│  📄 Upload        ✂️ Chunk         🔢 Embed        💾 Store       │
│  ───────── ──→ ────────── ──→ ─────────── ──→ ──────────        │
│  PDF/TXT         Split into      Convert to       Save in        │
│  files           1000-char       numerical         FAISS          │
│                  pieces          vectors           index          │
│                                                                  │
│  ❓ Query         🔍 Retrieve     📝 Augment       💬 Generate    │
│  ───────── ──→ ────────── ──→ ─────────── ──→ ──────────        │
│  User's          Find top        Add chunks       LLM answers    │
│  question        matching        to the           using the      │
│                  chunks          prompt           context         │
└──────────────────────────────────────────────────────────────────┘
```

---

## Component Deep Dive

### 1. Document Loading (`rag_utils.py`)

When you upload files, Estel uses LangChain's document loaders:

- **PDFs** → `PyPDFLoader` — extracts text page by page
- **TXT files** → `TextLoader` — reads the raw text content

Each file becomes a list of `Document` objects containing the text and metadata (page number, source file name).

```python
# Under the hood
loader = PyPDFLoader("uploaded_file.pdf")
docs = loader.load()
# docs = [Document(page_content="...", metadata={page: 0, source: "..."}), ...]
```

### 2. Chunking — `RecursiveCharacterTextSplitter`

Entire documents are too large to send to an LLM. Chunking splits them into smaller, overlapping pieces:

| Parameter | Value | Why |
|-----------|-------|-----|
| `chunk_size` | 1000 characters | Large enough to contain a complete thought |
| `chunk_overlap` | 200 characters | Prevents cutting a sentence in the middle |

**How `RecursiveCharacterTextSplitter` works:**

It tries to split on natural boundaries in this order:
1. Double newlines (`\n\n`) — paragraph breaks
2. Single newlines (`\n`) — line breaks
3. Spaces — word boundaries
4. Characters — last resort

This preserves meaning better than splitting at arbitrary character counts.

```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = text_splitter.split_documents(docs)
```

**Example:** A 5-page PDF might produce 15-25 chunks, each ~1000 characters with 200 characters overlapping between consecutive chunks.

### 3. Embeddings — `text-embedding-ada-002`

Each chunk is converted into a **numerical vector** (a list of 1536 numbers) that captures its semantic meaning. This is done by OpenAI's embedding model.

**Key insight:** Text with similar meaning produces vectors that are close together in vector space, regardless of the exact words used.

| Text | Similar? |
|------|----------|
| "The cat sat on the mat" ↔ "A feline rested on the rug" | ✅ Close vectors |
| "The cat sat on the mat" ↔ "Stock market crashed today" | ❌ Far apart |

```python
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
# Each chunk → [0.0023, -0.0142, 0.0341, ...] (1536 dimensions)
```

### 4. Vector Store — FAISS

**FAISS** (Facebook AI Similarity Search) is an open-source library for fast similarity search over vectors. It stores all chunk embeddings in an optimized index.

**Why FAISS?**
- Extremely fast — searches millions of vectors in milliseconds
- Runs locally — no external database needed
- Simple API — `from_documents()` to create, `as_retriever()` to search
- Persistent — saves to disk, reloads instantly

```python
# Create the index
vectordb = FAISS.from_documents(chunks, embeddings)

# Save to disk
vectordb.save_local("vectorstore_index/")

# Reload later
vectordb = FAISS.load_local("vectorstore_index/", embeddings)
```

**What's on disk:**

```
vectorstore_index/
├── index.faiss    ← The vector index (binary, optimized for search)
└── index.pkl      ← Mapping from vector IDs back to document text
```

### 5. Retrieval — Finding Relevant Chunks

When you ask a question, Estel:
1. Converts your question into a vector (same embedding model)
2. Searches the FAISS index for the most similar chunk vectors
3. Returns the top-k matching chunks (default: 4)

This is **semantic search** — it finds chunks by meaning, not keywords. So asking "What were the company's profits?" would match a chunk containing "Revenue exceeded $10M with net earnings of $2M" even though no words overlap.

```python
retriever = vectordb.as_retriever()
# Internally: embed question → find nearest vectors → return chunks
```

### 6. Augmented Generation — `RetrievalQA` Chain

LangChain's `RetrievalQA` chain ties everything together:

1. **Retrieve** — Get relevant chunks from FAISS
2. **Augment** — Insert chunks into a prompt template as context
3. **Generate** — Send the augmented prompt to `gpt-4o-mini`

```python
prompt_template = """You are a helpful assistant. Use the context below
to answer the user's question.

Context:
{context}

Question: {question}

Answer:"""

chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4o-mini", temperature=0),
    retriever=vectorstore.as_retriever(),
    chain_type="stuff",        # "stuff" = put all chunks in one prompt
    chain_type_kwargs={"prompt": prompt}
)
```

**Chain type "stuff"** means all retrieved chunks are concatenated ("stuffed") into a single prompt. This is simple and works well when retrieved content fits within the context window. Other strategies like "map_reduce" or "refine" handle larger contexts but add complexity.

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                     STREAMLIT UI                         │
│  ┌──────────────┬──────────────┬──────────────────────┐  │
│  │  Upload &    │   Ask        │   Chat                │  │
│  │  Index Tab   │   Estel Tab  │   History Tab         │  │
│  └──────┬───────┴──────┬───────┴──────────────────────┘  │
│         │              │                                  │
│         ▼              ▼                                  │
│  ┌─────────────┐ ┌──────────┐                            │
│  │ rag_utils   │ │chat_utils│                            │
│  │ .py         │ │ .py      │                            │
│  └──────┬──────┘ └────┬─────┘                            │
│         │              │                                  │
│         ▼              ▼                                  │
│  ┌─────────────────────────────────┐                     │
│  │         LangChain                │                     │
│  │  ┌──────────┐  ┌──────────────┐ │                     │
│  │  │TextSplit  │  │RetrievalQA   │ │                     │
│  │  │Embeddings │  │PromptTemplate│ │                     │
│  │  └─────┬─────┘  └──────┬──────┘ │                     │
│  └────────┼────────────────┼────────┘                     │
│           │                │                              │
│           ▼                ▼                              │
│  ┌──────────────┐  ┌──────────────┐                      │
│  │   FAISS      │  │  OpenAI API  │                      │
│  │  (local)     │  │  gpt-4o-mini │                      │
│  └──────────────┘  └──────────────┘                      │
└─────────────────────────────────────────────────────────┘
```

---

## File Structure

```
estel/
├── __init__.py       ← Package exports
├── constants.py      ← Configuration (model names, paths)
├── rag_utils.py      ← Document loading, chunking, FAISS create/load
└── chat_utils.py     ← RetrievalQA chain creation

pages/
└── 3_RAG_Chat.py     ← Streamlit UI with 3 tabs
```

| File | Responsibility |
|------|---------------|
| `constants.py` | Model names (`gpt-4o-mini`, `text-embedding-ada-002`), vector store path |
| `rag_utils.py` | `load_documents()` — parse PDFs/TXT; `create_vectorstore()` — chunk, embed, index; `load_vectorstore()` — reload from disk |
| `chat_utils.py` | `get_chain()` — builds the LangChain RetrievalQA chain with prompt template |
| `3_RAG_Chat.py` | Three-tab Streamlit interface: Upload & Index, Ask Estel, Chat History |

---

## Key Concepts for Students

### Why chunk size matters
- **Too small** (100 chars) — Chunks lack context, retrieval returns fragments
- **Too large** (5000 chars) — Less precise retrieval, wastes context window
- **Sweet spot** (~1000 chars) — Enough context per chunk while maintaining precision

### Why overlap matters
- Without overlap, a key sentence split across two chunks would be lost
- 200-character overlap ensures boundary sentences appear in both chunks

### Temperature = 0
- Estel uses `temperature=0` for deterministic, factual responses
- Higher temperatures would introduce randomness — not ideal for document Q&A

### "Stuff" chain type
- Simplest approach: concatenate all retrieved chunks into one prompt
- Works when total retrieved text fits in the model's context window
- For very large documents, alternatives like `map_reduce` process chunks in batches

### FAISS vs. cloud vector databases
| Feature | FAISS (used here) | Pinecone / Weaviate |
|---------|-------------------|---------------------|
| Cost | Free | Paid (managed service) |
| Setup | `pip install faiss-cpu` | Account + API keys |
| Persistence | Local files | Cloud-hosted |
| Scale | Millions of vectors | Billions |
| Best for | Prototyping, education | Production, multi-user |

---

## Try These Experiments

1. **Upload a PDF and ask questions about it** — Start simple, then ask follow-up questions
2. **Upload two contrasting documents** — Ask about differences between them
3. **Ask a question NOT covered in the document** — See how the model handles it (it should say it doesn't know)
4. **Compare RAG vs. no-RAG** — Ask the same question to ChatGPT without the document context and compare answers

---

## Cost Notes

Each question involves two API calls:
1. **Embedding the question** — ~$0.0001 per query (negligible)
2. **LLM generation** — `gpt-4o-mini` at ~$0.15/1M input tokens + $0.60/1M output tokens

A typical question with 4 retrieved chunks costs roughly **$0.001–0.003** (a fraction of a cent).

Document indexing is a one-time cost per document upload:
- Embedding 50 chunks ≈ $0.001

---

*Part of GenAI Foundry — MIT Professional Education: Applied Generative AI for Digital Transformation*
