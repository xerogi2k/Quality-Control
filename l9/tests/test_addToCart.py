import time

import pytest
import json
from pages.cart_page import CartPage

def load_test_data():
    with open("config/test_addToCart.json") as f:
        return json.load(f)

@pytest.mark.usefixtures("driver")
def test_add_single_product_to_cart_and_verify(driver):
    data = load_test_data()

    driver.get(data["first_product"]["link"])
    cart_page = CartPage(driver)

    cart_page.add_to_cart(quantity=int(data["first_product"]["quantity"]))

    cart_page.go_to_cart()

    cart_item_names = cart_page.get_cart_item_names()
    time.sleep(1)
    print("Items ", cart_item_names)

    assert "Casio MRP-700-1AVEF" in cart_item_names

    cart_item_quantity = cart_page.get_cart_item_quantity()
    assert str(data["first_product"][
                   "quantity"]) in cart_item_quantity

    cart_item_prices = cart_page.get_cart_item_prices()
    assert str(data["first_product"][
                   "price"]) in cart_item_prices

    cart_total = cart_page.get_cart_total()

    cart_total = cart_total.lstrip('$')

    assert cart_total == f"{data['first_product']['price'] * int(data['first_product']['quantity'])}"

@pytest.mark.usefixtures("driver")
def test_add_multiple_products_to_cart(driver):
    data = load_test_data()

    driver.get(data["first_product"]["link"])
    cart_page = CartPage(driver)

    cart_page.add_to_cart(quantity=int(data["first_product"]["quantity"]))

    driver.get(data["second_product"]["link"])
    cart_page = CartPage(driver)

    cart_page.add_to_cart(quantity=int(data["second_product"]["quantity"]))

    cart_item_names = cart_page.get_cart_item_names()
    assert "Casio MRP-700-1AVEF" in cart_item_names
    assert "Casio GA-1000-1AER" in cart_item_names

    cart_item_quantity = cart_page.get_cart_item_quantity()
    assert str(data["first_product"][
                   "quantity"]) in cart_item_quantity

    cart_item_prices = cart_page.get_cart_item_prices()
    assert str(data["first_product"][
                   "price"]) in cart_item_prices

    cart_total = cart_page.get_cart_total()

    cart_total = cart_total.lstrip('$')
    total_price = (data['first_product']['price'] * int(data['first_product']['quantity']) +
                   data['second_product']['price'] * int(data['second_product']['quantity']))
    assert cart_total == str(total_price)
