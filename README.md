<h1 align="center"> GenAI Foundry <br>
<img src="images/genai.png" alt="GenAI Badge" width="100">

## 📢 About GenAI Foundry

This repository was created to make the world of Generative AI **accessible, simple, and hands-on**.

Our mission:

- 🚀 Empower learners to experiment with LLMs and RAG pipelines.
- 🧠 Provide clear, beginner-friendly tutorials.
- 📚 Foster creativity and exploration with GenAI tools.

Feel free to **fork**, **adapt**, and **expand** these examples! 🎯

# 📚 Tutorials and Notebooks

Welcome to the GenAI Foundry learning series! Below you'll find a list of hands-on tutorials designed to help you learn about Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and more.

## A Practical Tour of LLM Mechanics (No API Key Required)

| 📓 Notebook | 📝 Description | 🚀 Colab Link |
|:-----------|:---------------|:----------------|
| [1. Tokens and Embeddings](notebooks/tokens_and_embeddings.ipynb) | Introduction to tokens and embeddings. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1gspDc-BuFDn4DtIPw6i7O9qWXATm-IqX#scrollTo=5ehx5CZNQPfu)
| [2. Semantic Similarity](notebooks/semantic_similarity.ipynb) | Introduction to semantic similarity. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1eQthtiit935_SrhbZC3xrhpCyddm90nv#scrollTo=490e2992)
| 3. Search with Embeddings (RAG Foundations) | Embeddings and RAG. | *🚧 Coming Soon* |
| 4. Model and Tradeoffs | Model selection and tradeoffs. | 🚧 Coming Soon |

---

## Inroductory Concepts (OpenAI API Key Required [![Powered by OpenAI](https://img.shields.io/badge/Powered_by-OpenAI-blue?logo=openai)](https://openai.com/))

| 📓 Notebook | 📝 Description | 🚀 Colab Link |
|:-----------|:---------------|:----------------|
| [Simple Chatbot](notebooks/simple_chatbot.ipynb) | Chatbot using an API key. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1k5VtEDxf7fYaeV_-fVezyJMaTvPi8P_q?usp=drive_link) |
| [Temperature and Token Explorer](notebooks/temperature_token.ipynb) | Explore how temperature and tokens affects LLM output. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1nf4tB7OiVDmhc8Ubcjm5D0-TvzBR03M9) |
| [Prompt Engineering Basics](notebooks/prompt_engineering.ipynb) | A gentle introduction to prompt engineering basics. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1jdyIrceJUBdfy5dfP0uw9ticvgh_4nur#scrollTo=Ezt3B02GhU9i) |
| [Few Shot / Zero Shot prompting](notebooks/few_shot_zero_shot.ipynb) | Prompt engineering techniques. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1UsKT57QXtnFffcy5IBmtWYlYZAI_hNCc)
| [Simple RAG Application](notebooks/simple_rag.ipynb) | A gentle introduction to RAG. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/15ylAMZdr8W44pcAOKw2ISOvI5N4gWOt0)
| [LangChain Basics](notebooks/langchain_introduction.ipynb) | A gentle introduction to LangChain capabilities. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1sajbwIQmqgFlbQAzbDuHcMZEDDYpL_kQ#scrollTo=R1oJC7t39iTJ)
| Fine-Tuning Basics | Intro to fine-tuning foundation models. | 🚧 Coming Soon |

---

# 🎓 Applied Generative AI — Interactive Demos

A multi-page Streamlit application with three interactive demos, all running in a single Docker container.

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

### 🤖 RAG Chat with Estel
*OpenAI API key required*

A complete document-grounded chat assistant powered by RAG:

- **Upload** — Load your own PDF or TXT documents
- **Index** — Documents are chunked, embedded, and stored in a FAISS vector database
- **Chat** — Ask questions and get answers grounded in your uploaded content
- **Learn** — See RAG in action as a complete end-to-end pipeline

📖 **[How RAG Chat Works — Deep Dive Guide](docs/RAG_CHAT_GUIDE.md)**

---

### 🐳 Running the Demos (Docker Required)

📖 **[Detailed Docker Guide for Beginners](docs/docker_guide.md)**

| Step | Command |
|:-----|:--------|
| 1. Clone this repo | `git clone https://github.com/dlwhyte/GenAI_foundry.git` |
| 2. Navigate to repo | `cd GenAI_foundry` |
| 3. Build container | `docker build -t genai-foundry .` |
| 4. Run demos | `docker run -p 8501:8501 genai-foundry` |
| 5. Open browser | [http://localhost:8501](http://localhost:8501) |

**With an OpenAI API key** (required for Ontology demo + RAG Chat):

```bash
docker run -p 8501:8501 -e OPENAI_API_KEY=sk-your-key-here genai-foundry
```

> 💡 Without the `-e` flag, you can still enter your API key in the sidebar on any page that requires it.

🔑 **[How to Get an OpenAI API Key](docs/openai.md)**

> 💡 **Don't have Docker?** Download it from [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)

---

# 🛠 How to Get Started

| Action | Description |
|:------|:------------|
| [![GitHub Guide](https://img.shields.io/badge/📖_GitHub-Guide-6A5ACD?style=for-the-badge&logo=github&logoColor=white)](docs/github_guide.md) | ✅ New to GitHub? Start here. |
| [![Docker Guide](https://img.shields.io/badge/🐳_Docker-Guide-2496ED?style=for-the-badge&logo=docker&logoColor=white)](docs/DOCKER_GUIDE.md) | ✅ Learn how to install and use Docker for running demos. |
| [![Open in Google Colab](https://img.shields.io/badge/Open_in-Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=black)](https://colab.research.google.com/github/dlwhyte/GenAI_foundry) | ✅ Open and run the notebooks directly in Google Colab. |
| [![Create OpenAI API Key](https://img.shields.io/badge/Create_OpenAI-API_Key-5A3EBA?style=for-the-badge&logo=openai&logoColor=white)](docs/openai.md) | ✅ Create your OpenAI API key to enable model access. Step-by-step instructions.|

---

## 📝 License

This project is licensed under the **MIT License** — free to use, modify, and share!

See the [LICENSE](LICENSE) file for more details.

---

[![Contact Me](https://img.shields.io/badge/Contact_Me-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dlwhyte/)


---

## 🚀 Ready for the Next Level?

This repo covers the **foundations** of Generative AI — how LLMs work, how to prompt them, and how to build RAG pipelines.

When you're ready to build AI systems that take action in the world, continue to the companion course:

### 👉 [AgenticAI Foundry](https://github.com/dlwhyte/AgenticAI_foundry) — Multi-agent systems, tool use, MCP, and agent security

| GenAI Foundry covers... | AgenticAI Foundry covers... |
|---|---|
| Tokens, embeddings, and how LLMs work | How agents observe, think, and act |
| Prompt engineering and few-shot learning | Multi-agent orchestration with CrewAI |
| RAG pipelines and vector search | Connecting agents to real tools via MCP |
| LangChain basics | Agent security and prompt injection defense |
| _Recommended first_ ✅ | _Take after GenAI Foundry_ ➡️ |
