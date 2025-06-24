import chromadb
from app.services.embedding import embed_texts
from app.config import CHROMA_DB_HOST, CHROMA_DB_PORT, CHROMA_DATABASE, CHROMA_TENANT
from fastapi import HTTPException

def add_to_chroma(ids: list[str], embeddings: list[list[float]], metadatas: list[dict], collection_name: str):
    client = chromadb.HttpClient(
        tenant= CHROMA_TENANT,
        database= CHROMA_DATABASE,
        host = CHROMA_DB_HOST, 
        port = CHROMA_DB_PORT
    )
        
    existing_collections = client.list_collections()
    collection_names= [col.name for col in existing_collections]

    if collection_name in collection_names:
        raise HTTPException(status_code=400, detail=f"Collection '{collection_name}' already exists")

    collection = client.create_collection(name=collection_name)

    documents = [meta["Question"] for meta in metadatas]
    collection.add(ids=ids,
    embeddings=embeddings,
    documents=documents,
    metadatas=metadatas
    )

    return {"message": f"Created new collection with name: '{collection_name}' and ingested '{len(metadatas)}' records"}


def query_chroma_with_similarity(query: str):
    client = chromadb.HttpClient(
        tenant=CHROMA_TENANT,
        database=CHROMA_DATABASE,
        host=CHROMA_DB_HOST,
        port=CHROMA_DB_PORT
    )

   # Get all collections in the database
    collections = client.list_collections()

   # Convert query to embeddings
    query_embedding = embed_texts([query])[0]
    all_results = []
    seen_documents= set() # To avoid duplicates

   # Query each collection
    for collection_info in collections:
        collection = client.get_collection(name=collection_info.name)
        try:
            results = collection.query(
                query_embeddings=[query_embedding],
                n_results=3
            )
            docs = results["documents"][0]
            metas = results["metadatas"][0]
            distances = results.get("distances", [[None]*len(docs)])[0]

           # Add collection name to each result
            for doc, meta, dist in zip(docs, metas, distances):
                if doc in seen_documents:
                    continue
                seen_documents.add(doc)
                all_results.append({
                    "document": doc,
                    "metadata": meta,
                    "similarity": 1-dist if dist is not None else None,
                    "collection": collection_info.name  # Add the collection name
                })
        except Exception as e:
            return{"error: " + str(e)}           
        # Skip collections that may have incompatible schema or other issues

   # Sort results by similarity (highest first)
    all_results.sort(key=lambda x: x.get("similarity", 0) if x.get("similarity") is not None else 0, reverse=True)
   # Get the top results (limiting to the top N if needed)
    top_results = all_results[:3]  # You can adjust the number or make it a parameter
   # Get best result
    best_result = top_results[0] if top_results else {}
    return top_results, best_result


def delete_collection(collection_name: str):
    client = chromadb.HttpClient(
        tenant= CHROMA_TENANT,
        database= CHROMA_DATABASE,
        host = CHROMA_DB_HOST, 
        port = CHROMA_DB_PORT
    )

    collection= client.get_collection(name=collection_name)
    
    if collection is None:
        raise HTTPException(status_code=404, detail=f"Collection '{collection_name}' does not exist")
    
    client.delete_collection(name=collection_name)
    return {"message": f"Deleted collection: '{collection_name}'"}

