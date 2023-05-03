from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os

if 'response' not in st.session_state:
    st.session_state.response = ''

def send_click():
    st.session_state.response  = 'TODO: Wire up Index with '+ st.session_state.prompt + os.environ["OPEN_API_KEY"]

"""
# TMA Question Asker

Learning how to do Python and LlamaIndex AKA GPT Index
"""
st.text_input("Ask something: ", key='prompt')
st.button("Send", on_click=send_click)
st.subheader("Response: ")
st.success(st.session_state.response, icon= "🤖")