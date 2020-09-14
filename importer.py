import bs4
import requests
from typing import Optional


def get_stock_price(url: str, html_object: str) -> Optional[str]:
    
    """
    Gets the stock price from any yahoo stock page
    :param url: url to website which describes the stock
    :param html_object: description of the html object
    :return: latest price of stock 
    """

    try:

        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.text, 'lxml')
        stock_price = soup.find_all('div', {'class': html_object})[0].find('span').text

        return stock_price
    except Exception as e:
        return None


price = get_stock_price('https://uk.finance.yahoo.com/quote/%5EVWRL/', 'My(6px) Pos(r) smartphone_Mt(6px)')
print(price)