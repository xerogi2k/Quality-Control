import time

import pytest
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.order_page import OrderPage

def load_test_data():
    with open("config/test_makeOrder.json") as f:
        return json.load(f)

@pytest.mark.usefixtures("driver")
def test_with_auth_user(driver):
    data = load_test_data()
    login_page = LoginPage(driver)

    login_page.open(data["url"])
    login_page.open_login_page()
    login_page.login(data["valid_credentials"]["login"], data["valid_credentials"]["password"])

    time.sleep(1)
    driver.get(data["product"]["link"])
    cart_page = CartPage(driver)
    cart_page.add_to_cart(int(data["product"]["quantity"]))
    cart_page.go_to_cart()

    order_page = OrderPage(driver)
    order_page.proceed_from_modal_to_checkout()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "form[method='post'] button[type='submit']"))
    )

    assert order_page.is_submit_enabled()

@pytest.mark.usefixtures("driver")
def test_with_nonauth_existing_user(driver):
    data = load_test_data()

    driver.get(data["product"]["link"])
    cart_page = CartPage(driver)
    cart_page.add_to_cart(int(data["product"]["quantity"]))
    cart_page.go_to_cart()

    order_page = OrderPage(driver)
    order_page.proceed_from_modal_to_checkout()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login"))
    )

    order_page.fill_checkout_form(data["existing_user_data"])
    order_page.submit_order()

    error = order_page.get_error_alert_text()
    assert error == "Этот логин уже занят"