# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as bs
import re
import locale
import pandas as pd
from datetime import date


def pagination(url):
    address = url
    response = requests.get(address)
    soup = bs(response.text, 'lxml')

    # Finds the last number of the pagination navigation button
    try:
        last_page = soup.find_all(class_="Paginationstyles__PageLink-sc-1hvuf20-1 hVoiWa xs-hidden sm-row")[-1].text
        last_page_int = int(last_page)
    except IndexError:
        last_page = None

    # Logic that looks at if page has pagination or not. The first part looks at if the page has pagination
    if last_page is not None:
        x = 2
        products = []
        merged = {}
        url_list = [address]
        prefix_url = address + 'opt/page:'
        # Add number to URL based on number of pages
        while x <= last_page_int:
            url_list.append(prefix_url + str(x))
            x += 1
            # Get products from each URL, which are stored in a dictionary and added to a list
            for n in url_list:
                products.append(product_links(n))
        # Merge dictionaries into 1 dictionary instead of using lists
        if len(products) > 1:
            for y in products:
                merged.update(y)
        return merged
    else:
        # If no pagination, just get products in a dictionary
        return product_links(address)


def product_links(url):
    address = url
    response = requests.get(address)
    soup = bs(response.text, 'lxml')

    links = [item['href'] for item in soup.find_all(class_='ProductCardstyles__Title-sc-1fgptbz-12 jdEaFQ')]

    title = [item.text for item in soup.find_all(class_='ProductCardstyles__Title-sc-1fgptbz-12 jdEaFQ')]

    prod_dict = dict(zip(title, links))

    prefix_url = 'https://www.argos.co.uk'

    for k, v in prod_dict.items():
        v = prefix_url + v
        prod_dict[k] = v

    return prod_dict


def product_page(category_dic, filename):
    product_details = {}
    today = date.today()
    d1 = today.strftime("%Y%m%d")
    for k, v in category_dic.items():

        url = v
        response = requests.get(url)
        soup = bs(response.text, 'lxml')

        prod = k

        try:
            price = soup.find_all('h2')[1].text
        except IndexError:
            price = '£0'

        decimal_point_char = locale.localeconv()['decimal_point']
        clean = re.sub(r'[^0-9' + decimal_point_char + r']+', '', price)
        value = float(clean)

        product_details[prod] = value

        df = pd.DataFrame.from_dict(product_details, orient='index', columns=['Price'])
    filename = 'exports/' + filename + d1 + '.csv'
    df.to_csv(filename)
