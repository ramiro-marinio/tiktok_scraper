"""Includes function to set up the app."""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import constants
import environment

def setup():
    """Starts up the browser and returns its object."""
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={environment.CHROME_USER_DATA_DIR}")
    options.add_argument(f'--profile-directory={environment.CHROME_PROFILE}')
    service = Service(executable_path=environment.CHROME_DRIVER_PATH)
    browser = webdriver.Chrome(service=service, options=options)
    browser.get(constants.TIKTOK_ENDPOINT)
    return browser
