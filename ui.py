import os
# import shutil
import streamlit as st
import time
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from utils.content_loader import load_web_content
from utils.text_processing import process_and_index
from utils.retriever_generator import retriever_generator
from langchain_chroma import Chroma

from dotenv import load_dotenv
load_dotenv() 

st.title("Website Q&A Tool")
st.sidebar.title("Website URL")

url = st.sidebar.text_input("URL ")

process_url_clicked = st.sidebar.button("Process URL")
file_path = "./chroma_db"

main_placeholder = st.empty()
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0.0)



if process_url_clicked:
    
    # load data
    main_placeholder.text("Data Loading...Started...✅✅✅")
    docs = load_web_content(url)

    main_placeholder.text("Text Splitter...Started...✅✅✅")

    # Create vector store
    vectorstore = process_and_index(docs,file_path)
    main_placeholder.text("Embedding Vector Ready...✅✅✅")

    time.sleep(1.2)


query = main_placeholder.text_input("Question: ")

ask_question = st.button("Ask Question")

if ask_question and query:

    if os.path.exists(file_path):
        vectorstore = Chroma(persist_directory=file_path, embedding_function=OpenAIEmbeddings())
        answer = retriever_generator(vectorstore, query, llm)
        st.header("Answer")
        st.write(answer)