# 🎓 Applied Generative AI - Interactive Demos

Interactive demonstrations of RAG (Retrieval-Augmented Generation) and Ontology-based AI reasoning concepts.

### 🔍 RAG Visual Explorer
*No API key required*

See how Retrieval-Augmented Generation works under the hood:
- **Chunking** — Watch documents split into searchable pieces
- **Embeddings** — See text transform into numerical vectors
- **Vector Space** — Visualize how similar content clusters together
- **Semantic Search** — Compare keyword vs. meaning-based search

### 🧠 Ontology & Counterfactual Reasoning
*OpenAI API key required for AI features (Demo Mode works without)*

Explore structured knowledge and "what if" analysis:
- **Ontology Explorer** — Interactive knowledge graph of cybersecurity risks
- **Counterfactual Analysis** — Test what happens when controls fail
- **LLM Validation** — Verify AI outputs against ground truth
- **Concepts** — Theory explained simply

---

### 🐳 Running the Demos (Docker Required)

| Step | Command |
|:-----|:--------|
| 1. Clone this repo | `git clone https://github.com/dlwhyte/GenAI_foundry.git` |
| 2. Navigate to demos | `cd GenAI_foundry/docker-demos` |
| 3. Build container | `docker build -t mit-genai-demos .` |
| 4. Run demos | `docker run -p 8501:8501 mit-genai-demos` |
| 5. Open browser | [http://localhost:8501](http://localhost:8501) |

📖 **[Detailed Docker Instructions](docs/DOCKER_GUIDE.md)** | 🔑 **[How to Get an OpenAI API Key](docs/openai.md)**

> 💡 **Don't have Docker?** Download it from [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)

---
