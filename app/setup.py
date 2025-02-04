"""Includes function to set up and run the app."""
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import app.utils.presentation as presentation
from app.utils.constants import constants
import environment
from . import find_videos_page, loop

def get_browser():
    """Creates the browser object."""
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={environment.CHROME_USER_DATA_DIR}")
    options.add_argument(f'--profile-directory={environment.CHROME_PROFILE}')
    service = Service(executable_path=environment.CHROME_DRIVER_PATH)
    browser = webdriver.Chrome(service=service, options=options)
    return browser

def run_app():
    """Starts up the browser and returns its object."""
    print(presentation.presentation()) #Cool presentation
    browser = get_browser()
    browser.get(constants.TIKTOK_ENDPOINT)
    time.sleep(5)
    find_videos_page.find_videos_page(browser=browser)
    input('Press any key to start collecting videos.')
    loop.loop(browser=browser)
    return browser
