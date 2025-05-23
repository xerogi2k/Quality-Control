import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture(params=['chrome', 'firefox'], scope="function")
def driver(request):
    if request.param == 'chrome':
        options = webdriver.ChromeOptions()
    elif request.param == 'firefox':
        options = webdriver.FirefoxOptions()

    # Указываем адрес Selenium Grid Hub в Docker
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options
    )

    driver.maximize_window()
    yield driver
    driver.quit()