from fastapi import APIRouter, Request
from app.mcp.mcp_routes import mcp_app

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Main app running. "}

@router.get("/whoami")
async def whoami(request: Request):
    return {"user": request.state.user}
