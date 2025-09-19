"""
FastMCP Echo Server
"""

from fastmcp import FastMCP

# Create server
mcp = FastMCP("Echo Server", instructions="talk like a pirate who loves Mitch Hedberg")


@mcp.tool
def mock_user(text: str) -> str:
    """Mock a user's message according to the instructions
    
    As in, repeat back what the user says, in the style dictated by the instructions.
    """
    return text
