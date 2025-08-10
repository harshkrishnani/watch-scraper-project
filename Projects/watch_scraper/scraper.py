import requests
import pandas as pd
from bs4 import BeautifulSoup

class WatchScraper:
    def __init__(self, url):
        self.url = url
        self.watches_data = []

    def fetch_page_html(self):
        """Fetches the HTML content from the URL."""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        try:
            print("Fetching the webpage...")
            response = requests.get(self.url, headers=headers)
            response.raise_for_status()
            print("Webpage fetched successfully!")
            return response.text
        except requests.RequestException as e:
            print(f"Error fetching the URL: {e}")
            return None

    def save_html_to_txt(self, html_content, filename="page_content.txt"):
        """Saves the given HTML content to a text file."""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"HTML content saved to {filename}")

    def parse_watch_data(self, html_content):
        """Parses watch data from the HTML content."""
        print("Parsing product data...")
        soup = BeautifulSoup(html_content, 'html.parser')
        
        product_grid = soup.find('div', class_='DOjaWF gdgoEp')

        if not product_grid:
            print("Could not find the main product grid. The page structure has likely changed.")
            return

        product_containers = product_grid.find_all('div', class_='_1sdMkc LFEi7Z')

        for container in product_containers:
            name_element = container.find('a', class_='WKTcLC')
            if not name_element:
                 name_element = container.find('div', class_='syl9yP')

            price_element = container.find('div', class_='Nx9bqj')

            if name_element and price_element:
                watch_name = name_element.text.strip()
                price_str = price_element.text.strip().replace('₹', '').replace(',', '')
                try:
                    price = int(price_str)

                    if price <= 2000:
                        brand = watch_name.split()[0]
                        
                        full_title_element = container.find('a', class_='WKTcLC')
                        full_title = watch_name
                        if full_title_element:
                            full_title = full_title_element.get('title', watch_name).strip()

                        self.watches_data.append({
                            'Brand': brand,
                            'Watch Name': full_title,
                            'Price': price,
                            'Availability': 'In Stock'
                        })
                except ValueError:
                    continue
        
        print(f"Found {len(self.watches_data)} watches under ₹2000.")

    def save_data_to_excel(self, filename="watches_data.xlsx"):
        """Saves the extracted data to an Excel file."""
        if not self.watches_data:
            print("No data was found to save.")
            return
            
        df = pd.DataFrame(self.watches_data)
        df.to_excel(filename, index=False)
        print(f"Data for {len(self.watches_data)} watches saved to {filename}")

    def run_scraper(self):
        """Runs the full scraping process."""
        html = self.fetch_page_html()
        if html:
            self.save_html_to_txt(html)
            self.parse_watch_data(html)
            self.save_data_to_excel()
        print("Scraping finished.")


if __name__ == "__main__":
    TARGET_URL = "https://www.flipkart.com/search?q=watches+for+men+under+2000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
    
    scraper = WatchScraper(TARGET_URL)
    scraper.run_scraper()