import os
from pinecone import Pinecone
import sys
from langchain.vectorstores import Pinecone
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import WebBaseLoader
import streamlit as st
from app import llm, embeddings

os.environ["PINECONE_API_KEY"] 




def main():
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    url = st.text_input("Enter URL")
    if query:
        loader = WebBaseLoader(query)
        documents = loader.load()
        texts = text_splitter.split_documents(documents)

    
    

        vectordb = Pinecone.from_documents(texts, embeddings, index_name="doc")

        qa_chain = ConversationalRetrievalChain.from_llm(
    llm,
    vectordb.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True
)
    
    chat_history = []
    while url:
        query = st.chat_input('Prompt: ')
        if query:
            result = qa_chain({'question': query, 'chat_history': chat_history})
            st.write_stream('Answer: ' + result['answer'] + '\n')
            chat_history.append((query, result['answer']))
        if query == "exit":
            break



if __name__ == "__main__":
    main()



