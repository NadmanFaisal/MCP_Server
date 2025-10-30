import ollama
from embedding.vector_embedding import *

FILE = 'datasets/cat-facts.txt'

# Loading the dataset
dataset = []
with open(FILE, 'r') as file:
  dataset = file.readlines()
  print(f'Loaded {len(dataset)} entries')

query = input("What can I help you with?")

similarities = get_similarity(query, dataset)
print(similarities)
result = retrieve_best_document(query, dataset, similarities)
print(result[0]['best_document'])
