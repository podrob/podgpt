import streamlit as st

from chat import create_chat
from chat_view_model import ChatViewModel

def main():
    chat_view_model = ChatViewModel()
    create_chat(view_model=chat_view_model)

if __name__ == "__main__":
    main()