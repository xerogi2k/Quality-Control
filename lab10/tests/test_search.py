import pytest
from pages.category_page import CategoryPage
from pages.search_page import SearchPage
import json

def load_test_data():
    with open("config/test_search.json") as f:
        return json.load(f)

@pytest.mark.usefixtures("driver")
def test_search_with_query(driver):
    data = load_test_data()
    page = SearchPage(driver)

    page.open(data["url"])
    page.search(data["valid_query"])

    search_query_text = page.get_search_query_text()
    assert "Поиск по запросу \"casio\"" == search_query_text

@pytest.mark.usefixtures("driver")
def test_search_empty_query(driver):
    data = load_test_data()
    page = SearchPage(driver)

    page.open(data["url"])
    page.search(data["empty_query"])

    search_query_text = page.get_search_query_text()
    assert "Поиск по запросу \"\"" == search_query_text

@pytest.mark.usefixtures("driver")
def test_category(driver):
    data = load_test_data()

    category_page = CategoryPage(driver)
    category_page.open(data["url"])
    category_page.go_to_category()

    product_titles = category_page.get_product_titles()
    assert product_titles is not None

    # Проверяем, что хотя бы один товар содержит "casio" в названии
    casio_products = [title for title in product_titles if "casio" in title.lower()]
    assert len(casio_products) > 0, f"Не найдено ни одного товара Casio среди: {product_titles}"