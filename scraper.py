import requests
import csv
from bs4 import BeautifulSoup

page_number = 1
all_books = []

while True:
    response = requests.get(f'http://books.toscrape.com/catalogue/page-{page_number}.html')
    if response.status_code != 200:
        break
    soup = BeautifulSoup(response.content, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    for book in books:
        title = book.find('h3').find('a').get('title')
        price = book.find('p', class_='price_color').text
        rating = book.find('p', class_='star-rating').get('class')[1]  # Get the second class which indicates the rating
        dictionary = {'title': title, 'price': price, 'rating': rating}
        all_books.append(dictionary)
    page_number += 1


    
print(len(all_books))

with open('books.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'price', 'rating'])
    writer.writeheader()
    writer.writerows(all_books)
