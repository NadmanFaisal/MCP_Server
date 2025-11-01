import re
import pdfplumber

def preprocess_and_chunk(file_path):
    with open(file_path, 'r') as f:
        full_text = f.read()

    text = re.sub(r'\s*\n\s*\n\s*', '\n\n', full_text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    cleaned_lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join(cleaned_lines)
    chunks = [chunk.strip() for chunk in text.split('\n\n') if chunk.strip()]

    return chunks

def save_to_text_file(destination, content):
    with open(destination, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

        print(f"Successfully extracted pages of text.")
        print(f"Content written to: {destination}")

        return True 
    return False

def extract_text(source):

    full_text = ""
    
    try:
        with pdfplumber.open(source) as pdf:
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    full_text += f"\n\n--- Page {i + 1} ---\n\n{page_text}"
        print(f"Successfully extracted {len(pdf.pages)} pages of text.")
        return full_text
    
    except FileNotFoundError:
        print(f"Error: File not found at {source}")
    except Exception as e:
        print(f"An error occurred during processing: {e}")

