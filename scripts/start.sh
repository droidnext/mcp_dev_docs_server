#!/bin/bash

# Start the MCP Documentation Server
# Assumes the application is defined as 'mcp_app' in app/mcp/mcp_routes.py
# and runs on port 8000.

uvicorn app.main:app