#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:48:21 2023

@author: williamsirski
"""
# Install PyPDF when using code for the first time
# pip install PyPDF2 nltk docx2txt
# pip install -U pip setuptools wheel
# pip install -U spacy
# !python -m spacy download en_core_web_sm
# pip install pygls

import PyPDF2
import docx2txt
import nltk
import spacy
import tkinter as tk
from tkinter import filedialog
from nltk.corpus import stopwords
from difflib import SequenceMatcher
from nltk.tokenize import word_tokenize

# Download NLTK stopwords if not already downloaded
nltk.download('stopwords')

# Load spaCy model (you'll need to download a language model, e.g., 'en_core_web_sm')
nlp = spacy.load('en_core_web_sm')

# Function to extract text from a PDF or Word document
def extract_text(file_path):
    if file_path.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(file_path)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    elif file_path.endswith('.docx'):
        text = docx2txt.process(file_path)
    else:
        print("Unsupported file format")
        return None
    return text

# Function to calculate text similarity using SequenceMatcher
def text_similarity(text1, text2):
    return SequenceMatcher(None, text1, text2).ratio()

# Function to analyze resume using spaCy
def analyze_resume(resume_text):
    doc = nlp(resume_text)
    
    # Extract entities (e.g., names, skills)
    entities = [ent.text for ent in doc.ents]

    # Extract nouns (e.g., skills, qualifications)
    nouns = [token.text for token in doc if token.pos_ == 'NOUN' and not token.is_stop]

    return entities, nouns

# Function to open file explorer dialog and return selected file path
def select_pdf_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf"), ("Word Files", "*.docx")])
    return file_path

if __name__ == "__main__":
    # Use file explorer to select the PDF resume file
    resume_file_path = select_pdf_file()

    if resume_file_path:
        # Prompt for the job description (copy-pasted text)
        job_description = input("Copy and paste the job description here:\n")

        # Extract text from the resume
        resume_text = extract_text(resume_file_path)

        if resume_text:
            # Calculate text similarity between resume and job description
            similarity_score = text_similarity(resume_text, job_description)
            print(f"Text Similarity Score: {similarity_score:.2f}")

            # Analyze resume using spaCy
            entities, nouns = analyze_resume(resume_text)

            print("\nNamed Entities in Resume:")
            for entity in entities:
                print(entity)

            print("\nNouns in Resume:")
            for noun in nouns:
                print(noun)

            # Tokenize job description and remove stopwords
            job_description_tokens = set(word_tokenize(job_description))
            stop_words = set(stopwords.words('english'))
            job_desc_keywords = [word.lower() for word in job_description_tokens if word.lower() not in stop_words]

            # Tokenize resume and remove stopwords
            resume_tokens = set(word_tokenize(resume_text))
            resume_keywords = [word.lower() for word in resume_tokens if word.lower() not in stop_words]

            # Find keywords in job description but not in the resume
            keywords_not_in_resume = set(job_desc_keywords) - set(resume_keywords)

            if keywords_not_in_resume:
                print("\nKeywords in Job Description but not in Resume:")
                for keyword in keywords_not_in_resume:
                    print(keyword)
            else:
                print("\nNo keywords found in the Job Description that are not in the Resume.")
