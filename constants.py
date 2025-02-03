"""Constant values that we will use throughout the program."""
TIKTOK_ENDPOINT = "https://www.tiktok.com"
class TiktokSelectors:
    """CSS selectors for TikTok elements."""

    class MainMenu:
        """CSS selectors for the main menu."""
        SEARCH_BUTTON = "TUXButton-content"
        SEARCH_INPUT = "css-1rl3x5e-InputElement e14ntknm3"
        FIRST_VIDEO_XPATH = "/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/div/div/div[1]/div[1]/div/div/a/div/div[1]"     
    class Video:
        """CSS selectors for the video menu."""
        SCROLL_DOWN = "css-1s9jpf8-ButtonBasicButtonContainer-StyledVideoSwitch e11s2kul11"
        VIDEO_TITLE = "css-1fbzdvh-H1Container ejg0rhn1"
        LIKES = "css-1w013xe-StrongText e1hk3hf92"
        COMMENTS = "css-1w013xe-StrongText e1hk3hf92"
        SAVES = "css-1w013xe-StrongText e1hk3hf92"
