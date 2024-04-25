# CTransformers -> GGML install: pip install ctransformers
import streamlit as st
from langchain.llms import CTransformers

llm = CTransformers(
    model = "llama-2-7b-chat.ggmlv3.q6_K.bin",
    # model = "llama-2-13b.ggmlv3.q5_0.bin",
    model_type = "llama"
)

st.title("LLaMA2 : Financial Statements")

content = st.text_input("Write company name")

if st.button('Request'):
    with st.spinner('Writting ...'):
        result = llm.predict("write financial about:" + content)
        st.write(result)