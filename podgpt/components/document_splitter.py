import os

from langchain.document_loaders import TextLoader, PyPDFLoader, Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

CHUNK_SIZE = 1028
CHUNK_OVERLAP = 100

class DocumentSplitter:
    def create_chunks(self):
        print ("Loading documents...")
        documents = []
        for file in os.listdir('docs'):
            if file.endswith('.pdf'):
                pdf_path = './docs/' + file
                loader = PyPDFLoader(pdf_path)
                documents.extend(loader.load())
            elif file.endswith('.docx') or file.endswith('.doc'):
                doc_path = './docs/' + file
                loader = Docx2txtLoader(doc_path)
                documents.extend(loader.load())
            elif file.endswith('.txt'):
                text_path = './docs/' + file
                loader = TextLoader(text_path)
                documents.extend(loader.load())
        print ("Documents loaded")
        print ("Creating chunks...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = CHUNK_SIZE,
            chunk_overlap = CHUNK_OVERLAP,
            length_function = len,
        )

        chunks = text_splitter.split_documents(documents)
        print("Created", len(chunks), "chunks of data")
        return chunks