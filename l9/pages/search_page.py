from selenium.webdriver.common.by import By

class SearchPage:
    SEARCH_INPUT = (By.CSS_SELECTOR, "#typeahead")
    BREADCRUMB_QUERY = (By.CSS_SELECTOR, "div.breadcrumbs li:nth-child(2)")

    def __init__(self, driver):
        self.driver = driver

    def open(self, base_url):
        self.driver.get(base_url)

    def get_search_query_text(self):
        breadcrumb_element = self.driver.find_element(*self.BREADCRUMB_QUERY)
        return breadcrumb_element.text.strip()

    def search(self, query):
        search_box = self.driver.find_element(*self.SEARCH_INPUT)
        search_box.send_keys(query)
        search_box.submit()
