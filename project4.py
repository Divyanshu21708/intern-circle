import requests
from bs4 import BeautifulSoup
import json

def scrape_quotes():
    # Target URL (a standard sandbox site for web scraping practice)
    url = 'http://quotes.toscrape.com/'
    
    print(f"Sending HTTP GET request to {url}...")
    
    try:
        # 1. HTTP requests handling
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for bad status codes (4xx or 5xx)
        
        # 2. HTML tag inspection & extraction
        soup = BeautifulSoup(response.text, 'html.parser')
        extracted_data = []
        
        # Inspecting the web structure: quotes are wrapped in <div class="quote">
        quote_blocks = soup.find_all('div', class_='quote')
        
        for block in quote_blocks:
            # Extracting text from <span class="text"> and <small class="author">
            text = block.find('span', class_='text').get_text(strip=True)
            author = block.find('small', class_='author').get_text(strip=True)
            
            extracted_data.append({
                'quote': text,
                'author': author
            })
            
        # 3. Data formatting into clean JSON
        output_file = 'scraped_quotes.json'
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(extracted_data, file, indent=4, ensure_ascii=False)
            
        print(f"Successfully scraped {len(extracted_data)} quotes.")
        print(f"Data has been formatted and saved to '{output_file}'.")
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the HTTP request: {e}")

if __name__ == "__main__":
    scrape_quotes()