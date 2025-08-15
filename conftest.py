import pytest

from selene.support.shared import browser
from selenium import webdriver

from const import RESOURCES_DIR


@pytest.fixture(scope="function")
def browser_options():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    driver_options.add_argument("--disable-gpu")
    driver_options.add_argument("--ignore-certificate-errors")
    driver_options.add_argument("--window-size=1920,1080")
    driver_options.add_argument("--disable-extensions")
    driver_options.add_argument("--disable-popup-blocking")
    driver_options.add_argument("--disable-notifications")
    driver_options.add_argument("--disable-infobars")
    prefs = {
        "profile.default_content_settings.popups": 0,
        "profile.default_content_setting_values.notifications": 2,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "download.default_directory": RESOURCES_DIR,
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True
    }
    driver_options.add_experimental_option("prefs", prefs)
    return driver_options


@pytest.fixture(scope="function", autouse=True)
def browser_open_and_quit(browser_options):
    browser.config.driver_options = browser_options
    yield
    browser.quit()