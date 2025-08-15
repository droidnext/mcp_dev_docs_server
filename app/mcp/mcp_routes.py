from fastmcp import FastMCP, Context
import logging
from pathlib import Path



logger = logging.getLogger("MCP Document App")


content_dir = Path(__file__).parent.parent.parent / "content"  # Go up three levels to project root


# Initialize FastMCP
mcp = FastMCP(
    "MCP Documents App",
    # description="Application documentation MCP Server",
    instructions="""
    # Applcaition documentation MCP Server

    This server provides tools to access Application documentation like quickstart and code examples.
    """,
    version="1.0.0"
)

@mcp.tool()
async def quickstart(application_name: str, query: str, context: Context) -> str:
    """Get quickstart documentation for a specific application.

    Args:
        application_name: Name of the application to get documentation for
        query: Search query to filter documentation content
        context: FastMCP context object

    Returns:
        str: Markdown content of the quickstart documentation
    """
    quickstart_path = content_dir / application_name / "quickstart.md"
    return quickstart_path.read_text(encoding="utf-8")


@mcp.tool()
async def code_examples(application_name: str, query: str, context: Context) -> str:
    """Get code examples for a specific application.

    Args:
        application_name: Name of the application to get documentation for
        query: Search query to filter documentation content
        context: FastMCP context object

    Returns:
        str: Markdown content of the code examples documentation
    """
    code_examples_path = content_dir / application_name / "code_examples.md"
    return code_examples_path.read_text(encoding="utf-8")




# Create FastMCP app
# mcp_app = mcp.sse_app()
mcp_app = mcp.http_app(path="/mcp-app-docs-server/mcp", transport='streamable-http')

