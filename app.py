import streamlit as st
from agente import responder_pergunta

st.title("Agente Perguntas e Respostas sobre Notas Fiscais")

pergunta = st.text_input("Digite sua pergunta:")

if pergunta:
    resposta = responder_pergunta(pergunta)
    st.write("Resposta:")
    st.write(resposta)
