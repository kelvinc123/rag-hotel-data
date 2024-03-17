# Code from https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps
# Feel free to check the documentation and modify the script

import streamlit as st
from rag import Rag

st.title("Hotel Chatbot")

# Initialize RAG object
if 'rag' not in st.session_state:
    st.session_state.rag = Rag()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask me about hotels"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response using RAG
    with st.spinner('Thinking...'):
        response = st.session_state.rag.chat(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})