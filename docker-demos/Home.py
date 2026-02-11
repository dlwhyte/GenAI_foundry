"""
MIT Professional Education - Applied Generative AI for Digital Transformation
Interactive Demos for Module 5

Navigate using the sidebar to explore:
1. RAG Demo - Chunking, embeddings, and semantic search
2. Ontology & Counterfactuals - Structured knowledge and "what if" analysis
"""

import streamlit as st

# Page config
st.set_page_config(
    page_title="Applied GenAI Demos",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Shared API key in sidebar (persists across pages)
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input(
        "OpenAI API Key", 
        type="password", 
        help="Required for Ontology demo's AI reasoning",
        key="openai_api_key"
    )
    if api_key:
        st.success("✅ API key set")
    else:
        st.info("Enter key for AI features")
    
    st.markdown("---")
    st.caption("Select a demo from the navigation above ☝️")

# Main content
st.title("🎓 Applied Generative AI")
st.subheader("Interactive Demos for Digital Transformation")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🔍 RAG Visual Explorer")
    st.markdown("""
    **Understand Retrieval-Augmented Generation**
    
    See how documents are processed for AI search:
    
    - **Chunking** — Split documents into pieces
    - **Embeddings** — Convert text to numbers
    - **Vector Space** — Visualize semantic relationships
    - **Search** — Find by meaning, not keywords
    
    *No API key required for this demo.*
    """)
    st.page_link("pages/1_RAG_Demo.py", label="Open RAG Demo →", icon="🔍")

with col2:
    st.markdown("### 🧠 Ontology & Counterfactuals")
    st.markdown("""
    **Structured Knowledge + "What If" Analysis**
    
    Explore how AI reasons about risk:
    
    - **Ontology** — Concepts and relationships
    - **Counterfactuals** — Test control effectiveness  
    - **Validation** — Verify AI accuracy
    - **Concepts** — Theory explained
    
    *Requires OpenAI API key for AI reasoning.*
    """)
    st.page_link("pages/2_Ontology_Demo.py", label="Open Ontology Demo →", icon="🧠")

st.markdown("---")

# Quick start guide
st.markdown("### 🚀 Quick Start")
st.markdown("""
1. **For RAG Demo:** Just click and explore — no setup needed
2. **For Ontology Demo:** Enter your OpenAI API key in the sidebar first
3. **Navigate:** Use the sidebar menu or the buttons above
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>MIT Professional Education — Applied Generative AI for Digital Transformation</p>
    <p>Module 5: RAG, Ontologies, and Counterfactual Reasoning</p>
</div>
""", unsafe_allow_html=True)
