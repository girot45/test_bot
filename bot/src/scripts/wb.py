import requests

from bot.config import url


def proccess_card_info(card_dict):
    qty = 0

    for sizes in card_dict["sizes"]:
        for stock in sizes["stocks"]:
            qty += stock["qty"]

    rating = card_dict["rating"]
    name = card_dict["name"]
    price = card_dict["priceU"]/100
    card_id = card_dict["id"]

    return qty, rating, name, price, card_id

def get_card_info(item_number):
    request_url = url + item_number
    response = requests.get(request_url)
    if response.status_code != 200:
        return None
    data = response.json()
    if not data["data"]["products"]:
        return None
    return proccess_card_info(data["data"]["products"][0])
