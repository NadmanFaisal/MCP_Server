import environ
from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
from database.database import *

# Initialize FastMCP server
mcp = FastMCP("RAG_MCP")

env = environ.Env()
env.read_env() 

CHROMA_DB_HOST = env('CHROMA_DB_HOST')
PORT = env('PORT')

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
    results = await get_documents(query, CHROMA_DB_HOST, PORT)
    documents_list = results.get('documents', [[]])[0]
    formatted_string = "--- RAG Context ---\n" + "\n".join(documents_list)
    return formatted_string

def main():
    mcp.run(transport='stdio')

if __name__ == "__main__":
    main()

