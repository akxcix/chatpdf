import streamlit as st
from utils.constants import TASKS

def initialize_chat_history():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def clear_chat_history():
    st.session_state.chat_history = []

def render_task_selector():
    return st.selectbox("Select Task", TASKS)

def render_file_uploader():
    return st.file_uploader("Upload a PDF", type="pdf")

def render_task_specific_ui(task, num_pages):
    if task == "Expansion":
        return st.selectbox("Select a page to expand", range(1, num_pages + 1))
    
    if task == "Comparison":
        col1, col2 = st.columns(2)
        with col1:
            page1 = st.selectbox("Select first page", range(1, num_pages + 1), key="page1")
        with col2:
            page2 = st.selectbox("Select second page", range(1, num_pages + 1), key="page2")
        return page1, page2
    
    if task == "Q&A":
        return st.text_input("Enter your question based on the PDF")
    
    return None

def render_response(response_text, user_input=None):
    # Add the new interaction to chat history
    if user_input:
        st.session_state.chat_history.append({"role": "user", "content": user_input})
    st.session_state.chat_history.append({"role": "assistant", "content": response_text})
    
    # Add clear chat button
    if st.button("Clear Chat"):
        clear_chat_history()
        st.rerun()
    
    # Display chat history in a container
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.write("👤 You:")
                st.write(message["content"])
            else:
                st.write("🤖 Assistant:")
                st.write(message["content"])
            st.markdown("---") 