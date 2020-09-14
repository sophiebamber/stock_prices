from datetime import date

import bs4
import requests
from typing import Optional
from pandas_datareader import data as pdr
from matplotlib import pyplot as plt
import pandas as pd


def get_stock_price(url: str, html_object: str) -> Optional[str]:
    
    """
    Gets the stock price from any yahoo stock page
    :param url: url to website which describes the stock
    :param html_object: description of the html object
    :return: latest price of stock 
    """

    try:
        print('Howdy')

        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.text, 'lxml')
        stock_price = soup.find_all('div', {'class': html_object})[0].find('span').text

        return stock_price
    except Exception as e:
        return e


price = get_stock_price('https://uk.finance.yahoo.com/quote/%5EVWRL/', 'My(6px) Pos(r) smartphone_Mt(6px)')
print(price)

start_date = '2011-01-01'
today = date.today()
data = pdr.get_data_yahoo('VOO', start=start_date, end=today).reset_index()
print(data)
data['Date'] = pd.to_datetime(data['Date'])

data.plot(x='Date', y=['High', 'Low'])
plt.show()