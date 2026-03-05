"""
Applied Generative AI — Interactive Demos
Speed of Learning: GenAI Foundry
"""

import streamlit as st
import os

st.set_page_config(
    page_title="GenAI Foundry",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS — matching existing design system
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A5F;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 1.5rem;
    }
    .highlight-box {
        background: linear-gradient(135deg, #f0f4ff 0%, #e8f4fd 100%);
        border-left: 5px solid #1E3A5F;
        padding: 1.5rem;
        border-radius: 0 10px 10px 0;
        margin-bottom: 1.5rem;
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A5F;
        margin: 0;
    }
    .card {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1.2rem;
        height: 100%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        transition: box-shadow 0.2s;
    }
    .card:hover { box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
    .card h4 { color: #1E3A5F; margin-top: 0; }
    .card ul { color: #444; padding-left: 1.2rem; }
    .card li { margin-bottom: 0.3rem; }
    .module-badge {
        display: inline-block;
        background: #1E3A5F;
        color: white;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        padding: 3px 10px;
        border-radius: 20px;
        margin-bottom: 10px;
    }
    .module-badge.danger {
        background: #c0392b;
    }
    .section-divider {
        border: none;
        border-top: 2px solid #e0e0e0;
        margin: 2rem 0 1.5rem 0;
    }
    .section-label {
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: #8b949e;
        margin-bottom: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ── Sidebar API key ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🔑 OpenAI API Key")
    api_key = st.text_input("Enter your API key", type="password", placeholder="sk-...")
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
        st.success("✅ API key set")
    else:
        st.info("💡 Tip: Run with `-e OPENAI_API_KEY=sk-...` or enter key here")

st.markdown("---")
st.caption("Select a demo from the sidebar navigation 👈")

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<p class="main-header">🚀 GenAI Foundry</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Speed of Learning — Interactive Demos</p>', unsafe_allow_html=True)

# ── Key insight box ───────────────────────────────────────────────────────────
st.markdown("""
<div class="highlight-box">
<h3>🗺️ The Learning Journey</h3>
<p style="font-size: 1.3rem; margin-bottom: 0;">
<strong>From raw text to intelligent retrieval — and knowing when to trust it.</strong>
</p>
<p style="margin-top: 0.5rem;">
These demos make abstract GenAI concepts tangible through hands-on exploration.
As you progress through the modules, you'll go from understanding how LLMs work,
to building with them, to critically evaluating their risks.
</p>
</div>
""", unsafe_allow_html=True)

# ── Stats row ─────────────────────────────────────────────────────────────────
st.markdown("### 📊 What's Inside")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: #f0f7ff; border-radius: 10px;">
    <p class="stat-number">4</p>
    <p><strong>Interactive Demos</strong><br/>RAG Explorer, Ontology Reasoning, Document Chat, and Prompt Injection</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: #f0f7ff; border-radius: 10px;">
    <p class="stat-number">6</p>
    <p><strong>Core Concepts</strong><br/>Chunking, Embeddings, Vector Search, Ontologies, RAG Pipeline, AI Safety</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: #f0f7ff; border-radius: 10px;">
    <p class="stat-number">0</p>
    <p><strong>Setup Required</strong><br/>RAG Explorer and Prompt Injection run with no API key — just click and learn</p>
    </div>
    """, unsafe_allow_html=True)

# ── Demo cards — Modules 1–5 ──────────────────────────────────────────────────
st.markdown("---")
st.markdown('<div class="section-label">📚 Modules 1–5 — How GenAI Works</div>', unsafe_allow_html=True)
st.markdown("### 🔍 Explore the Demos")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <span class="module-badge">Modules 1–3</span>
    <h4>🔍 RAG Visual Explorer</h4>
    <ul>
    <li>See how documents are split into chunks</li>
    <li>Watch text transform into embedding vectors</li>
    <li>Visualize semantic clusters in vector space</li>
    <li>Compare keyword vs. meaning-based search</li>
    </ul>
    <p><em>No API key required</em></p>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/1_RAG_Demo.py", label="Open RAG Demo →", icon="🔍")

with col2:
    st.markdown("""
    <div class="card">
    <span class="module-badge">Module 4</span>
    <h4>🧠 Ontology & Counterfactuals</h4>
    <ul>
    <li>Explore interactive cybersecurity knowledge graphs</li>
    <li>Test "what if" scenarios when controls fail</li>
    <li>Verify AI outputs against ground truth</li>
    <li>Understand structured reasoning concepts</li>
    </ul>
    <p><em>API key required for AI features</em></p>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/2_Ontology_Demo.py", label="Open Ontology Demo →", icon="🧠")

with col3:
    st.markdown("""
    <div class="card">
    <span class="module-badge">Module 5</span>
    <h4>🤖 RAG Chat with Estel</h4>
    <ul>
    <li>Upload your own PDF or TXT documents</li>
    <li>Documents are chunked, embedded, and indexed</li>
    <li>Ask questions grounded in your documents</li>
    <li>See RAG in action as a complete pipeline</li>
    </ul>
    <p><em>API key required</em></p>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/3_RAG_Chat.py", label="Open RAG Chat →", icon="🤖")

# ── Module 6 — Devious LLMs ───────────────────────────────────────────────────
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)
st.markdown('<div class="section-label">⚠️ Module 6 — Devious LLMs</div>', unsafe_allow_html=True)
st.markdown("### 🪤 When LLMs Go Wrong")

st.markdown("""
<div class="highlight-box" style="border-left-color: #c0392b; background: linear-gradient(135deg, #fff5f5 0%, #fff0f0 100%);">
<h4 style="color: #c0392b; margin-top: 0;">You understand how LLMs work. Now see how they can be exploited.</h4>
<p>
You've learned how prompts, embeddings, RAG, and agents function.
But what happens when an attacker controls what text the model sees?
Module 6 explores <strong>Devious LLMs</strong> — the ways AI systems can be manipulated,
deceived, or turned against the users they're meant to serve.
</p>
</div>
""", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="card">
    <span class="module-badge danger">Module 6 — New</span>
    <h4>🪤 Prompt Injection Playground</h4>
    <ul>
    <li>Watch hidden instructions hijack AI agents</li>
    <li>Three real-world attack scenarios</li>
    <li>See guardrails block each attack live</li>
    <li>Understand defence principles</li>
    </ul>
    <p><em>No API key required</em></p>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/4_Prompt_Injection.py", label="Open Playground →", icon="🪤")

with col5:
    st.markdown("""
    <div class="card" style="background: #fafafa; border: 1px dashed #ccc;">
    <span class="module-badge" style="background:#aaa;">Module 6 — Coming Soon</span>
    <h4 style="color:#aaa;">🎭 Sycophancy Detector</h4>
    <ul style="color:#aaa;">
    <li>See how models tell users what they want to hear</li>
    <li>Compare neutral vs. leading questions</li>
    <li>Understand confirmation bias in LLMs</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="card" style="background: #fafafa; border: 1px dashed #ccc;">
    <span class="module-badge" style="background:#aaa;">Module 6 — Coming Soon</span>
    <h4 style="color:#aaa;">😴 Sleeper Agent Simulator</h4>
    <ul style="color:#aaa;">
    <li>Explore deceptive alignment concepts</li>
    <li>See how models behave differently in testing vs. production</li>
    <li>Based on Anthropic safety research</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ── Quick start ───────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
### 🚀 Quick Start

```bash
# Clone and run locally
git clone https://github.com/dlwhyte/GenAI_foundry.git
cd GenAI_foundry
pip install -r requirements.txt
streamlit run Home.py
```

Or run with Docker:
```bash
docker build -t genai-foundry .
docker run -p 8501:8501 genai-foundry
```
""")

st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#6c757d; font-size:0.85rem;">
Speed of Learning | GenAI Foundry | MIT Professional Education
</div>
""", unsafe_allow_html=True)
