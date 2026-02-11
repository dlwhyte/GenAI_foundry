from langchain.chains import RetrievalQA
from langchain_core.vectorstores import VectorStore
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from estel.constants import MODEL_NAME


def get_chain(vectorstore: VectorStore) -> RetrievalQA:
    """
    Create a RetrievalQA chain from a vectorstore.
    """
    llm = ChatOpenAI(model=MODEL_NAME, temperature=0)
    prompt_template = """You are a helpful assistant. Use the context below to answer the user's question.
    
    Context:
    {context}

    Question: {question}

    Answer:"""

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=False,
    )
    return chain
