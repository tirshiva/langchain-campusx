from langchain_ollama import ChatOllama
import streamlit as st
from langchain_core.prompts import load_prompt

st.header('Research Assistant')

llm = ChatOllama(model="llama3.2")

paper_input = st.selectbox("Select Research Paper Name", ["Attention is all you need", "BERT:Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models beat GANs on Image synthesis"])

style_input = st.selectbox("Select explanation Style", ["Beginner-friendly", "Technical", "Code Oriented", "Mathematical"])

length_input = st.selectbox("Select explanation length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

template = load_prompt('template.json')




if st.button('Submit'):
    chain = template | llm
    result = chain.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
    })
    st.write(result.content)
    