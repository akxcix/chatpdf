import streamlit as st
from utils.constants import SYSTEM_PROMPTS

def generate_prompt(task, content, user_question=None, selected_page=None, page1=None, page2=None):
    if content is None:
        st.info("Upload a PDF to see extraction.")
        return None

    separator = "\n---------------------------------\n\n"
    
    if task == "Summarization":
        return content["text"]
    
    if task == "Q&A":
        if user_question:
            return content["text"] + separator + user_question
        st.info("Please enter a question")
        return None
    
    if task == "Expansion":
        if selected_page is not None:
            return content["pageText"][selected_page - 1]
        st.info("Please select a page")
        return None
    
    if task == "Comparison":
        if page1 and page2:
            return (
                "First document"
                + separator
                + content["pageText"][page1 - 1]
                + separator
                + "Second document"
                + content["pageText"][page2 - 1]
                + separator
            )
        st.info("Please select the two pages to compare")
        return None
    
    if task == "MCQ Generation":
        return content["text"]
    
    return None

def get_messages(task, prompt):
    if prompt is None:
        return None
    
    # Start with system message
    messages = [{"role": "system", "content": SYSTEM_PROMPTS[task]}]
    
    # Add chat history if it exists
    if "chat_history" in st.session_state:
        messages.extend(st.session_state.chat_history)
    
    # Add the current prompt
    messages.append({"role": "user", "content": prompt})
    
    return messages 