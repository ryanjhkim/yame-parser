import requests
import re
from bs4 import BeautifulSoup


def get_html_from_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if 200 <= response.status_code < 300:
        return response.text
    else:
        raise Exception('Error - could not get HTML from URL. HTTP Status # {}'.format(response.status_code))


def parse_menu_items_from_html(restaurant_html):
    restaurant_soup = BeautifulSoup(restaurant_html, 'html.parser')

    for category in restaurant_soup.findAll("h2"):
        for category_siblings in category.next_siblings:
            for menu_items in category_siblings.findAll("div", {"data-anchor-id": "MenuItem"}):
                for menu_item_name in menu_items.findAll("button"):
                    print(category.text + " - " + menu_item_name["aria-label"])


def parse_menu_item_and_price(menu_item_with_price):
    return menu_item_with_price.split("CA$")


def parse_restaurant_name(restaurant_soup):
    return restaurant_soup.findAll("h1")[0].text


def parse_restaurant_address(restaurant_soup, restaurant_name):
    restaurant_address = ""
    delivery_address = restaurant_soup.find("span", text=re.compile("delivered from"))
    for siblings in delivery_address.next_siblings:
        if siblings.find(text=re.compile(restaurant_name)):
            # takes on pattern of
            # Restaurant Name, Street Address, <a>City</a>, Province, Postal Code, Country
            for address in siblings.children:
                if get_text_from_html_tag(address) == restaurant_name:
                    continue



def get_text_from_html_tag(tag):
    try:
        adr_str = tag.text
    except AttributeError:
        adr_str = tag
    return adr_str.strip()

if __name__ == '__main__':
    resp = get_html_from_url('https://www.doordash.com/store/1058055/?pickup=false')
    # parse_menu_items_from_html(resp)
    restaurant_soup = BeautifulSoup(resp, 'html.parser')
    print(parse_restaurant_address(restaurant_soup, parse_restaurant_name(restaurant_soup)))
