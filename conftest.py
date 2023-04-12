import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager


def pytest_addoption(parser):
    # URL
    parser.addoption(
        "--url", default="http://localhost", help="base URL for tests"
    )
    # BROWSER
    parser.addoption(
        "--browser", default="chrome", help="browsers for tests: chrome, firefox and opera"
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox" or browser_name == "ff":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "opera":
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    else:
        raise pytest.UsageError("--browser supported only Chrome, Firefox and Opera")
    driver.maximize_window()

    request.addfinalizer(driver.close)

    return driver
