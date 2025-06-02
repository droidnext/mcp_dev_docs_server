# Quickstart Guide: Integrating with the XYZ Application via MCP Tools

This guide provides a step-by-step process for integrating your application with the XYZ service using the Model Context Protocol (MCP) tools.

## Prerequisites

Before you begin, ensure you have the following installed:

*   Python 3.7 or higher
*   `uv` package manager (`pip install uv`)
*   Access to the XYZ application API and necessary credentials.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [repository_url]
    cd [repository_directory]
    ```

2.  **Set up the virtual environment and install dependencies:**

    ```bash
    uv init
    uv venv
    source .venv/bin/activate
    uv pip install fastapi uvicorn openai fastmcp
    ```

3.  **Configure environment variables:**

    Create a `.env` file in the root directory of your project and add the following, replacing the placeholder values with your actual credentials:

    ```env
    XYZ_API_KEY=your_xyz_api_key
    XYZ_API_URL=your_xyz_api_url
    ```

## Usage

This section will walk you through making your first call to the XYZ application using the provided MCP tools.

1.  **Import necessary libraries:**

    ```python
    from fastmcp import mcp
    import os
    ```

2.  **Initialize the MCP client:**

    ```python
    # Assuming XYZ_API_KEY and XYZ_API_URL are set in your .env file
    xyz_api_key = os.environ.get("XYZ_API_KEY")
    xyz_api_url = os.environ.get("XYZ_API_URL")

    if not xyz_api_key or not xyz_api_url:
        raise ValueError("XYZ_API_KEY and XYZ_API_URL must be set in the environment.")

    mcp_client = mcp.MCPClient(api_key=xyz_api_key, api_url=xyz_api_url)
    ```

3.  **Make a sample API call:**

    ```python
    try:
        response = mcp_client.send_request("some_xyz_endpoint", {"param1": "value1"})
        print("API Response:", response)
    except Exception as e:
        print(f"An error occurred: {e}")
    ```
