import re
import pdfplumber

from data_cleaning.data_extractor import *
from embedding.vector_embedding import *

PDF_PATH = 'datasets/L03 - Utility Trees and Styles.pdf'
FILE_PATH = 'datasets/lecture.txt'

text = extract_text(PDF_PATH)
save_to_text = save_to_text_file(FILE_PATH, text)

dataset = preprocess_and_chunk(FILE_PATH)

print(dataset)
print(f'Loaded {len(dataset)} coherent chunks')

query = input("What can I help you with?")

similarities = get_similarity(query, dataset)
print(similarities)

results = retrieve_best_document(query, dataset, similarities)
print(results)
