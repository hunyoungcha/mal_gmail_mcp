
from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

mcp = FastMCP("http Server")


@mcp.tool()
def hello(name: str) -> str:
    """
    Simple tool that greets the provided name.
    """
    return f"Hello, {name}!"


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two numbers and returns the sum.
    """
    return a + b
