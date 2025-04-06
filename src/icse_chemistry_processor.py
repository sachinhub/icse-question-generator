import requests
from bs4 import BeautifulSoup
import os
from document_processor import DocumentProcessor

class ICSEChemistryProcessor:
    def __init__(self):
        self.base_url = "https://www.studiestoday.com/download-books/24938/chemistry.html"
        self.document_processor = DocumentProcessor()
        self.data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

    def get_book_links(self):
        """Fetch all available ICSE Class 7 Chemistry book links"""
        try:
            response = requests.get(self.base_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all links to Chemistry books
            book_links = []
            for link in soup.find_all('a', href=True):
                href = link['href']
                if 'chemistry' in href.lower() and 'class-7' in href.lower():
                    book_links.append(href)
            
            return book_links
        except Exception as e:
            print(f"Error fetching book links: {str(e)}")
            return []

    def download_book(self, book_url):
        """Download a Chemistry book from the given URL"""
        try:
            response = requests.get(book_url)
            if response.status_code == 200:
                # Extract filename from URL
                filename = os.path.basename(book_url)
                if not filename.endswith('.pdf'):
                    filename += '.pdf'
                
                # Save the file
                file_path = os.path.join(self.data_dir, filename)
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                return file_path
            return None
        except Exception as e:
            print(f"Error downloading book: {str(e)}")
            return None

    def process_chemistry_books(self):
        """Process all available ICSE Class 7 Chemistry books"""
        book_links = self.get_book_links()
        processed_content = []
        
        for link in book_links:
            file_path = self.download_book(link)
            if file_path:
                content = self.document_processor.process_document(file_path)
                processed_content.append(content)
        
        return processed_content

    def get_chapter_topics(self):
        """Get the list of chapters and topics from the Chemistry books"""
        return {
            "Chapter 1": "Elements and Compounds",
            "Chapter 2": "Physical and Chemical Changes",
            "Chapter 3": "Acids, Bases, and Salts",
            "Chapter 4": "Air and Its Constituents",
            "Chapter 5": "Water",
            "Chapter 6": "Useful Elements and Compounds",
            "Chapter 7": "Man-made Substances"
        } 