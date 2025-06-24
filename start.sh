#!/bin/bash

# Start ChromaDB container
echo "Starting ChromaDB Docker container..."
docker start chromadb

# Start Backend
echo "Starting Backend server..."
cd /opt/containers/RagApp

#Activate virtual env for python app
source venv/bin/activate

#kill process if running already
kill -9 $(lsof -t -i:8090)

# Run uvicorn in background
nohup uvicorn app.main:app --reload --port 8090 > backend.log 2>&1 &

# Start Frontend
# Find the vite process and kill it if already running
kill -9 $(lsof -t -i:5173)
echo "Starting Frontend..."
cd /opt/containers/rag-app
nohup npm run dev > rag-UI.log 2>&1 &
