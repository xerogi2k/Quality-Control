from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    QUANTITY_INPUT = (By.CSS_SELECTOR, "input[name='quantity']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "a.add-to-cart-link")
    CART_MODAL = (By.CSS_SELECTOR, "#cart")
    CART_BUTTON = (By.CSS_SELECTOR, "a[href='cart/show']")
    CART_PRODUCT_LINKS = (By.CSS_SELECTOR, "#cart tbody tr td a[href^='product/']")
    CART_QUANTITIES = (By.CSS_SELECTOR, "#cart tbody tr td:nth-child(3)")
    CART_PRICES = (By.CSS_SELECTOR, "#cart tbody tr td:nth-child(4)")
    CART_TOTAL = (By.CSS_SELECTOR, "#cart .cart-sum")

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, quantity):
        quantity_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.QUANTITY_INPUT)
        )
        quantity_field.clear()
        quantity_field.send_keys(str(quantity))

        add_button = self.driver.find_element(*self.ADD_TO_CART_BUTTON)
        add_button.click()

    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(self.CART_MODAL)
        )
        cart_button = self.driver.find_element(*self.CART_BUTTON)
        cart_button.click()

    def wait_for_cart_modal(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CART_MODAL)
        )

    def get_cart_item_names(self):
        self.wait_for_cart_modal()
        items = self.driver.find_elements(*self.CART_PRODUCT_LINKS)
        return [item.get_attribute("title") or item.text.strip() for item in items]

    def get_cart_item_quantity(self):
        self.wait_for_cart_modal()
        quantities = self.driver.find_elements(*self.CART_QUANTITIES)
        return [q.text.strip() for q in quantities if q.text.strip().isdigit()]

    def get_cart_item_prices(self):
        self.wait_for_cart_modal()
        prices = self.driver.find_elements(*self.CART_PRICES)
        return [p.text.strip() for p in prices if p.text.strip()]

    def get_cart_total(self):
        self.wait_for_cart_modal()
        total = self.driver.find_element(*self.CART_TOTAL)
        return total.text.strip()
