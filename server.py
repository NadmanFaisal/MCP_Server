from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
from database.database import *

# Initialize FastMCP server
mcp = FastMCP("RAG_MCP")

USER_AGENT = "weather-app/1.0"

@mcp.tool()
def add_numbers(n1: int, n2: int) -> int:
    """
        Add two integers to prodive a sum.
        args:
        n1: The first number
        n2: The second number

        return: returns an integer
    """
    return n1 + n2

@mcp.tool()
async def get_documents_from_RAG(query: str) -> str:
    """
        Retrieves the most semantically similar text documents from the 
        vector database based on the input query.

        Args:
            query: The natural language query to embed and search against.
    
        Returns:
            A concatenated string containing the retrieved documents and their sources.
    """
    results = await get_documents(query)
    documents_list = results.get('documents', [[]])[0]
    formatted_string = "--- RAG Context ---\n" + "\n".join(documents_list)
    return formatted_string

def main():
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()

