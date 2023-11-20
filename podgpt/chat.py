import streamlit as st
from pathlib import Path

from components.qa_model import QA_Model
from components.documents import Documents
from chat_view_model import ChatViewModel
from utils.file_manager import FileManager

def create_application(view_model: ChatViewModel):
    st.set_page_config("PodGPT")
    if view_model.show_chat():
        st.session_state.show_chat = True

    if "show_chat" not in st.session_state:
        create_setup(view_model = view_model)
    else:
        create_chat(view_model = view_model)
        
def create_setup(view_model: ChatViewModel):
    st.title("PodGPT Setup")

    st.info("No database was found. Please add any files you want to constitute the database. Once done, click on Process")
    
    uploaded_files = st.file_uploader("Please upload your files", type=["pdf", "txt", "docx", "doc"], accept_multiple_files=True)
    
    if st.button("Process", type="primary"):        
        with st.spinner('Moving your files into docs folder'):
            view_model.save_files(uploaded_files=uploaded_files)

        with st.spinner('Ingesting documents...'):
            view_model.ingest_docs()
            st.session_state.show_chat = True
            st.rerun()

def create_chat(view_model: ChatViewModel):
    st.title("PodGPT")

    with st.sidebar:
        st.info('The following reference files were used to construct answer', icon="ℹ️")
       
        st.title('Reference Files')
        for file_name in FileManager.getFiles():
            if file_name.endswith('.pdf'):
                with open('./docs/' +str(file_name), "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                st.download_button(label=file_name,
                                    data=PDFbyte,
                                    file_name=file_name,
                                    mime='application/octet-stream')
                
            elif file_name.endswith('.txt'):
                st.download_button(file_name, Path('./docs/' + str(file_name)).read_text(), file_name)
        
        st.divider()
        if st.button("Clear database", type="primary"):
            view_model.clear_database()
            del st.session_state.show_chat
            st.rerun()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("What's your question?"):

        # Add user message to the chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response
        with st.chat_message("assistant"):
            message_placeholder = st.markdown("AI is thinking...")
            response = view_model.generate_response(prompt)
            print(response)
            message_placeholder.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})