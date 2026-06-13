import requests
from bs4 import BeautifulSoup

response = requests.get('http://books.toscrape.com/')

soup = BeautifulSoup(response.content, 'html.parser')

books = soup.find_all('article', class_='product_pod')

all_books = []

for book in books:
    title = book.find('h3').find('a').get('title')
    price = book.find('p', class_='price_color').text
    rating = book.find('p', class_='star-rating').get('class')[1]  # Get the second class which indicates the rating
    dictionary = {'title': title, 'price': price, 'rating': rating}
    all_books.append(dictionary)
    
print(all_books)