# python-mcp-server-template

A Python template for a Microservice Control Plane (MCP) server, featuring a health check controller and OpenAPI support.  
**Ready to run with Docker, locally, or as an MCP server for Claude Desktop.**

---

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
  - [Run with Docker](#run-with-docker)
  - [Run Locally (with uv)](#run-locally-with-uv)
  - [Run as MCP Server for Claude Desktop](#run-as-mcp-server-for-claude-desktop)
- [API & OpenAPI](#api--openapi)
- [Makefile Commands](#makefile-commands)
- [Contributing](#contributing)
- [License](#license)

---

## Features
- FastAPI-based Python server
- Health check endpoint
- OpenAPI (Swagger) documentation
- Docker and local development support
- Ready for integration with Claude Desktop via MCP

---

## Prerequisites

- [uv](https://github.com/astral-sh/uv) (for local runs)
- [Docker](https://www.docker.com/) (for containerized runs)
- [Claude Desktop](https://www.anthropic.com/claude) (optional, for MCP integration)

---

## Quick Start

### Run with Docker

```bash
docker-compose up --build
```
The API will be available at [http://localhost:8000](http://localhost:8000).

**Validate the app is running:**
```bash
curl -X GET http://localhost:8000/healthz
```
Expected response:
```json
{"message":"API is up and running!!"}
```

---

### Run Locally (with uv)

```bash
pip install uv
make init
make run
```
Or, directly:
```bash
uv run src/main.py
```
The API will be available at [http://localhost:8000](http://localhost:8000).

**Validate the app is running:**
```bash
curl -X GET http://localhost:8000/healthz
```
Expected response:
```json
{"message":"API is up and running!!"}
```

---

### Run as MCP Server for Claude Desktop

1. Open Claude Desktop configuration directory:
   ```bash
   open ~/Library/Application\ Support/Claude
   ```
2. Go to Claude -> Settings -> Developer -> Edit Config

3. Create or edit `claude_desktop_config.json`:
   ```json
   {
     "mcpServers": {
       "python-mcp-server-template": {
         "command": "/absolute/path/to/uv",
         "args": [
           "--directory",
           "/absolute/path/to/python-mcp-server-template",
           "run",
           "src/main.py"
         ]
       }
     }
   }
   ```
   - Replace paths with your actual locations.
   - Find your `uv` path with `which uv`.

#### Example: Using npx with mcp-remote (localhost:8000)

If you want to connect Claude Desktop to a remote MCP server using `npx` and `mcp-remote`, you can use the following configuration in your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "python-mcp-server-template": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://localhost:8000/mcp/"
      ]
    }
  }
}
```

- This will use `npx` to run the `mcp-remote` package and connect to the MCP server at `https://localhost:8000/mcp/`.
- Make sure you have `npx` installed (it comes with Node.js).
- You can add multiple servers under the `mcpServers` key for different environments or projects.


---

## Makefile Commands

| Command                  | Description                                 |
|--------------------------|---------------------------------------------|
| `make init`              | Install dependencies                        |
| `make run`               | Run locally                                 |
| `make run_local`         | Run in Docker                               |
| `make test`              | Run unit tests                              |
| `make coverage-test`     | Run coverage tests                          |
| `make integration-test`  | Run integration tests                       |
| `make tear_down_containers` | Stop and remove Docker containers        |

---

## Contributing

Contributions are welcome!  
Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

[MIT](LICENSE) or your preferred license. 