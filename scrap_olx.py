from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.olx.uz/list/q-novey/').text
soup = BeautifulSoup(html_text, 'lxml')

offers = soup.find_all('div', class_='offer-wrapper')
for offer in offers:
    offer_text = offer.find('strong').text
    price = offer.find('p', class_='price').strong.text
    print(f'{offer_text} \n\tNarxi: {price}')

