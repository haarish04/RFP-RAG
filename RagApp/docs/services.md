# Services

## Overview
This module provides functionality to embed texts using the Sentence Transformers library. It utilizes a pre-trained model specified in the configuration to generate embeddings for a list of texts.


## Embedding.py


### embed_texts()

**Description:** Import the embedding model from app.config and import sentence transformers package. Define function. This function recieves a list of strings and returns the list of embeddings which is list of list of floating point integers. Invoke the encode method of that particular embedding model using the sentenceTransformer package.

---

## llm.py

### ask_llama()

**Description:** Import the together_api key from app.config and import together.ai library. Create a client to connect to the together.ai server. Make an API call and specify the model to be used. Two message arew passed to the mode. The first message creates the guideline for the model to work. Restrict the model to respond using the data provided only. The second message will contain the actual query along with the closest matching queries from the DB. The LLM will respond based on the queries stored in DB and not from its own knowledge base.

---

## retriever.py

### add_to_chroma()

**Description:** Import the chromadb client and the chromaDB port and address to establish connection with the database. Initialize a new connection using the host, port, tenant and the database. Create new collection where the embeddings are to be stored. It recieves list of ids and list of embeddings to be stored. It also recieves metadata which contans the question and answer pairs(dict). Add all the records in the collection.

---

