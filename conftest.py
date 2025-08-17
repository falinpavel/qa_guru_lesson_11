import os
import pytest

from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from const import Const
from utils import attach


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version', default=Const.DEFAULT_BROWSER_VERSION,
        help=f"Choose browser version (default: {Const.DEFAULT_BROWSER_VERSION})"
    )


@pytest.fixture(scope="session", autouse=True)
def load_environment():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def browser_options(request):
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
        "download.default_directory": Const.RESOURCES_DIR,
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True
    }
    driver_options.add_experimental_option(name="prefs", value=prefs)
    browser_version = request.config.getoption("--browser_version")
    browser_version = browser_version if browser_version else Const.DEFAULT_BROWSER_VERSION
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True
        }
    }
    driver_options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{os.getenv('LOGIN')}:{os.getenv('PASSWORD')}@selenoid.autotests.cloud/wd/hub",
        options=driver_options
    )
    browser.config.driver = driver
    yield
    attach.add_screenshot(browser=browser)
    attach.add_logs(browser=browser)
    attach.add_html(browser=browser)
    attach.add_video(browser=browser)
    browser.quit()
