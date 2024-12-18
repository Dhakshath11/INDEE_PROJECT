import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as wait


class Videos:
    """
    POM Class of Video Selected

    Attributes:
        attribute1 (driver): Chrome WebDriver
    """

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver  # TODO: You need to remove it
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

        # --------------------- Locators -----------------
        self.videoname_header = (
            By.CSS_SELECTOR, ".banner-card-text-container div p")
        self.add_watchlist_icon = (
            By.CSS_SELECTOR, "[aria-label='Add to Watchlist']")
        self.add_watchlist_Description = (
            By.CSS_SELECTOR, "[aria-label='Add to Watchlist']~p")  # CSS-Selector Traversing
        self.remove_watchlist_icon = (
            By.CSS_SELECTOR, "[aria-label='Remove from Watchlist']")
        self.remove_watchlist_Description = (
            By.CSS_SELECTOR, "[aria-label='Remove from Watchlist']~p")

        self.videosection_header = (By.ID, "videosSection")
        # --------------------- VIDEO-SECTION -----------------
        self.video_thumbnail = (
            By.XPATH, "//img[contains(@alt,'thumbnail')]")  # By XPATH contians function
        self.video_play_button = (By.CSS_SELECTOR, "[aria-label='Play Video']")
        self.video_time = (
            By.XPATH, "//div[contains(@class,'play-section')]/span")
        self.video_info_button = (
            By.CSS_SELECTOR, "[aria-label='Open Info Dialog']")
        self.video_totaltime = (By.ID, "vidTitle")
        self.video_expiry_label = (
            By.XPATH, "(//span[contains(@class,'expiry-date')]/span)[1]")  # By Xpath select 1
        self.video_expiry_value = (
            By.XPATH, "(//span[contains(@class,'expiry-date')]/span)[2]")  # By Xpath select 2
        self.video_views_label = (
            By.XPATH, "(//span[contains(@class,'remaining-views')]/span)[2]")
        self.video_view_value = (
            By.XPATH, "(//span[contains(@class,'remaining-views')]/span)[2]")

        self.details_section_header = (By.ID, "detailsSection")
        # --------------------- DETAILS_SECTION -----------------
        self.details_thumbnail = (
            By.XPATH, "(//figure[contains(@class,'poster-container')]/img)[2]")
        self.details_header = (By.ID, "project-title")
        self.details_description = (By.ID, "project-description")

    # Actions/Methods
    def isIn_PlayVideoPage(self):
        """
        To wait until user is in Selected Video page
        """
        try:
            self.wait.until(wait.visibility_of_element_located(
                self.videoname_header))
            print(">> User is in Play Video Page")
            return True
        except Exception as e:
            print(
                f"Oops..!! Play video Page didnt not load, Waited for 10 seconds. {e}")
            return False

    def click_AddToWatchList(self):
        try:
            self.driver.find_element(*self.add_watchlist_icon).click()
            print(">> Clicked on Add to WatchList")
            return True
        except Exception as e:
            print(
                f"Oops..!! Add to Watchlist Icon Element not found. {e}")

    def get_AddToWatchList_Description(self):
        try:
            return self.driver.find_element(*self.add_watchlist_Description).text
        except Exception as e:
            print(
                f"Oops..!! Add to Watchlist description Element not found. {e}")
            return None

    def click_RemoveFromWatchList(self):
        try:
            self.driver.find_element(*self.remove_watchlist_icon).click()
            print(">> Clicked on Remove from WatchList")
            return True
        except Exception as e:
            print(
                f"Oops..!! Remove from Watchlist Icon Element not found. {e}")

    def get_RemoveFromWatchList_Description(self):
        try:
            self.wait.until(wait.visibility_of_element_located(
                self.remove_watchlist_Description))  # Since prior Action is performed on Add Watchlist, hence wait
            return self.driver.find_element(*self.remove_watchlist_Description).text
        except Exception as e:
            print(
                f"Oops..!! Remove from Watchlist Description Element not found. {e}")
            return None

    def click_VideoSection(self):
        try:
            self.driver.find_element(*self.videosection_header).click()
            print(">> Clicked on Video Section")
            return True
        except Exception as e:
            print(f"Oops..!! Video Section Button not found. {e}")
            return False

    def click_DetailsSection(self):
        try:
            self.driver.find_element(*self.details_section_header).click()
            print(">> Clicked on Details Section")
            return True
        except Exception as e:
            print(
                f"Oops..!! Details Section Button Element not found. {e}")
            return False

    def scrollToVideoSection(self):
        try:
            element = self.driver.find_element(*self.videosection_header)
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", element)
            print(">> Scrolled to Video Section")
            # Implicit-Wait for Smooth Execution (:TODO Optional - Can be removed)
            time.sleep(5)
            return True
        except Exception as e:
            print(f"Oops..!! Unable to scroll to Video Section. {e}")
            return False

    # Video Section Begins
    # Is Displayed function
    def is_VideoSectionThumbnail_Displayed(self):
        try:
            self.wait.until(wait.visibility_of_element_located(
                self.video_thumbnail))
            self.driver.find_element(*self.video_thumbnail).is_displayed()
            print(">> Video Thumbnail displayed in video section")
            return True
        except Exception as e:
            print(
                f"Oops..!! Video Section Thumbnail Element not found. {e}")
            return False

    def click_PlayButton(self):
        try:
            self.driver.find_element(*self.video_play_button).click()
            print(">> Clicked on Play Button")
            return True
        except Exception as e:
            print(f"Oops..!! Play Button Element not found. {e}")
            return False

    def get_VideoTime(self):
        try:
            return self.driver.find_element(*self.video_time).text
        except Exception as e:
            print(f"Oops..!! Video Time Element not found. {e}")
            return None

    def click_InfoButton(self):
        try:
            self.driver.find_element(*self.video_info_button).click()
            print(">> Clicked on Info button")
            return True
        except Exception as e:
            print(f"Oops..!! Info Button Element not found. {e}")
            return False

    def get_VideoTotalTime(self):
        try:
            self.wait.until(
                wait.visibility_of_element_located(self.video_totaltime))
            return self.driver.find_element(*self.video_totaltime).text
        except Exception as e:
            print(
                f"Oops..!! Total Video Time Element not found. {e}")
            return None

    def get_ExpiryLabel(self):
        try:
            return self.driver.find_element(*self.video_expiry_label).text
        except Exception as e:
            print(f"Oops..!! Expiry Label Element not found. {e}")
            return None

    def get_ExpiryValue(self):
        try:
            return self.driver.find_element(*self.video_expiry_label).text
        except Exception as e:
            print(f"Oops..!! Expiry Value Element not found. {e}")
            return None

    def get_RemainingViewsLabel(self):
        try:
            return self.driver.find_element(*self.video_views_label).text
        except Exception as e:
            print(
                f"Oops..!! Remaining View Label Element not found. {e}")
            return None

    def get_RemainingViewsValue(self):
        try:
            return self.driver.find_element(*self.video_view_value).text
        except Exception as e:
            print(
                f"Oops..!! Remaining View Label Element not found. {e}")
            return None

    # Details Section Begins
    def is_DetailThumbnail_displayed(self):
        try:
            self.wait.until(wait.visibility_of_element_located(
                self.details_thumbnail))  # Since prior Action is performed on Remove WatchList, hence wait
            self.driver.find_element(*self.details_thumbnail).is_displayed()
            print(">> Video Thumbnail displayed in details section")
            return True
        except Exception as e:
            print(
                f"Oops..!! Details Section Thumbnail Element not found. {e}")
            return False

    def get_Details_ProjectName(self):
        try:
            self.wait.until(wait.visibility_of_element_located(
                self.details_header))
            return self.driver.find_element(*self.details_header).text
        except Exception as e:
            print(f"Oops..!! Project Name Element not found. {e}")
            return None

    def get_Details_ProjectDescription(self):
        try:
            return self.driver.find_element(*self.details_description).text
        except Exception as e:
            print(
                f"Oops..!! Project Description Element not found. {e}")
            return None
