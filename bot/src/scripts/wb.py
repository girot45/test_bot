import requests

from bot.src.config import url


def proccess_card_info(card_dict):
    qty = 0
    for stock in card_dict["sizes"]["stocks"]:
        qty += stock["qty"]

    rating = card_dict["rating"]
    name = card_dict["name"]
    price = card_dict["priceU"]/100
    salePrice = card_dict["salePriceU"]/100
    card_id = card_dict["id"]
    sale = card_dict["sale"]

    return qty, rating, name, price, salePrice, card_id, sale

def get_card_info(item_number):
    request_url = url + item_number
    response = requests.get(request_url)
    if response.status_code != 200:
        return None
    data = response.json()
    if not data["data"]["products"]:
        return None
    return proccess_card_info(data["data"]["products"])

