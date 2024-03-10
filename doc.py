import os
from pinecone import Pinecone
import sys
from langchain.vectorstores import Pinecone
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.document_loaders import WebBaseLoader
import streamlit as st
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI



os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["PINECONE_API_KEY"] = os.getenv("PINECONE_API_KEY")
text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=120)
llm = ChatGoogleGenerativeAI(model="gemini-pro",convert_system_message_to_human=True)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def inser_text(url, embeddings):
    loader = WebBaseLoader(url)
    documents = loader.load()
    texts = text_splitter.split_documents(documents)
    vectordb = Pinecone.from_documents(texts, embeddings, index_name="doc")
    return vectordb


def create_response(query, vectordb, llm):
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs={"k":2})
    qa = RetrievalQA.from_chain_type(
    llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True)
    result = qa({"query": query})
    response = llm.invoke(f"Your task is to answer questions by using a given context. If the context is not relevant to the question, Use your own ability to answer.Answer in at least 350 characters.  context {result}. question {query} " )
    return response.content




def main():
    url = st.text_input("Enter URL")
    if url: 
        vectordb = inser_text(url, embeddings)
        
        query = st.chat_input("Enter your query")
        if query:
            response = create_response(query, vectordb, llm)
            st.write(response)
        
        #result = sources_chain.invoke(input_documents=docs, question=query)






if __name__ == "__main__":
    main()



