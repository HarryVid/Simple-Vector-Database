from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma

from langchain_huggingface import HuggingFaceEmbeddings



document_loader = PyPDFLoader("./DailyStoic.pdf")
documents = document_loader.load()

# print(documents)
# print(type(documents))
print(len(documents))

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
chunks = text_splitter.split_documents(documents)

# print(chunks)
# print(type(chunks))
print(len(chunks))

embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

db = Chroma.from_documents(chunks, embedding_function)

query = "What do Stoics say about anger?"

search1 = db.similarity_search(query)
print(search1[0].page_content)

search2 = db.as_retriever(search_type="mmr").invoke(query)[0]
print(search2.page_content)
