# wuwa-wiki-api-mcp

`wuwa-wiki-api-mcp` is an MCP Server that talks to a GraphQL API to retrieve information about Wuthering Waves (aka "wuwa"). It works hand-in-hand with the GraphQL server in the [wuwa-wiki-api](https://github.com/d2verb/wuwa-wiki-api) repository, so if you want to run the MCP server locally, be sure to clone and start that GraphQL server as well.

## Requirements

- Python 3.12 or higher
- uv

## Quick Start

Start the MCP server manually:
```bash
uv run main.py
```

Sample server definition for your MCP configuration file (e.g. `claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "wuwa-wiki-api-mcp": {
      "command": "/path/to/uv",
      "args": [
        "--directory",
        "/path/to/wuwa-wiki-api-mcp",
        "run",
        "main.py"
      ]
    }
  }
}
```

