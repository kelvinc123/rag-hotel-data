import openai
import streamlit as st
from rag import Rag

if __name__ == "__main__":
    rag = Rag()
    # Streamlit UI
    st.title('Your personal hotel chatbot')
    user_input = st.text_input("Ask me about hotel")

    if user_input:
        with st.spinner('Thinking...'):
            response = rag.chat(user_input)
            st.text_area("Response", value=response, height=250, max_chars=None, key=None)