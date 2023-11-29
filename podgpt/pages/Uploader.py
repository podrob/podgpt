import streamlit as st

from chat_view_model import ChatViewModel

def create_setup(view_model: ChatViewModel):
    st.title("PodGPT Setup")
    styling()
    st.info("No database was found. Please add any files you want to constitute the database. Once done, click on Process")
    
    uploaded_files = st.file_uploader("Please upload your files", type=["pdf", "txt", "docx", "doc"], accept_multiple_files=True)
    
    if st.button("Process", type="primary"):        
        with st.spinner('Moving your files into docs folder'):
            view_model.save_files(uploaded_files=uploaded_files)

        with st.spinner('Ingesting documents...'):
            view_model.ingest_docs()
            st.session_state.show_chat = True
            st.rerun()
    
    st.divider()
    if st.button("Clear database", type="secondary"):
        view_model.clear_database()
        del st.session_state.show_chat
        st.rerun()

def styling():
     st.markdown("""
        <style>
        .st-emotion-cache-zq5wmm.ezrtsby0
                { 
                    visibility: hidden;
                }   
        .st-emotion-cache-h5rgaw.ea3mdgi1
                {
                    visibility: hidden;
                } 
        .st-emotion-cache-1dp5vir.ezrtsby1
                {
                    linear-gradient(90deg, rgb(143, 192, 67), rgb(127, 128, 131))
                }
        </style>
        """, unsafe_allow_html=True)

    
if __name__ == "__main__":
    chat_view_model = ChatViewModel()
    create_setup(chat_view_model)