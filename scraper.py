import requests
from bs4 import BeautifulSoup

response = requests.get('http://books.toscrape.com/')

soup = BeautifulSoup(response.content, 'html.parser')

books = soup.find_all('article', class_='product_pod')

for book in books:
    title = book.find('h3').find('a').get('title')
    price = book.find('p', class_='price_color').text
    rating = book.find('p', class_='star-rating').get('class')[1]  # Get the second class which indicates the rating
    print(title)
    print(price)
    print(rating)