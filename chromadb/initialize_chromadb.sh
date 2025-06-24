#!/bin/bash

if docker ps -a | grep -q "chromadb"; then
 echo "Chromadb container already exists"
 echo "Starting chromaDB container...."
 docker start chromadb

else
 echo "Pulling chromaDB container from registry....."
 docker run -d \
 -p 8000:8000 \
 -e IS_PERSISTENT=TRUE \
 -v /opt/containers/chromadb/chroma-data:/chroma/chroma \
 --name chromadb \
 chromadb/chroma
 echo "Starting chromaDB container...."
 docker start chromadb
fi
