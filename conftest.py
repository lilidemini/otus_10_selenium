import pytest
import datetime
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--base_url", default="http://localhost/", help="base URL for tests"
    )
    parser.addoption(
        "--admin_login_url", default="http://localhost/admin", help="admin login URL for tests"
    )
    parser.addoption(
        "--account_register_url", default="http://localhost//index.php?route=account/register",
        help="base URL for tests"
    )
    parser.addoption(
        "--browser", default="firefox", help="browsers for tests: chrome, firefox and opera"
    )
    parser.addoption(
        "--log_level", action="store", default="DEBUG"
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
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.originalname}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox" or browser_name == "ff":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "opera":
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    else:
        raise pytest.UsageError("--browser supported only Chrome, Firefox and Opera")

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser)

    driver.maximize_window()

    def fin():
        driver.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
    return driver
