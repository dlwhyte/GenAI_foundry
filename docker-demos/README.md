# 🎓 Applied Generative AI - Interactive Demos

**MIT Professional Education — Applied Generative AI for Digital Transformation**

Interactive demonstrations of RAG (Retrieval-Augmented Generation) and Ontology-based AI reasoning concepts.

---

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

👉 **[See detailed instructions: How to Get an OpenAI API Key](../docs/openai.md)**

Quick summary:
1. Go to [platform.openai.com](https://platform.openai.com/)
2. Sign up or log in
3. Go to API Keys section
4. Create a new key and copy it
5. Add $5-10 in credits (more than enough for this course)

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
3. Contact the course instructor

---

*MIT Professional Education — Applied Generative AI for Digital Transformation*
