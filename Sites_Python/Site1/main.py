# Ctrl+C no terminal interrompe o site

## Título ##

### input do chat ###
    
# a cada mensagem enviada:
    # mostrar a mensagem que o usuário enviou no chat
    # enviar a mensagem para a I.A. responder
    # mostrar na tela a resposta da I.A.


# streamlit -> criar sites com soluções de I.A.
    # front e backend






import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key=" ")

# título
st.write("# ChatBot com I.A.") # markdown


## session_state -> memória | dicionário ##
if not "msg_list" in st.session_state:
    st.session_state["msg_list"] = []



# exibir o histórico de mensagens
for mensagem in st.session_state["msg_list"]:
    role = mensagem["role"]
    text = mensagem["content"]
    st.chat_message(role).write(text)


# input do usuário
msg_user = st.chat_input("Digita sua dúvida aqui...")


if msg_user:
    # user -> humano
    # assistant -> inteligência artificial
    st.chat_message("user").write(msg_user)
    mensagem = {
        "role": "user", "content":msg_user
    }
    st.session_state["msg_list"].append(mensagem)

    #resposta da I.A.
    answer_modelo = modelo.chat.completions.create(
        messages=st.session_state["msg_list"],
        model="gpt-3.5-turbo"
    )
    print(answer_modelo)
    answerIA = answer_modelo.choices[0].message.content

    #exibir a resposta da I.A. na tela
    st.chat_message("assistant").write(answerIA)
    mensagem_ia = {
        "role": "assistant", "content": answerIA
    }
    st.session_state["msg_list"].append(mensagem_ia)
