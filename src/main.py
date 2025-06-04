import streamlit as st
from utils.pdf_processor import process_pdf
from utils.prompt_generator import generate_prompt, get_messages
from components.ui import (
    render_task_selector,
    render_file_uploader,
    render_task_specific_ui,
    render_response,
    initialize_chat_history
)
from client import get_completion_ollama

def main():
    st.title("PDF Analyser")
    
    # Initialize chat history
    initialize_chat_history()

    task = render_task_selector()
    uploaded_file = render_file_uploader()
    
    content = None
    task_specific_input = None
    
    if uploaded_file:
        content = process_pdf(uploaded_file)
        if content:
            num_pages = len(content["pageText"])
            task_specific_input = render_task_specific_ui(task, num_pages)

    if st.button("Submit"):
        prompt = generate_prompt(
            task=task,
            content=content,
            user_question=task_specific_input if task == "Q&A" else None,
            selected_page=task_specific_input if task == "Expansion" else None,
            page1=task_specific_input[0] if task == "Comparison" and task_specific_input else None,
            page2=task_specific_input[1] if task == "Comparison" and task_specific_input else None
        )

        if prompt is not None:
            messages = get_messages(task, prompt)
            try:
                response_text = get_completion_ollama(messages)
                render_response(response_text, user_input=task_specific_input if task == "Q&A" else None)
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
