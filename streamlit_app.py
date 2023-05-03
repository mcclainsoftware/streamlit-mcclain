
from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
from llama_index import GPTVectorStoreIndex

#index = GPTVectorStoreIndex.load_from_disk('.\\vector\\vector.json')

if 'response' not in st.session_state:
    st.session_state.response = ''

def send_click():
    st.session_state.response  = 'dont know' #index.query(st.session_state.prompt +" Only give answers you are sure about given the content of WebTMA knowledge base", verbose=True)

"""
# TMA Question Asker

Learning how to do Python and LlamaIndex AKA GPT Index
"""
st.text_input("Ask something: ", key='prompt')
st.button("Send", on_click=send_click)
st.subheader("Response: ")
st.success(st.session_state.response, icon= "🤖")
