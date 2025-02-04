"""
Contains the function which will run the app loop and make it work.
"""
import json
import os
import datetime
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from app.utils.constants import constants
from app.utils.functions import convert_number,random_functions,combine_files

def scroll_down(browser:WebDriver):
    """Scroll to next reel"""
    scroll_down_button = browser.find_element(By.XPATH,
                                                  constants.TiktokSelectors.Video.SCROLL_DOWN_XPATH)
    scroll_down_button.click()
    random_functions.random_wait()

def generate_batch_object(**kwargs):
    """Will generate JSON object for the batch."""
    return {
        'videoInfo': {
            'url': kwargs.get('url'),
            'title': kwargs.get('title'),
            'likes': kwargs.get('likes'),
            'comments': kwargs.get('comments'),
            'saves': kwargs.get('saves'),
            'date': kwargs.get('date'),
        },
        'author': {
            'username': kwargs.get('username'),
            'name': kwargs.get('name'),
        },
    }

def fetch_data(browser:WebDriver):
    """Fetches all data and returns its batch object version."""
    current_url = browser.current_url
    title = browser.find_element(By.XPATH,
                                    constants.TiktokSelectors.Video.VideoData.VIDEO_TITLE_XPATH)
    likes = browser.find_element(By.XPATH,
                                    constants.TiktokSelectors.Video.VideoData.LIKES_XPATH)
    comments = browser.find_element(By.XPATH,
                                    constants.TiktokSelectors.Video.VideoData.COMMENTS_XPATH)
    saves = browser.find_element(By.XPATH,
                                    constants.TiktokSelectors.Video.VideoData.SAVES_XPATH)
    date = browser.find_element(By.XPATH,
                                    constants.TiktokSelectors.Video.VideoData.DATE_XPATH)
    username = browser.find_element(By.XPATH,
                                    constants.TiktokSelectors.Video.Author.USERNAME_XPATH)
    name = browser.find_element(By.XPATH,
                                    constants.TiktokSelectors.Video.Author.NAME_XPATH)
    batch_object = generate_batch_object(
        url=current_url,
        title=title.text,
        likes=convert_number.convert_number(likes.text),
        comments=convert_number.convert_number(comments.text),
        saves=convert_number.convert_number(saves.text),
        date=date.text,
        username=username.text,
        name=name.text,
    )
    return batch_object
videos = 0
iterations = 0
batch = []
today_string = datetime.datetime.now().strftime("%Y-%m-%d")
def loop(browser:WebDriver):
    """This loop will run nonstop and save videos."""
    errors = 0
    def save_batch():
        """Allows us to clear the batch and save it to the disk."""
        random_suffix = random_functions.random_string(7)
        os.makedirs(constants.OUTPUT_DIRECTORY, exist_ok=True)
        os.makedirs(os.path.join(constants.OUTPUT_DIRECTORY,today_string), exist_ok=True)
        filename = f"${today_string}-{random_suffix}.json"
        file_path = os.path.join(constants.OUTPUT_DIRECTORY,today_string,filename)
        with open(file_path,
                  "w+",encoding='utf-8') as file:
            print(batch)
            file.write(json.dumps(batch))
            file.close()
            batch.clear()

    def add_to_batch(batch_object:dict):
        """Adds an object to the batch and saves it should it reach or exceed the threshold."""
        batch.append(batch_object)
        global videos
        videos += 1
        if len(batch) >= constants.BATCH_SIZE:
            save_batch()

    def cooldown():
        """Stops the loop if there are repeated errors in order to fix it."""
        if errors > 5:
            input("""The loop has temporarily stopped due to several errors.
                  Please fix the issue and press any key to continue.""")
    while videos < (constants.BATCH_SIZE * (constants.TARGET_VIDEOS // constants.BATCH_SIZE)):
        try:
            batch_object = fetch_data(browser)
            add_to_batch(batch_object=batch_object)
            scroll_down(browser=browser)
            errors = 0
        except Exception as e:
            errors += 1
            print(f'An error has occurred: {e}')
            cooldown()

    print('Finished scraping videos. Wrapping up...')
    combine_files.combine_files()
    browser.quit()
