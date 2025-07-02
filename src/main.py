from prometheusrock import PrometheusMiddleware, metrics_route
from starlette.middleware import Middleware
from internal.logger.logger import get_logger
from api.handlers.health import health as health_check_handler

from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

logger = get_logger(__name__)

APP_NAME = "python-mcp-server-template"

logger.info(f"Starting {APP_NAME} API")

mcp = FastMCP(name=APP_NAME, 
instructions="""
        This server provides an scafolding to start an mcp server using Python, uv, prometheus, and FastMCP library.""")

@mcp.custom_route("/healthz", methods=["GET"])
async def healthz(_: Request) -> JSONResponse:
    return JSONResponse(health_check_handler.healthz())

@mcp.custom_route("/readyz", methods=["GET"])
async def readyz(_: Request) -> JSONResponse:
    return JSONResponse(health_check_handler.readyz())

@mcp.custom_route("/metrics", methods=["GET"])
async def metrics(request: Request) -> Response:
    return metrics_route(request=request)

@mcp.tool
def add(a: int, b: int) -> int:
    """Adds two integer numbers together."""
    return a + b

custom_middleware = [
    Middleware(
        PrometheusMiddleware,
        app_name=APP_NAME,
        skip_paths=["/metrics", "/healthz", "/readyz"],
        remove_labels=["headers"],
    ),
]

# Get a Starlette app instance for Streamable HTTP transport (recommended)
# app is a Starlette application that can be integrated with other ASGI-compatible web frameworks (like uvicorn).
# you can run the app by calling 'uvicorn path.to.your.app:http_app --host 0.0.0.0 --port 8000'
app = mcp.http_app(middleware=custom_middleware)

# Alias for compatibility with tests and tools that expect 'http_app' instead of 'app'
http_app = app

if __name__ == "__main__":
    mcp.run(
        transport="http", 
        log_level="debug")


