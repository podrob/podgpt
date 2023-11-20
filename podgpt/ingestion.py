import os

from dotenv import load_dotenv

from langchain.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


def load_and_split_documents(chunk_size, chunk_overlap):
    loader = DirectoryLoader(
        path='./docs',
        # loader_cls=PyPDFLoader,
        glob="**/*",
        show_progress=False,
        use_multithreading=True
    )

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap,
        length_function = len
    )

    chunks = loader.load_and_split(
        text_splitter=text_splitter
    )
    return chunks



def main():
    load_dotenv()
    chunk_size = 1024
    chunk_overlap = 100

    chunks = load_and_split_documents(chunk_size, chunk_overlap)
    print(chunks)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(documents= chunks, embedding=embeddings)
    vectorstore.save_local("faiss_vector_db")
    print("Success! Vector store has been created!")

if __name__ == "__main__":
    main()
          