import os


os.environ["OPENAI_API_KEY"] = "Your key goes here"


import chromadb
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


def queryDB(query):
    client = chromadb.HttpClient(host="localhost", port=8000)
    embedding_function = OpenAIEmbeddings(model="text-embedding-3-large")
    db4 = Chroma(client=client, collection_name="filings", embedding_function=embedding_function)
    docs = db4.similarity_search(query)
    return [doc.metadata for doc in docs]

if __name__ == "__main__":
    result = queryDB("milestone payment")
    print(result)
