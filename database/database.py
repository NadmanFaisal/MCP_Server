import chromadb
import asyncio
import uuid

from data_cleaning.data_extractor import *
from embedding.vector_embedding import *

async def delete_collection(collection_name, host, port):
    client = await chromadb.AsyncHttpClient(host=host, port=port)
    await client.delete_collection(name=collection_name)


async def save_to_db(file_path, host, port):
    client = await chromadb.AsyncHttpClient(host=host, port=port)
    dataset = preprocess_and_chunk(file_path)
    document_embeddings = embed_document(dataset)
    document_ids = []
    document_metadata = []

    for i in range(0, len(dataset)):
        random_id = uuid.uuid4()
        document_ids.append(f'{random_id}')
        document_metadata.append({"source": file_path})
    
    print(f'Loaded {len(dataset)} coherent chunks')
    print(f'Loaded ids: {len(document_ids)}')

    collection = await client.get_or_create_collection(name="my_collection")
    await collection.upsert(
        documents=dataset,
        ids=document_ids,
        embeddings=document_embeddings,
        metadatas=document_metadata
    )
    return True

async def get_documents(query, host, port):
    client = await chromadb.AsyncHttpClient(host=host, port=port)
    query_embedding = embed_query(query)

    collection = await client.get_or_create_collection(name="my_collection")
    documents = await collection.query(
        query_embeddings=query_embedding
    )
    return documents
