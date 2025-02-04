"""Constant values that we will use throughout the program."""
TIKTOK_ENDPOINT = "https://www.tiktok.com"
SEARCH = "products"
OUTPUT_DIRECTORY = "output"
BATCH_SIZE = 20
TARGET_VIDEOS=2000
class TiktokSelectors:
    """CSS selectors for TikTok elements."""

    class MainMenu:
        """CSS selectors for the main menu."""
        SEARCH_BUTTON = ".TUXButton-content"
        SEARCH_INPUT_XPATH = "/html/body/div[1]/div[2]/div[1]/div/div[5]/div[1]/div[2]/form/input"
        FIRST_VIDEO_XPATH = (
            "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[1]/div[1]/div/"
            "div/a/div/div[1]"
        )
    class Video:
        """CSS selectors for the video menu."""
        SCROLL_DOWN_XPATH = (
            "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div/div[1]/button[3]"
        )
        class Author:
            """CSS selectors for the author data."""
            USERNAME_XPATH = (
                '//*[@id="tabs-0-panel-search_top"]/div[3]/div/div[2]/div[1]'
                '/div/div[1]/div[1]/div[1]/a[2]/span[1]/span[1]'
            )
            NAME_XPATH = (
                '//*[@id="tabs-0-panel-search_top"]/div[3]/div/div[2]'
                '/div[1]/div/div[1]/div[1]/div[1]/a[2]/span[2]/span[1]'
            )
        class VideoData:
            """CSS selectors for the video data."""
            VIDEO_TITLE_XPATH = (
                '//*[@id="tabs-0-panel-search_top"]/div[3]/div/div[2]/'
                'div[1]/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/h1'
            )
            LIKES_XPATH = (
                '//*[@id="tabs-0-panel-search_top"]/div[3]/div/div[2]/div[1]'
                '/div/div[1]/div[2]/div/div[1]/div[1]/button[1]/strong'
            )
            COMMENTS_XPATH = (
                '//*[@id="tabs-0-panel-search_top"]/div[3]/div/'
                'div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/button[2]/strong'
            )
            SAVES_XPATH = (
                '//*[@id="tabs-0-panel-search_top"]/div[3]/div/div[2]/div[1]'
                '/div/div[1]/div[2]/div/div[1]/div[1]/div/button/strong'
            )
            DATE_XPATH = (
                "/html/body/div[1]/div[2]/div[2]/div[1]/"
                "div[2]/div[3]/div/div[2]/div[1]/div/div[1]"
                "/div[1]/div[1]/a[2]/span[2]/span[3]"
            )

class RandomWait:
    """
    Range values (in seconds) that define how much each random wait lasts for.
    The purpose of random waits is to bypass bot checks, making the client appear somewhat human.
    """
    MIN = 1
    MAX = 4
