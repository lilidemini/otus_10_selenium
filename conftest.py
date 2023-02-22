import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager


def pytest_addoption(parser):
    # URLS
    parser.addoption(
        "--base_url", default="http://localhost:8081/", help="base URL for tests"
    )
    parser.addoption(
        "--admin_login_url", default="http://localhost:8081/admin", help="admin login URL for tests"
    )
    parser.addoption(
        "--account_register_url", default="http://localhost:8081//index.php?route=account/register",
        help="base URL for tests"
    )
    # BROWSERS
    parser.addoption(
        "--browser", default="chrome", help="browsers for tests: chrome, firefox and opera"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture
def admin_login_url(request):
    return request.config.getoption("--admin_login_url")


@pytest.fixture
def account_register_url(request):
    return request.config.getoption("--account_register_url")


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

    request.addfinalizer(driver.close)

    return driver
