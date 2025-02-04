"""Contains function to enter scroll page."""
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import app.utils.constants.constants as constants
from app.utils.functions.random_functions import random_wait
def find_videos_page(browser:WebDriver):
    """Reaches videos page. After this, we will start scrolling and scraping videos."""
    search_button = browser.find_element(By.CSS_SELECTOR,
                                         constants.TiktokSelectors.MainMenu.SEARCH_BUTTON)
    search_button.click()
    random_wait()
    search_input = browser.find_element(By.XPATH,
                                        constants.TiktokSelectors.MainMenu.SEARCH_INPUT_XPATH)
    search_input.send_keys(constants.SEARCH + Keys.ENTER)
    input('Please continue when the videos load.')
    random_wait()
    first_video = browser.find_element(By.XPATH,constants.TiktokSelectors.
                                                MainMenu.FIRST_VIDEO_XPATH)
    first_video.click() #This will put us in the scroll page,
    # completing the function.
    random_wait()
