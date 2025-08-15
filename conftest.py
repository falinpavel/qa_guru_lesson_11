import pytest
from selene import browser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from const import RESOURCES_DIR
from utils import attach


@pytest.fixture(scope="function", autouse=True)
def browser_options():
    driver_options = Options()
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
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    driver_options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=driver_options
    )
    browser.config.driver = driver
    yield
    attach.add_screenshot(browser=browser)
    # attach.add_logs(browser=browser)
    attach.add_html(browser=browser)
    attach.add_video(browser=browser)
    browser.quit()

#
# @pytest.fixture(scope="function", autouse=True)
# def browser_open_and_quit(browser_options):
#     driver = webdriver.Remote(
#         command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
#         options=browser_options
#     )
#     browser.config.driver = driver
#     yield
#     attach.add_screenshot(browser)
#     attach.add_logs(browser)
#     attach.add_html(browser)
#     attach.add_video(browser)
#     browser.quit()
#
