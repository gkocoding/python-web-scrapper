# Python Web Scraper - Books to Scrape

A simple web scraper built with Python that extracts book data from [books.toscrape.com](http://books.toscrape.com), a sandbox website designed for scraping practice.

## What it does

The scraper goes through all pages of the website and extracts the following information for each book:
- Title
- Price
- Rating (1-5 stars)

All data is saved into a `books.csv` file for easy viewing in Excel or any spreadsheet tool.

## Technologies used

- Python 3
- requests
- BeautifulSoup4

## How to run

1. Clone the repository
2. Create and activate a virtual environment: