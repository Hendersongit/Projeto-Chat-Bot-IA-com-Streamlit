# Passo a passo Chat Bot de IA
# Título
# Campo de mensagem(input)
# quando o usuário enviar uma mensagem
    # mostrar a mensagem na conversa 
    # mandar mensagem para a IA responder 
    # enviar a resposta da IA para o usúario 

# streamlit e a OpenAI 
#streamlit run codigo.py
import os 
from openai import OpenAI
import streamlit as st

modelo = OpenAI(
    api_key= os.getenv("GEMINI_API_KEY"),
    base_url= "https://generativelanguage.googleapis.com/v1beta/openai"
)
# st.write() -> Adicionar texto na tela
# st.button() -> Adicionar botão na tela
# st.chart() -> Adicionar gráfico na tela

st.write ("## Chat Bot de IA")

# criar histórico das conversas 

if  "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []
    # esse código pra armazenar, com a memória do streamlit
    #adicionar uma mensagem


mensagem_usuario = st.chat_input("Fala comigo")


for mensagem in st.session_state["lista_mensagens"]:
    quem_enviou = mensagem["role"]
    texto_mensagem = mensagem["content"]
    st.chat_message(quem_enviou).write(texto_mensagem)



if mensagem_usuario: 
    #exibir a mensagem na tela
    # user -> usuario 
    # assistant -> Chat Bot
    st.chat_message("user").write(mensagem_usuario)
    mensagem1 = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append (mensagem1)

    # pegar a respota da IA
    # enviar a mensagem da IA no chat 
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model= "gemini-flash-lite-latest"
    )
    resposta_ia = resposta_modelo.choices[0].message.content

    st.chat_message("assistant").write(resposta_ia)
    mensagem2 ={"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append (mensagem2)


    #enviar a resposta da IA no chat 

    #st.file_uploader -> Adicionar upload de arquivo 
    #st.audio_input -> Adcionar input de áudio

# Manter o histórico das conversa, criar memória
# Tornar as respostas inteligentes



