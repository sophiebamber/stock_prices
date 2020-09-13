import bs4
import requests
from datetime import datetime

r = requests.get('https://uk.finance.yahoo.com/quote/%5EVWRL/')

soup = bs4.BeautifulSoup(r.text, 'lxml')

price = soup.find_all('div', {'class': 'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
print(price)