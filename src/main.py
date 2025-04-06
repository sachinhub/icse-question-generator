#!/usr/bin/env python3
"""
Main application file for ICSE Question Generator.
"""

import os
import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from document_processor import DocumentProcessor
from question_generator import QuestionGenerator
from web_search import WebSearcher
from icse_chemistry_processor import ICSEChemistryProcessor
from question_generator.chemistry import ChemistryGenerator
from question_generator.physics import PhysicsGenerator
from question_generator.mathematics import MathematicsGenerator
from utils.helpers import export_to_pdf, export_to_docx
from knowledge_base.chemistry_kb import ChemistryKnowledgeBase

# Load environment variables
load_dotenv()

class ICSEQuestionGenerator:
    def __init__(self):
        self.llm = OpenAI(temperature=0.7)
        self.document_processor = DocumentProcessor()
        self.question_generator = QuestionGenerator(self.llm)
        self.web_searcher = WebSearcher()
        self.chemistry_processor = ICSEChemistryProcessor()

    def process_material(self, file_path):
        """Process the ICSE course material"""
        return self.document_processor.process_document(file_path)

    def generate_questions(self, material, num_questions=10):
        """Generate questions based on the processed material"""
        return self.question_generator.generate(material, num_questions)

    def enhance_with_web_search(self, topic):
        """Enhance questions with web search results"""
        return self.web_searcher.search(topic)

def display_exam_questions(show_answers=False):
    """Display the annual exam questions and answers on the screen."""
    # Read the exam questions file
    with open('data/annual_exam_questions.md', 'r') as file:
        questions = file.read()
    
    # Read the answers file if requested
    answers = None
    if show_answers:
        with open('data/annual_exam_answers.md', 'r') as file:
            answers = file.read()
    
    # Clear the screen
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Display the questions
    print("\n" + "="*80)
    print("ICSE Class 7 Chemistry Annual Examination".center(80))
    print("="*80 + "\n")
    
    # Split the content into sections and display
    sections = questions.split('\n\n')
    for section in sections:
        if section.startswith('#'):
            print("\n" + section.strip('#').strip())
            print("-"*80)
        elif section.startswith('##'):
            print("\n" + section.strip('#').strip())
            print("-"*80)
        elif section.startswith('###'):
            print("\n" + section.strip('#').strip())
            print("-"*80)
        else:
            print(section)
        
        # If answers are requested, show them after each question
        if show_answers and answers:
            answer_section = answers.split('\n\n')
            for ans_section in answer_section:
                if ans_section.startswith('###') and section.startswith('###'):
                    if ans_section.split('\n')[0].strip('#').strip() == section.split('\n')[0].strip('#').strip():
                        print("\nAnswer:")
                        print("-"*80)
                        print(ans_section)
                        break
        
        input("\nPress Enter to continue...")
        os.system('clear' if os.name == 'posix' else 'cls')

def main():
    """Main function to run the question generator application."""
    print("Welcome to ICSE Question Generator!")
    
    while True:
        print("\nMenu:")
        print("1. View Annual Exam Questions")
        print("2. View Annual Exam Questions with Answers")
        print("3. Generate New Questions")
        print("4. Export Questions")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            display_exam_questions(show_answers=False)
        elif choice == '2':
            display_exam_questions(show_answers=True)
        elif choice == '3':
            # Initialize knowledge base
            kb = ChemistryKnowledgeBase()
            
            # Example usage
            chemistry_generator = ChemistryGenerator()
            questions = chemistry_generator.generate_questions()
            print("\nNew questions generated successfully!")
        elif choice == '4':
            # Export questions
            export_to_pdf(questions, "chemistry_questions.pdf")
            export_to_docx(questions, "chemistry_questions.docx")
            print("\nQuestions exported successfully!")
        elif choice == '5':
            print("\nThank you for using ICSE Question Generator!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main() 