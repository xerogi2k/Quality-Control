from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrderPage:
    CHECKOUT_LINK = (By.CSS_SELECTOR, "a.btn.btn-primary[href='cart/view']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "form[action='cart/checkout'] button[type='submit']")
    LOGIN_INPUT = (By.CSS_SELECTOR, "#login")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#pasword")
    NAME_INPUT = (By.CSS_SELECTOR, "#name")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "#address")
    NOTE_INPUT = (By.CSS_SELECTOR, "textarea[name='note']")
    ERROR_ALERT = (By.CSS_SELECTOR, "div.alert-danger ul li")

    def __init__(self, driver):
        self.driver = driver

    def proceed_from_modal_to_checkout(self):
        checkout_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CHECKOUT_LINK)
        )
        checkout_link.click()

    def is_submit_enabled(self):
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.SUBMIT_BUTTON)
        )
        return submit_button.is_enabled()

    def fill_checkout_form(self, data):
        self.driver.find_element(*self.LOGIN_INPUT).send_keys(data["login"])
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(data["password"])
        self.driver.find_element(*self.NAME_INPUT).send_keys(data["name"])
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(data["email"])
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(data["address"])
        self.driver.find_element(*self.NOTE_INPUT).send_keys(data["note"])

    def submit_order(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_error_alert_text(self):
        try:
            alert = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.ERROR_ALERT)
            )
            return alert.text.strip()
        except:
            return None
