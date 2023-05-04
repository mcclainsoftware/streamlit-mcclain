

import streamlit as st
import os
from llama_index import GPTVectorStoreIndex
from llama_index import download_loader
from llama_index.node_parser import SimpleNodeParser
from llama_index import GPTSimpleVectorIndex
from llama_index import LLMPredictor, GPTSimpleVectorIndex, PromptHelper, ServiceContext
from langchain import OpenAI
index = None
try:
    index = GPTVectorStoreIndex.load_from_disk('./vector/vector.json')
except Exception as exc:
    st.error("Error: "+exc)

if 'response' not in st.session_state:
    st.session_state.response = ''

def send_click():
    st.session_state.response  = 'Not working' if index==None else index.query(st.session_state.prompt +" Only give answers you are sure about given the content of WebTMA knowledge base", verbose=True)

"""
# TMA Question Asker

Learning how to do Python and LlamaIndex AKA GPT Index
"""
st.text_input("Ask something: ", key='prompt')
st.button("Send", on_click=send_click)
st.subheader("Response: ")
st.success(st.session_state.response, icon= "🤖")
