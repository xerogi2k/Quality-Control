import pytest
import json
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

#  pytest tests/test_login.py -v

def load_test_data():
    with open("config/test_login.json") as f:
        return json.load(f)

@pytest.mark.usefixtures("driver")
def test_login(driver):
    data = load_test_data()
    page = LoginPage(driver)

    page.open(data["url"])
    page.open_login_page()
    page.login(data["valid_credentials"]["login"], data["valid_credentials"]["password"])

    success_text = page.get_success_message()
    assert success_text == "Вы успешно авторизованы"


@pytest.mark.usefixtures("driver")
def test_invalid_login(driver):
    data = load_test_data()
    page = LoginPage(driver)

    page.open(data["url"])
    page.open_login_page()
    page.login(data["invalid_credentials"]["login"], data["invalid_credentials"]["password"])

    error_text = page.get_error_message()
    assert error_text == "Логин/пароль введены неверно"

@pytest.mark.usefixtures("driver")
def test_empty_login(driver):
    data = load_test_data()
    page = LoginPage(driver)

    page.open(data["url"])
    page.open_login_page()

    page.login(data["empty_credentials"]["login"], data["empty_credentials"]["password"])

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit'].disabled")
    assert login_button is not None
