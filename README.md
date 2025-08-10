# Project 1: Flipkart Watch Scraper

This project contains a Python script that scrapes watch information from a Flipkart search results page, processes the data, and saves it to an Excel file.

## Solution Explanation

This script uses Object-Oriented Programming (OOP) principles by defining a `WatchScraper` class to handle the scraping logic.

The process is as follows:
1.  It fetches the HTML content from the Flipkart search results for "Watches for Men under 2000".
2.  The raw HTML is saved into a `page_content.txt` file for reference.
3.  Using the `BeautifulSoup` library, it parses the HTML to extract the watch name, price, and brand for each product.
4.  It filters out any watches with a price greater than 2000.
5.  Finally, it uses the `pandas` library to store the filtered data into a `watches_data.xlsx` file.

## Setup Instructions

Follow these steps to set up and run the script locally.

1.  Clone the repository:
    ```bash
    git clone [https://github.com/harshkrishnani/watch-scraper-project.git](https://github.com/harshkrishnani/watch-scraper-project.git)
    cd watch-scraper-project
    ```

2.  Create and activate a virtual environment:
    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate on Windows
    venv\Scripts\activate

    # Activate on macOS/Linux
    source venv/bin/activate
    ```

3.  Install the required dependencies:
    ```bash
    pip install requests beautifulsoup4 pandas openpyxl
    ```

## How to Run the Scraper

To run the script and generate the Excel file, execute the following command in your terminal:

```bash
python scraper.py
