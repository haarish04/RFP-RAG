import chromadb

client = chromadb.HttpClient(
    tenant= "admin",
    database= "rag_db",
    host = "localhost", 
    port = "8000"
    )

collection= client.get_collection("test_embeddings")
print(collection)