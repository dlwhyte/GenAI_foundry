<h1 align="center">
  GenAI Foundry
  <br>
  <img src="images/genai.png" alt="GenAI Badge" width="100">

## 📢 About GenAI Foundry

This repository was created to make the world of Generative AI **accessible, simple, and hands-on**.

Our mission:
- 🚀 Empower learners to experiment with LLMs and RAG pipelines.
- 🧠 Provide clear, beginner-friendly tutorials.
- 📚 Foster creativity and exploration with GenAI tools.

Feel free to **fork**, **adapt**, and **expand** these examples! 🎯

# 📚 Tutorials and Notebooks

Welcome to the GenAI Foundry learning series!   Below you’ll find a list of hands-on tutorials designed to help you learn about Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and more. 



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

 ## 🎓 Applied Generative AI - Interactive Demos

Interactive demonstrations of RAG (Retrieval-Augmented Generation) and Ontology-based AI reasoning concepts.


## 📋 Prerequisites

### Install Docker Desktop

Docker is required to run these demos. Download and install it for your operating system:

| Operating System | Download Link |
|-----------------|---------------|
| **Windows** | [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/) |
| **Mac (Intel)** | [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/) |
| **Mac (Apple Silicon)** | [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/) |
| **Linux** | [Docker Desktop for Linux](https://docs.docker.com/desktop/install/linux-install/) |

After installation, **start Docker Desktop** and wait for it to fully load (you'll see the whale icon in your system tray/menu bar).

### Get an OpenAI API Key (Optional)

The RAG demo works without an API key. The Ontology demo's AI features require one.

1. Go to [platform.openai.com](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to API Keys
4. Create a new key and copy it somewhere safe

---

## 🚀 Quick Start

### Step 1: Download the Code

**Option A — Using Git (recommended):**
```bash
git clone https://github.com/YOUR_USERNAME/mit-genai-demos.git
cd mit-genai-demos
```

**Option B — Download ZIP:**
1. Click the green **Code** button above
2. Select **Download ZIP**
3. Extract the ZIP file
4. Open Terminal/Command Prompt and navigate to the folder:
   ```bash
   cd Downloads/mit-genai-demos-main
   ```

### Step 2: Build the Container

Run this command (takes 2-3 minutes the first time):

```bash
docker build -t mit-genai-demos .
```

You'll see lots of output as it downloads and installs packages. Wait for it to complete.

### Step 3: Run the Demos

```bash
docker run -p 8501:8501 mit-genai-demos
```

You should see output like:
```
You can now view your Streamlit app in your browser.
URL: http://0.0.0.0:8501
```

### Step 4: Open in Your Browser

Go to: **http://localhost:8501**

You'll see the home page with links to both demos.

---

## 🔍 The Demos

### RAG Visual Explorer
*No API key required*

Learn how Retrieval-Augmented Generation works:
- **Chunking** — See how documents are split into pieces
- **Embeddings** — Watch text become numerical vectors
- **Vector Space** — Visualize how similar content clusters together
- **Semantic Search** — Compare keyword vs. meaning-based search

### Ontology & Counterfactual Reasoning
*API key required for AI features (Demo Mode works without)*

Explore structured knowledge and "what if" analysis:
- **Ontology Explorer** — Interactive knowledge graph of cybersecurity risks
- **Counterfactual Analysis** — Test what happens when controls fail
- **LLM Validation** — Verify AI outputs against ground truth
- **Concepts** — Theory explained simply

---

## 🛑 Stopping the Demo

Press `Ctrl+C` in the terminal window where you ran `docker run`.

Or open a new terminal and run:
```bash
docker stop $(docker ps -q --filter ancestor=mit-genai-demos)
```

---

## 🔄 Running Again Later

You only need to build once. After that, just run:

```bash
docker run -p 8501:8501 mit-genai-demos
```

---

## ❓ Troubleshooting

### "Docker command not found"
- Make sure Docker Desktop is installed and running
- On Windows, you may need to restart your computer after installation
- Try opening a new terminal window

### "Port 8501 is already in use"
Another application is using that port. Either:
- Stop the other application, or
- Use a different port: `docker run -p 8502:8501 mit-genai-demos` then go to `localhost:8502`

### "Cannot connect to Docker daemon"
- Make sure Docker Desktop is running (look for the whale icon)
- On Mac/Linux, try: `sudo docker run ...`

### Build fails with memory error
Docker may need more memory. In Docker Desktop:
1. Go to Settings → Resources
2. Increase Memory to at least 4GB
3. Click Apply & Restart

### Page loads but shows errors
- Refresh the page
- If using the Ontology demo, make sure you've entered your API key in the sidebar

### "Model download is slow"
The first time you use the RAG demo, it downloads a ~90MB model. This is normal and only happens once.

---

## 📁 Project Structure

```
mit-genai-demos/
├── Dockerfile           # Container configuration
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── Home.py             # Landing page
└── pages/
    ├── 1_RAG_Demo.py         # RAG demonstration
    └── 2_Ontology_Demo.py    # Ontology & counterfactuals
```

---

## 💡 Tips for Learning

1. **Start with RAG Demo** — It requires no setup and teaches foundational concepts

2. **Try different queries** — In the search tab, experiment with:
   - Exact phrases from the document
   - Synonyms and paraphrases
   - Questions in natural language

3. **Adjust chunk size** — See how smaller/larger chunks affect search results

4. **Use Demo Mode for Validation** — In the Ontology demo's Validation tab, Demo Mode shows pre-built examples with deliberate errors so you can see how validation works

5. **Compare test modes** — Try Standard, Challenge, and Demo modes to see how prompt design affects AI accuracy

---

## 📚 Further Reading

- [What is RAG?](https://docs.anthropic.com/claude/docs/retrieval-augmented-generation)
- [Understanding Embeddings](https://platform.openai.com/docs/guides/embeddings)
- [Ontologies in AI](https://en.wikipedia.org/wiki/Ontology_(information_science))

---

## 🆘 Need Help?

If you encounter issues not covered here, please:
1. Check that Docker Desktop is running
2. Try rebuilding: `docker build --no-cache -t mit-genai-demos .`
3. Contact me

---

*MIT Professional Education — Applied Generative AI for Digital Transformation*
---

# 🛠 How to Get Started

| Action | Description |
|:------|:------------|
| [![Clone or Download Repo](https://img.shields.io/badge/Clone_or_Download-Repo-6A5ACD?style=for-the-badge&logo=github&logoColor=white)](https://github.com/dlwhyte/GenAI_foundry) | ✅ Clone or download this repository to your local machine. |
| [![Open in Google Colab](https://img.shields.io/badge/Open_in-Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=black)](https://colab.research.google.com/github/dlwhyte/GenAI_foundry) | ✅ Open and run the notebooks directly in Google Colab. |
| [![Create OpenAI API Key](https://img.shields.io/badge/Create_OpenAI-API_Key-5A3EBA?style=for-the-badge&logo=openai&logoColor=white)](docs/openai.md) | ✅ Create your OpenAI API key to enable model access. Step-by-step instructions.|

---

## 📝 License

This project is licensed under the **MIT License** — free to use, modify, and share!

See the [LICENSE](LICENSE) file for more details.

---
[![Contact Me](https://img.shields.io/badge/Contact_Me-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dlwhyte/)
