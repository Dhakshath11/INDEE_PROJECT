import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as wait


class Dashboard:
    """
    POM Class of Dashboard Page

    Attributes:
        attribute1 (driver): Chrome WebDriver
    """

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

        # --------------------- Locators -----------------
        self.allTiles_header = (By.XPATH, "//p[text()=' All Titles ']")
        # CSS-Selector Traversing
        self.dropDown = (By.CSS_SELECTOR, "#expiringSoon>span")
        self.dropDown_options = (By.CSS_SELECTOR, "div[role='menuitem']")
        self.video_thumbnail = (
            By.CSS_SELECTOR, "[alt='Test automation project']")
        self.video_description = (
            By.XPATH, "//h5[text()='Test automation project']")
        self.signOut_button = (By.CSS_SELECTOR, "button#signOutSideBar")

    # Actions/Methods
    def isIn_IndeeDashboardPage(self):
        """
        To wait until user is in Dashboard page
        """
        try:
            self.wait.until(
                wait.visibility_of_element_located(self.allTiles_header))
            print(">> User is in Dashboard")
            return True
        except Exception as e:
            print(
                f"Oops..!! Indee Tv Dashboard Page didnt not load, Waited for 10 seconds. {e}")
            return False

    def scrollToAllTiles(self):
        # Method is used to scroll user to 'All titles'
        try:
            element = self.driver.find_element(*self.allTiles_header)
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true);", element)  # Java-script
            # Implicit-Wait for Smooth Execution (:TODO Optional - Can be removed)
            time.sleep(5)
            print(">> Scrolled down to All Tiles")
            return True
        except Exception as e:
            print(f"Oops..!! Unable to scroll to All tiles. {e}")
            return False

    def get_DropDown_CurrentMode(self):
        try:
            return self.driver.find_element(*self.dropDown).text
        except Exception as e:
            print(f"Oops..!! Drop-Down Element not found. {e}")
            return None

    def get_DropDown_AvailableModes(self):
        """
        To get Available drops-downs options. As of now : Geners & Family
        """
        try:
            options = []
            elements = self.driver.find_elements(*self.dropDown_options)
            for element in elements:
                options.append(element.text)
            return options
        except Exception as e:
            print(
                f"Oops..!! Drop-Down Options Element not found. {e}")
            return None

    # Is Displayed function
    def is_Video_Displayed(self):
        try:
            self.driver.find_element(*self.video_thumbnail).is_displayed()
            print(">> video Thumbnail is displayed")
            return True
        except Exception as e:
            print(
                f"Oops..!! Video Thumbnail Element not found. {e}")
            return False

    def get_Video_Description(self):
        try:
            return self.driver.find_element(*self.video_description).text
        except Exception as e:
            print(
                f"Oops..!! Video Description Element not found. {e}")
            return False

    def click_Video(self):
        try:
            self.driver.find_element(*self.video_description).click()
            print(">> Clicked on Video")
            return True
        except Exception as e:
            print(
                f"Oops..!! Video Description Element not found. {e}")

    def Click_SignOut(self):
        try:
            self.driver.find_element(*self.signOut_button).click()
            print(">> Clicked on Sign Out button")
            return True
        except Exception as e:
            print(
                f"Oops..!! Sign Out Element not found. {e}")
