from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, "div.btn-group a.dropdown-toggle")
    LOGIN_LINK = (By.CSS_SELECTOR, "ul.dropdown-menu a[href*='user/login']")
    USERNAME_INPUT = (By.CSS_SELECTOR, "form#login input#login")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "form#login input#pasword")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "form#login button[type='submit']")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    ERROR_ALERT = (By.CSS_SELECTOR, ".alert-danger")

    def __init__(self, driver):
        self.driver = driver

    def open(self, base_url):
        self.driver.get(base_url)

    def open_login_page(self):
        account_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ACCOUNT_DROPDOWN)
        )
        account_dropdown.click()

        login_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGIN_LINK)
        )
        login_link.click()

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def get_success_message(self):
        try:
            alert = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.SUCCESS_ALERT)
            )
            return alert.text.strip()
        except:
            return None

    def get_error_message(self):
        try:
            alert = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.ERROR_ALERT)
            )
            return alert.text.strip()
        except:
            return None
