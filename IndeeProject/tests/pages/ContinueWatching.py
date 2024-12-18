from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as wait


class ContinueWatching:
    """
    POM Class of Continue Watching Page

    Attributes:
        attribute1 (driver): Chrome WebDriver
    """

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

        # --------------------- Locators -----------------
        self.back_button = (
            By.CSS_SELECTOR, "[aria-label='Go Back and continue playing video']")  # CSS-Selector by Attribute
        self.video_thumbnail = (
            By.XPATH, "//figure[contains(@class,'poster-container')]/img")  # XPATH with Contains function
        self.video_resume_button = (
            By.CSS_SELECTOR, "[aria-label='Continue Watching']")
        self.video_resume_description = (
            By.CSS_SELECTOR, "p.responsive-text")  # CSS-Selector by class
        self.video_timeRemaining = (By.CSS_SELECTOR, "div.responsive-text")
        self.yourwatching_header = (
            By.CSS_SELECTOR, "#responsive-text-main>div>p:nth-child(1)")  # CSS-Selector by travsering to nth child
        self.video_name = (
            By.CSS_SELECTOR, "#responsive-text-main>div>p:nth-child(2)")
        self.video_totalTime = (
            By.CSS_SELECTOR, "#responsive-text-main>div>p:nth-child(4)")
        self.video_description = (
            By.CSS_SELECTOR, "#responsive-text-main>div>p:nth-child(5)")

    # Actions/Methods
    def isIn_ContinueWatchingPage(self):
        """
        To wait until user is in Continue Watching page
        """
        try:
            # As only way to come to continue watching page is by JW_player which is inside iframe
            self.driver.switch_to.default_content()
            self.wait.until(wait.visibility_of_element_located(
                self.yourwatching_header))
            print(">> User is in Continue Watching page")
            return True
        except Exception as e:
            print(
                f"Oops..!! Continue Watching video Page didnt not load, Waited for 10 seconds. {e}")
            return False

    def click_BackButton(self):
        try:
            self.driver.find_element(*self.back_button).click()
            print(">> Clicked on Back Button")
            return True
        except Exception as e:
            print(
                f"Oops..!! Back Button Element not found. {e}")
            return False

    # Is Displayed function
    def is_VideoThumbnail_Displayed(self):
        try:
            # check if Element displayed
            self.driver.find_element(*self.video_thumbnail).is_displayed()
            print(">> Video Thumbnail displayed")
            return True
        except Exception as e:
            print(
                f"Oops..!! Video Thumbnail Element not found. {e}")
            return False

    def click_ContinueWatchingButton(self):
        try:
            self.driver.find_element(*self.video_resume_button).click()
            print(">> Clicked on Resume button")
            return True
        except Exception as e:
            print(
                f"Oops..!! Continue Watching Button Element not found. {e}")

    def get_ContinueWatching_Description(self):
        try:
            return self.driver.find_element(*self.video_resume_description).text
        except Exception as e:
            print(
                f"Oops..!! Continue Watching Description Element not found. {e}")
            return None

    def get_RemainingTime(self):
        try:
            return self.driver.find_element(*self.video_timeRemaining).text
        except Exception as e:
            print(
                f"Oops..!! Remanining Time Element not found. {e}")
            return None

    def get_YourWatching_Header(self):
        try:
            return self.driver.find_element(*self.yourwatching_header).text
        except Exception as e:
            print(
                f"Oops..!! Your Watching Header Element not found. {e}")
            return None

    def get_VideoName(self):
        try:
            return self.driver.find_element(*self.video_name).text
        except Exception as e:
            print(
                f"Oops..!! Video Name Element not found. {e}")
            return None

    def get_VideoTotalTime(self):
        try:
            return self.driver.find_element(*self.video_totalTime).text
        except Exception as e:
            print(
                f"Oops..!! Video Total Time Element not found. {e}")
            return None

    def get_VideoDescription(self):
        try:
            return self.driver.find_element(*self.video_description).text
        except Exception as e:
            print(
                f"Oops..!! Video Description Element not found. {e}")
            return None
