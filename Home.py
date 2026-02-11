"""
Applied Generative AI - Interactive Demos
MIT Professional Education: Applied Generative AI for Digital Transformation
"""

import streamlit as st

st.set_page_config(
    page_title="GenAI Foundry",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS — matching AgenticAI Foundry design system
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
        margin-bottom: 2rem;
    }
    .highlight-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .stat-number {
        font-size: 2.5rem;
        font-weight: bold;
        color: #0066cc;
    }
    .card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        border-left: 4px solid #0066cc;
    }
</style>
""", unsafe_allow_html=True)

# API key handling — check env var first, then allow sidebar entry
import os
env_key = os.environ.get("OPENAI_API_KEY", "")

with st.sidebar:
    st.header("⚙️ Configuration")
    if env_key:
        st.success("✅ API key set via environment")
    else:
        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            help="Required for Ontology demo AI features and RAG Chat",
            key="openai_api_key"
        )
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
            st.success("✅ API key set")
        else:
            st.info("💡 Tip: Run with `-e OPENAI_API_KEY=sk-...` or enter key here")

    st.markdown("---")
    st.caption("Select a demo from the sidebar navigation ☝️")

# Header
st.markdown('<p class="main-header">🎓 GenAI Foundry</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Applied Generative AI for Digital Transformation — Interactive Demos</p>', unsafe_allow_html=True)

# Key insight box
st.markdown("""
<div class="highlight-box">
<h3>🎯 The Learning Journey</h3>
<p style="font-size: 1.3rem; margin-bottom: 0;">
<strong>From raw text to intelligent retrieval</strong> — see how chunking, embeddings, ontologies,
and document-grounded chat work under the hood.
</p>
<p style="margin-top: 0.5rem;">
These demos make abstract GenAI concepts tangible through hands-on exploration.
</p>
</div>
""", unsafe_allow_html=True)

# Stats row
st.markdown("### 📊 What's Inside")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: #f0f7ff; border-radius: 10px;">
    <p class="stat-number">3</p>
    <p><strong>Interactive Demos</strong><br/>RAG Explorer, Ontology Reasoning, and Document Chat</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: #f0f7ff; border-radius: 10px;">
    <p class="stat-number">5</p>
    <p><strong>Core Concepts</strong><br/>Chunking, Embeddings, Vector Search, Ontologies, RAG Pipelines</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align: center; padding: 1rem; background: #f0f7ff; border-radius: 10px;">
    <p class="stat-number">0</p>
    <p><strong>Setup Required</strong><br/>RAG Explorer runs with no API key — just click and learn</p>
    </div>
    """, unsafe_allow_html=True)

# Demo cards
st.markdown("---")
st.markdown("### 🧪 Explore the Demos")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
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

# Quick start
st.markdown("---")
st.markdown("### 🚀 Quick Start")
st.info("""
👈 **Select a demo from the sidebar** to begin exploring.

1. **RAG Explorer** — No setup needed, just click and learn
2. **Ontology Demo** — Enter your OpenAI API key in the sidebar first
3. **RAG Chat** — Enter your API key, upload documents, and start chatting
""")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9rem;">
<p>MIT Professional Education: Applied Generative AI for Digital Transformation</p>
<p>Interactive Demo Hub | <a href="https://github.com/dlwhyte/GenAI_foundry" target="_blank">GitHub Repository</a></p>
</div>
""", unsafe_allow_html=True)
