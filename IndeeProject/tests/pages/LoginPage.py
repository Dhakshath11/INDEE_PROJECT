from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as wait


class LoginPage:
    """
    POM Class of Login Page

    Attributes:
        attribute1 (driver): Chrome WebDriver
    """

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

        # --------------------- Locators -----------------
        self.indee_header = (By.ID, "form-logo-image")
        self.signIn_header = (By.XPATH, "//div[text()='Sign in']")
        self.accessCode_label = (By.CSS_SELECTOR, "label[for='access-code']")
        self.accessCode_input = (By.ID, "access-code")
        self.accessCode_visible_button = (
            By.CLASS_NAME, "icon-width-gen")  # By Class-Name
        self.signin_button = (By.ID, "sign-in-button")
        self.checkbox_button = (By.ID, "remeber-me-thirty-checkbox")  # By ID
        self.checkbox_description = (
            By.XPATH, "//label[text()='Keep me signed in for 2 days']")  # By XPATH
        self.terms_description = (By.ID, "terms-and-conditions-link")
        # By CSS-Selector
        self.terms_link = (By.CSS_SELECTOR, "a[role='link']")

    # Actions/Methods
    def isIn_IndeeLoginPage(self):
        """
        To wait until user is in Login page
        """
        try:
            self.wait.until(
                wait.visibility_of_element_located(self.indee_header))
            print(">> User is in Sign In page")
            return True
        except Exception as e:
            print(
                f"Oops..!! Indee Tv Login Page didnt not load, waited for 10 seconds. {e}")
            return False

    def get_SignInHeader_text(self):
        try:
            return self.driver.find_element(*self.signIn_header).text
        except Exception as e:
            print(f"Oops..!! Sign In Header Element not found. {e}")
            return None

    def get_AccessCode_label(self):
        try:
            return self.driver.find_element(*self.accessCode_label).text
        except Exception as e:
            print(
                f"Oops..!! Access Code Label Element not found. {e}")
            return False

    def enter_AccessCode(self, accessCode):
        try:
            self.driver.find_element(
                *self.accessCode_input).send_keys(accessCode)
            print(f">> Entered Access code : {accessCode}")
            return True
        except Exception as e:
            print(
                f"Oops..!! Access Code Input field Element not found. {e}")
            return False

    def get_AccessCode(self):
        try:
            accessCode = self.driver.find_element(
                *self.accessCode_input).get_attribute("value")
            return accessCode
        except Exception as e:
            print(
                f"Oops..!! Access Code Input field Element not found. {e}")
            return None

    def click_SignIn(self):
        try:
            self.driver.find_element(*self.signin_button).click()
            print(">> Clicked sign in button")
            return True
        except Exception as e:
            print(f"Oops..!! CheckBox Element not found. {e}")
            return False

    def click_CheckBox(self):
        try:
            self.driver.find_element(*self.checkbox_button).click
            print(">> Clicked checkbox")
            return True
        except Exception as e:
            print(f"Oops..!! CheckBox Element not found. {e}")
            return False

    def get_CheckBox_Description(self):
        try:
            return self.driver.find_element(*self.checkbox_description).text
        except Exception as e:
            print(
                f"Oops..!! CheckBox Description Element not found. {e}")
            return False

    def get_Terms_Description(self):
        try:
            return self.driver.find_element(*self.terms_description).text
        except Exception as e:
            print(
                f"Oops..!! Terms Description Element not found. {e}")

    def click_TermsLink(self):
        try:
            self.driver.find_element(*self.terms_link).click
            return True
        except Exception as e:
            print(
                f"Oops..!! Terms Link button Element not found. {e}")
            return False
