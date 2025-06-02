#!/bin/bash

# Stop the MCP Documentation Server
# Attempts to find and terminate the process running on port 8000.

PID=$(lsof -t -i :8000)

if [ -z "$PID" ]
then
  echo "No process found running on port 8000."
else
  echo "Stopping process with PID $PID"
  kill $PID
  echo "Process $PID stopped."
fi 