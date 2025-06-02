# MCP Documentation Server

This project serves documentation for various applications using the Model Context Protocol (MCP). It demonstrates how to organize and expose documentation content, including quickstart guides and code examples, via MCP tools.

## 📚 Documentation Structure

Application documentation is organized under the `content/` directory. For the XYZ application, content is located in `content/xyz/` and includes:

- `quickstart.md`: A quickstart guide for integrating with the XYZ application.
- `code_examples.md`: Various code examples demonstrating how to use the XYZ application with MCP tools.

## 🛠️ MCP Tools

MCP tools are defined in `app/mcp/mcp_routes.py` to expose the documentation content:

- `quickstart`: Provides the quickstart guide for a specified application.
- `code_examples`: Provides code examples for a specified application.

## ⚙️ Setup Instructions

1.  **Initialize the environment**
    ```bash
    uv init
    uv venv
    source .venv/bin/activate
    uv pip install fastapi uvicorn openai fastmcp
    uvicorn app.main:app
    ```

2.  **Start the application server**

    Run the provided start script:

    ```bash
    chmod +x scripts/start.sh
    ./scripts/start.sh
    ```

## Connect to MCP Server using Claude Desktop

To connect Claude Desktop to this MCP documentation server, you need to add a new server configuration in Claude's settings.

1.  Open Claude Desktop settings.
2.  Navigate to the 'Developer' section.
3.  Under 'MCP Server Configs', add the following JSON configuration:

```json
{
  "AppDocsServer": {
    "command": "npx",
    "args": [
      "mcp-remote",
      "http://localhost:8000/mcp-app-docs-server/mcp"
    ]
  }
}
```

4.  Save the settings. Claude Desktop should now be able to discover and use the tools provided by this server.

## Running the MCP Inspector

To test and inspect the MCP tools exposed by this server, you can use the MCP inspector tool. Run the following command in your terminal:

```bash
npx @modelcontextprotocol/inspector node build/index.js
```

This will start the inspector, allowing you to interact with the `quickstart` and `code_examples` tools provided by this server.




