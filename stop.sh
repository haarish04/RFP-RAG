#!/bin/bash
# Stop Backend server
echo "Stopping Backend server..."
# Find the uvicorn process and kill it
kill -9 $(lsof -t -i:8090)

# Stop Frontend server
echo "Stopping Frontend..."
# Find the vite process and kill it
kill -9 $(lsof -t -i:5173)

# Stop ChromaDB Docker container
echo "Stopping ChromaDB container..."
docker stop chromadb
echo "All services stopped."