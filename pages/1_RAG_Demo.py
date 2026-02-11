"""
RAG Visual Explorer - Streamlit Page
Demonstrates chunking, embeddings, and semantic search
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
import re

# Try to import UMAP, fall back to PCA
USE_UMAP = False
try:
    import umap
    USE_UMAP = True
except ImportError:
    pass

# Sample documents
SAMPLE_DOCS = {
    "Cybersecurity Policy": """
Cybersecurity Risk Management Framework

Section 1: Introduction to Risk Assessment
Risk assessment is the cornerstone of any cybersecurity program. Organizations must identify, analyze, and evaluate risks to their information assets. This process involves understanding the threat landscape, identifying vulnerabilities in systems and processes, and determining the potential impact of security incidents. A comprehensive risk assessment enables organizations to prioritize their security investments and allocate resources effectively.

Section 2: Threat Identification
Modern organizations face a diverse array of cyber threats. These include malware attacks such as ransomware and trojans, phishing campaigns targeting employees, insider threats from disgruntled or negligent staff, and advanced persistent threats (APTs) from nation-state actors. Understanding these threats requires continuous monitoring of the threat intelligence landscape and regular updates to threat models.

Section 3: Vulnerability Management
Vulnerability management is an ongoing process of identifying, classifying, remediating, and mitigating security weaknesses. This includes regular vulnerability scanning, penetration testing, and code reviews. Organizations should maintain an inventory of all assets and ensure that patches are applied promptly. The Common Vulnerability Scoring System (CVSS) provides a standardized way to assess vulnerability severity.

Section 4: Incident Response Planning
Every organization needs a well-defined incident response plan. This plan should outline roles and responsibilities, communication protocols, containment strategies, and recovery procedures. Regular tabletop exercises and simulations help ensure that staff are prepared to respond effectively when incidents occur. Post-incident reviews are essential for continuous improvement.

Section 5: Business Continuity
Business continuity planning ensures that critical operations can continue during and after a security incident. This includes maintaining backup systems, establishing recovery time objectives (RTO) and recovery point objectives (RPO), and testing disaster recovery procedures regularly. Cloud-based backup solutions and geographic redundancy are key components of modern continuity strategies.
""",
    "Customer Support FAQ": """
Customer Support Knowledge Base

Returns and Refunds Policy
Customers may return most items within 30 days of purchase for a full refund. Items must be in original condition with all packaging and tags intact. Electronics and software have a 15-day return window. Customized products cannot be returned unless defective. Refunds are processed within 5-7 business days after we receive the returned item.

Shipping Information
Standard shipping takes 5-7 business days within the continental US. Express shipping delivers within 2-3 business days. Overnight shipping is available for orders placed before 2 PM EST. International shipping times vary by destination, typically 10-21 business days. Free shipping is available on orders over $50.

Account Management
To create an account, click the Sign Up button and enter your email address. You can reset your password using the Forgot Password link on the login page. To update your account information, go to Account Settings. To delete your account, contact customer support.

Payment Options
We accept all major credit cards including Visa, Mastercard, and American Express. PayPal and Apple Pay are also supported. Gift cards can be used for full or partial payment. Payment plans are available for orders over $200 through our partnership with Affirm.

Technical Support
For technical issues with our products, first try restarting the device. Check our troubleshooting guides in the Help Center. If the issue persists, contact our technical support team via chat or phone. Our support hours are Monday through Friday, 9 AM to 6 PM EST.
"""
}

# Initialize session state
if 'rag_model' not in st.session_state:
    st.session_state.rag_model = None
if 'rag_chunks' not in st.session_state:
    st.session_state.rag_chunks = []
if 'rag_embeddings' not in st.session_state:
    st.session_state.rag_embeddings = None


@st.cache_resource
def load_model():
    """Load the embedding model (cached)"""
    return SentenceTransformer('all-MiniLM-L6-v2')


def chunk_document(text, chunk_size=400, overlap=50):
    """Split document into overlapping chunks"""
    text = text.strip()
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    chunks = []
    current_chunk = ""
    chunk_id = 0
    
    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= chunk_size:
            current_chunk += sentence + " "
        else:
            if current_chunk:
                chunks.append({
                    'id': chunk_id,
                    'text': current_chunk.strip(),
                    'char_count': len(current_chunk.strip())
                })
                chunk_id += 1
            words = current_chunk.split()
            overlap_text = ' '.join(words[-10:]) if len(words) > 10 else ''
            current_chunk = overlap_text + " " + sentence + " "
    
    if current_chunk.strip():
        chunks.append({
            'id': chunk_id,
            'text': current_chunk.strip(),
            'char_count': len(current_chunk.strip())
        })
    
    return chunks


def semantic_search(query, chunks, embeddings, model, top_k=3):
    """Perform semantic search"""
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    top_indices = np.argsort(similarities)[::-1][:top_k]
    
    results = []
    for idx in top_indices:
        results.append({
            'chunk_id': chunks[idx]['id'],
            'text': chunks[idx]['text'],
            'similarity': similarities[idx]
        })
    
    return results, query_embedding, similarities


def keyword_search(query, chunks):
    """Simple keyword search"""
    query_words = set(query.lower().split())
    scores = []
    for chunk in chunks:
        chunk_words = set(chunk['text'].lower().split())
        matches = len(query_words.intersection(chunk_words))
        scores.append(matches / len(query_words) if query_words else 0)
    return scores


# Page content
st.title("🔍 RAG Visual Explorer")
st.markdown("*Understanding Retrieval-Augmented Generation through interactive visualization*")

# Sidebar
with st.sidebar:
    st.header("📄 Document Settings")
    
    doc_choice = st.selectbox(
        "Select Document",
        ["Cybersecurity Policy", "Customer Support FAQ", "Custom"]
    )
    
    if doc_choice == "Custom":
        custom_doc = st.text_area("Enter your document:", height=150)
        document = custom_doc if custom_doc else SAMPLE_DOCS["Cybersecurity Policy"]
    else:
        document = SAMPLE_DOCS[doc_choice]
    
    chunk_size = st.slider("Chunk Size (chars)", 200, 800, 400, 50)
    
    if st.button("📦 Process Document", type="primary", use_container_width=True):
        with st.spinner("Loading model and processing..."):
            st.session_state.rag_model = load_model()
            st.session_state.rag_chunks = chunk_document(document, chunk_size)
            chunk_texts = [c['text'] for c in st.session_state.rag_chunks]
            st.session_state.rag_embeddings = st.session_state.rag_model.encode(chunk_texts)
        st.success(f"✅ {len(st.session_state.rag_chunks)} chunks created!")

# Main content
if st.session_state.rag_chunks:
    tab1, tab2, tab3, tab4 = st.tabs([
        "📦 Chunks", "🧮 Embeddings", "🗺️ Vector Space", "🔍 Search"
    ])
    
    with tab1:
        st.header("Document Chunks")
        st.markdown("See how the document is split into searchable pieces:")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            for chunk in st.session_state.rag_chunks:
                with st.expander(f"Chunk {chunk['id']} ({chunk['char_count']} chars)"):
                    st.write(chunk['text'])
        
        with col2:
            chunk_df = pd.DataFrame(st.session_state.rag_chunks)
            fig = px.bar(
                chunk_df,
                x='id',
                y='char_count',
                title='Chunk Sizes',
                labels={'id': 'Chunk ID', 'char_count': 'Characters'},
                color='char_count',
                color_continuous_scale='Viridis'
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.header("Embeddings Visualization")
        st.markdown("Each chunk is converted to a 384-dimensional vector:")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Chunks", len(st.session_state.rag_chunks))
        col2.metric("Dimensions", st.session_state.rag_embeddings.shape[1])
        col3.metric("Total Values", st.session_state.rag_embeddings.size)
        
        fig = px.imshow(
            st.session_state.rag_embeddings[:, :50],
            labels=dict(x="Dimension", y="Chunk", color="Value"),
            title="Embedding Heatmap (First 50 Dimensions)",
            color_continuous_scale="RdBu",
            aspect="auto"
        )
        st.plotly_chart(fig, use_container_width=True)
        
        with st.expander("🔢 View Raw Embedding Values"):
            selected_chunk = st.selectbox("Select chunk:", range(len(st.session_state.rag_chunks)))
            st.write(f"First 20 values of Chunk {selected_chunk}'s embedding:")
            st.code(np.round(st.session_state.rag_embeddings[selected_chunk][:20], 4))
    
    with tab3:
        st.header("Vector Space Visualization")
        st.markdown("Chunks projected to 2D — similar content clusters together:")
        
        with st.spinner("Computing projection..."):
            n_neighbors = min(5, len(st.session_state.rag_chunks)-1)
            if USE_UMAP and n_neighbors >= 2:
                reducer = umap.UMAP(n_components=2, random_state=42, n_neighbors=n_neighbors)
            else:
                reducer = PCA(n_components=2, random_state=42)
            embeddings_2d = reducer.fit_transform(st.session_state.rag_embeddings)
        
        viz_df = pd.DataFrame({
            'x': embeddings_2d[:, 0],
            'y': embeddings_2d[:, 1],
            'label': [f"Chunk {c['id']}" for c in st.session_state.rag_chunks],
            'text': [c['text'][:100] + "..." for c in st.session_state.rag_chunks]
        })
        
        fig = px.scatter(
            viz_df,
            x='x', y='y',
            hover_data=['label', 'text'],
            title='Document Chunks in Vector Space',
            color_discrete_sequence=['#636EFA']
        )
        
        for i, row in viz_df.iterrows():
            fig.add_annotation(
                x=row['x'], y=row['y'],
                text=row['label'],
                showarrow=False,
                yshift=10
            )
        
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("💡 **Tip:** Similar chunks cluster together in vector space!")
    
    with tab4:
        st.header("Semantic Search Demo")
        
        query = st.text_input(
            "Enter your search query:",
            placeholder="e.g., How do I respond to a security incident?"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            top_k = st.slider("Number of results:", 1, len(st.session_state.rag_chunks), 3)
        with col2:
            compare_mode = st.checkbox("Compare with keyword search")
        
        if query:
            results, query_emb, similarities = semantic_search(
                query, st.session_state.rag_chunks, st.session_state.rag_embeddings,
                st.session_state.rag_model, top_k
            )
            
            st.subheader("🏆 Top Results")
            for i, result in enumerate(results, 1):
                with st.container():
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.markdown(f"**#{i} - Chunk {result['chunk_id']}**")
                        st.write(result['text'])
                    with col2:
                        st.metric("Similarity", f"{result['similarity']:.4f}")
                    st.divider()
            
            fig = go.Figure()
            colors = ['#EF553B' if i == np.argmax(similarities) else '#636EFA' 
                      for i in range(len(similarities))]
            
            fig.add_trace(go.Bar(
                x=[f"Chunk {i}" for i in range(len(st.session_state.rag_chunks))],
                y=similarities,
                marker_color=colors,
                text=[f"{s:.3f}" for s in similarities],
                textposition='outside'
            ))
            
            fig.update_layout(
                title="Similarity Scores",
                yaxis_range=[0, 1],
                height=350
            )
            st.plotly_chart(fig, use_container_width=True)
            
            if compare_mode:
                st.subheader("📊 Keyword vs Semantic Comparison")
                kw_scores = keyword_search(query, st.session_state.rag_chunks)
                
                fig = make_subplots(rows=1, cols=2, subplot_titles=['Keyword Search', 'Semantic Search'])
                
                chunk_labels = [f"C{i}" for i in range(len(st.session_state.rag_chunks))]
                
                fig.add_trace(
                    go.Bar(x=chunk_labels, y=kw_scores, marker_color='#FFA15A'),
                    row=1, col=1
                )
                fig.add_trace(
                    go.Bar(x=chunk_labels, y=similarities, marker_color='#636EFA'),
                    row=1, col=2
                )
                
                fig.update_layout(height=350, showlegend=False)
                st.plotly_chart(fig, use_container_width=True)
                
                st.info("💡 Notice how semantic search finds relevant content even when exact keywords don't match!")

else:
    st.info("👈 **Click 'Process Document' in the sidebar to begin!**")
    
    st.markdown("""
    ### What you'll learn:
    
    1. **Chunking** — How documents are split into searchable pieces
    2. **Embeddings** — How text becomes numerical vectors
    3. **Vector Space** — Visualizing semantic relationships
    4. **Semantic Search** — Finding content by meaning, not keywords
    """)
