import requests
from bs4 import BeautifulSoup as bs


def menu_links(url):
    address = url
    response = requests.get(address)
    soup = bs(response.text, 'lxml')

    # Gets the urls from the category menu
    links = [item['href'] for item in soup.find_all(class_='styles__CategoryLink-sc-8hzx8v-1 fTpStU')]

    # Gets the title from the category menu
    title = [item.text for item in soup.find_all(class_='styles__CategoryLink-sc-8hzx8v-1 fTpStU')]

    # Combine the title and urls into a dictionary
    cat_dict = dict(zip(title, links))

    # The links don't include https://www.argos.co.uk so the following code adds it.
    prefix_url = 'https://www.argos.co.uk'

    for k, v in cat_dict.items():
        v = prefix_url + v
        cat_dict[k] = v

    return cat_dict
