import os

from dotenv import load_dotenv

from langchain.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS


def load_and_split_documents(chunk_size, chunk_overlap):
    documents = []
    for file in os.listdir('docs'):
        if file.endswith('.pdf'):
            pdf_path = './docs/' + file
            loader = PyPDFLoader(pdf_path)
            documents.extend(loader.load())
        # elif file.endswith('.docx') or file.endswith('.doc'):
        #     doc_path = './docs/' + file
        #     loader = Docx2txtLoader(doc_path)
        #     documents.extend(loader.load())
        elif file.endswith('.txt'):
            text_path = './docs/' + file
            loader = TextLoader(text_path)
            documents.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap,
        length_function = len
    )

    chunks = text_splitter.split_documents(documents)
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
          