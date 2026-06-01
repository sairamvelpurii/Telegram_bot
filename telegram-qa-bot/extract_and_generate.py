import fitz
import json
import os
import re
import random
from pathlib import Path

def extract_text_from_pdfs(pdf_folder="pdfs"):
    """Extract text from all PDFs in the folder and nested folders."""
    all_text = ""
    
    if not os.path.exists(pdf_folder):
        print(f"Folder '{pdf_folder}' not found!")
        return ""
    
    pdf_files = []
    for root, _, files in os.walk(pdf_folder):
        for file_name in files:
            if file_name.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, file_name))
    
    if not pdf_files:
        print(f"No PDF files found in '{pdf_folder}' folder or nested folders!")
        return ""
    
    print(f"Found {len(pdf_files)} PDF(s). Extracting text...")
    
    for pdf_path in pdf_files:
        print(f"  Extracting: {os.path.relpath(pdf_path, pdf_folder)}")
        
        try:
            with fitz.open(pdf_path) as pdf:
                for page in pdf:
                    all_text += page.get_text() + "\n"
        except Exception as e:
            print(f"  Error reading {pdf_path}: {e}")
    
    return all_text

def parse_text_to_qa(text):
    """
    Parse extracted text into Q&A pairs.

    Supports these formats:
    1. Q: Question? A: Answer
    2. Question then Answer on the next line
    3. Numbered questions with Answer: markers
    """
    qa_pairs = []
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    # Normalize repeated numbering in the beginning of a line like "1. 1. Question"
    def normalize_line(line):
        return re.sub(r'^(?:\d+\.\s*)+', '', line).strip()
    
    question_pattern = re.compile(r'^(?:Q[:\.]?\s*)?(.*\?.*)$', re.I)
    answer_prefix = re.compile(r'^(?:Answer|A)[:\-]\s*(.*)$', re.I)
    
    i = 0
    while i < len(lines):
        line = normalize_line(lines[i])
        question_match = question_pattern.match(line)
        
        if question_match:
            question = question_match.group(1).strip()
            answer = ""
            same_line_answer = answer_prefix.search(line)
            
            if same_line_answer:
                answer = same_line_answer.group(1).strip()
            else:
                j = i + 1
                while j < len(lines):
                    next_line = normalize_line(lines[j])
                    if question_pattern.match(next_line) and next_line != 'answer':
                        break
                    answer_match = answer_prefix.match(next_line)
                    if answer_match:
                        answer = answer_match.group(1).strip()
                        j += 1
                        while j < len(lines):
                            continuation = normalize_line(lines[j])
                            if question_pattern.match(continuation) or answer_prefix.match(continuation):
                                break
                            answer += ' ' + continuation
                            j += 1
                        break
                    if not answer:
                        answer = next_line
                        j += 1
                        while j < len(lines):
                            continuation = normalize_line(lines[j])
                            if question_pattern.match(continuation) or answer_prefix.match(continuation):
                                break
                            answer += ' ' + continuation
                            j += 1
                        break
                    j += 1
                i = j - 1
            
            if question and answer:
                qa_pairs.append({"question": question, "answer": answer.strip()})
        
        i += 1
    
    return qa_pairs

def generate_questions_json(num_questions=10, pdf_folder="pdfs"):
    """Extract PDFs and generate questions.json with random selection"""
    
    # Extract text from PDFs
    text = extract_text_from_pdfs(pdf_folder)
    
    if not text:
        print("No text extracted from PDFs.")
        return False
    
    # Parse into Q&A pairs
    qa_pairs = parse_text_to_qa(text)
    
    if not qa_pairs:
        print("Could not parse Q&A from the extracted text.")
        print("\nTip: Format your PDFs with questions and answers clearly separated.")
        print("Example format:")
        print("  Q: What is Python? A: A programming language")
        print("  OR")
        print("  What is Python?")
        print("  A programming language")
        print("  OR")
        print("  1. What is SQL?\n  Answer: Structured Query Language")
        return False
    
    # Randomly select the specified number of questions
    if len(qa_pairs) <= num_questions:
        selected_qa = qa_pairs
        print(f"Only {len(qa_pairs)} questions available, selecting all")
    else:
        selected_qa = random.sample(qa_pairs, num_questions)
        print(f"Randomly selected {num_questions} questions out of {len(qa_pairs)} available")
    
    print(f"Generated {len(selected_qa)} Q&A pairs")
    
    # Save to questions.json
    with open('questions.json', 'w', encoding='utf-8') as f:
        json.dump(selected_qa, f, indent=4, ensure_ascii=False)
    
    print("✓ Updated questions.json with NEW random questions")
    return True

if __name__ == "__main__":
    # Load config
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    num_questions = config.get('num_questions', 5)
    pdf_folder = config.get('pdf_folder', 'pdfs')
    
    generate_questions_json(num_questions, pdf_folder)
