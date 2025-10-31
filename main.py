from fastmcp import FastMCP
from message_sender import send_message

mcp = FastMCP("Gmail-MCP")

# send_message 툴 등록
@mcp.tool
def send_message_tool(to: str, subject: str, body: str) -> str:
    return send_message(to, subject, body)

if __name__ == "__main__":
    mcp.run()
