import os


os.environ["OPENAI_API_KEY"] = "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"


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