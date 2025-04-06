import requests
from bs4 import BeautifulSoup
from langchain.tools import DuckDuckGoSearchRun

class WebSearcher:
    def __init__(self):
        self.search = DuckDuckGoSearchRun()

    def search(self, topic):
        """Search the web for additional information about a topic"""
        try:
            # Use DuckDuckGo search to get relevant information
            results = self.search.run(f"ICSE Class 7 {topic}")
            
            # Process and clean the results
            cleaned_results = self._clean_search_results(results)
            return cleaned_results
        except Exception as e:
            print(f"Error during web search: {str(e)}")
            return None

    def _clean_search_results(self, results):
        """Clean and format the search results"""
        # Split the results into sentences
        sentences = results.split('. ')
        
        # Filter out irrelevant information
        relevant_sentences = [
            sentence for sentence in sentences
            if any(keyword in sentence.lower() for keyword in ['icse', 'class 7', 'grade 7'])
        ]
        
        return '. '.join(relevant_sentences) 