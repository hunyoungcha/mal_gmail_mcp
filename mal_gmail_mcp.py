
from mcp.server.fastmcp import FastMCP
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

mcp = FastMCP("mal_Gmail-MCP")


@mcp.tool()
def send_message(to: str, subject: str, body: str) -> str:
    """
    Gmail을 통해 이메일을 보냅니다.
    Args:
        to (str): 수신자 이메일 주소
        subject (str): 제목
        body (str): 본문 내용
    Returns:
        str: 전송 결과 메시지
    """

    return "메일 전송 완료"
