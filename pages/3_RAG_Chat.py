"""
RAG Chat with Estel
MIT Professional Education: Applied Generative AI for Digital Transformation

Upload documents and chat with them using RAG.
"""

import streamlit as st
from estel.rag_utils import load_documents, create_vectorstore
from estel.chat_utils import get_chain

# Initialize session state
if "estel_chat_history" not in st.session_state:
    st.session_state.estel_chat_history = []

if "estel_chain" not in st.session_state:
    st.session_state.estel_chain = None

# API key handling — check env var first, then allow sidebar entry
import os
env_key = os.environ.get("OPENAI_API_KEY", "")

with st.sidebar:
    st.header("⚙️ Configuration")
    if env_key:
        api_key = env_key
        st.success("✅ API key set via environment")
    else:
        api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            help="Required for RAG Chat with Estel",
            key="openai_api_key"
        )
        if api_key:
            os.environ["OPENAI_API_KEY"] = api_key
            st.success("✅ API key set")
        else:
            st.info("💡 Tip: Run with `-e OPENAI_API_KEY=sk-...` or enter key here")

# Page header
st.title("🤖 RAG Chat with Estel")
st.markdown("Upload your documents, then ask Estel questions grounded in your content.")

if not api_key:
    st.warning("⚠️ Please enter your OpenAI API key in the sidebar or run the container with `-e OPENAI_API_KEY=sk-...`")
    st.stop()

# Tabs
tabs = st.tabs(["📄 Upload & Index", "💬 Ask Estel", "📚 Chat History"])

# Tab 1: Upload & Index
with tabs[0]:
    st.subheader("Upload documents for Estel to read")
    uploaded_files = st.file_uploader(
        "Upload PDF or TXT files",
        type=["pdf", "txt"],
        accept_multiple_files=True
    )

    if st.button("📥 Process Documents") and uploaded_files:
        with st.spinner("Loading and indexing documents..."):
            try:
                docs = load_documents(uploaded_files)
                vectorstore = create_vectorstore(docs)
                st.session_state.estel_chain = get_chain(vectorstore)
                st.success(f"✅ Documents successfully processed and indexed! ({len(docs)} document(s) loaded)")
            except Exception as e:
                st.error(f"❌ Error processing documents: {e}")

# Tab 2: Ask Estel
with tabs[1]:
    st.subheader("Ask Estel")

    # Show chat history
    for user_prompt, response in st.session_state.estel_chat_history:
        with st.chat_message("user"):
            st.markdown(user_prompt)
        with st.chat_message("assistant"):
            st.markdown(response)

    # Input
    prompt = st.chat_input("Ask a question about your documents...")
    if prompt:
        chain = st.session_state.get("estel_chain")
        if chain:
            with st.chat_message("user"):
                st.markdown(prompt)
            with st.spinner("Thinking..."):
                result = chain.invoke({"query": prompt})
                answer = result["result"]
            with st.chat_message("assistant"):
                st.markdown(answer)
            st.session_state.estel_chat_history.append((prompt, answer))
        else:
            st.error("Please upload and process documents first (use the Upload & Index tab).")

# Tab 3: Full Chat History
with tabs[2]:
    st.subheader("Chat History with Estel")
    if not st.session_state.estel_chat_history:
        st.info("No questions asked yet.")
    else:
        for i, (user_prompt, response) in enumerate(st.session_state.estel_chat_history, 1):
            st.markdown(f"**Q{i}:** {user_prompt}")
            st.markdown(f"**A{i}:** {response}")
            st.markdown("---")

        if st.button("🗑️ Clear Chat History"):
            st.session_state.estel_chat_history = []
            st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9em;">
    <strong>RAG Chat with Estel</strong> | Part of GenAI Foundry<br>
    Demonstrates document-grounded retrieval-augmented generation
</div>
""", unsafe_allow_html=True)
