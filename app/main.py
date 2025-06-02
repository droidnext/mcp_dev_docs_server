import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.api.app_routes import router as api_router
from app.mcp.mcp_routes import mcp_app

logger = logging.getLogger("MainApp")


# Create main FastAPI app
app = FastAPI(
    title="MCP Development Documentation Server",
    version="0.1.0",
    # lifespan=shared_lifespan
    lifespan=mcp_app.lifespan
)

# Include API routes
app.include_router(api_router)


# Mount FastMCP app Endpoints /mcp-app-docs-server/mcp
app.mount("/", mcp_app)

if __name__ == "__main__":
    import uvicorn
    from app.main import app  # optional, to ensure correct import
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 