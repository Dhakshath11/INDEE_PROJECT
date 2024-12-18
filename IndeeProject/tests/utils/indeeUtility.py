from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as wait
import time
from tests.pages.ContinueWatching import ContinueWatching
from tests.pages.Dashboard import Dashboard
from tests.pages.LoginPage import LoginPage
from tests.pages.Player import Player
from tests.pages.Videos import Videos


class indeeUtility:
    """
    POM Class of Login Page

    Attributes:
        attribute1 (driver): Chrome WebDriver
    """

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

    def navigate(self, url):
        # Navigate to URL
        try:
            self.driver.get(url)
            print(f"====> Navigated to URL: {url}")
            return True
        except Exception as e:
            print(f"====> Navigation error: {e}")

    def signInToIndee(self, accessCode):
        # Sign In To Indee TV
        loginPage = LoginPage(self.driver)
        assert loginPage.isIn_IndeeLoginPage(), "Not in Login Page"
        assert loginPage.get_SignInHeader_text() == "Sign in", "Sign In Text did not match"
        assert loginPage.enter_AccessCode(
            accessCode), "Unable to Enter Access Code"
        assert loginPage.get_AccessCode() == accessCode, "Access Code didnt not match"
        assert loginPage.click_SignIn(), "Unable to click on Sign In button"
        print("--------- User Logged In Successfully ---------")

    def navigateToVideo(self):
        # Navigate to Video from Dashboard
        dashboardPage = Dashboard(self.driver)
        assert dashboardPage.isIn_IndeeDashboardPage(), "Not in Dashboard"
        assert dashboardPage.get_DropDown_CurrentMode(
        ) == "Genres", "Current Drop down did not match"
        assert dashboardPage.scrollToAllTiles(), "Unable to Scroll"
        assert dashboardPage.is_Video_Displayed(), "Video is not displayed"
        assert dashboardPage.click_Video(), "Unable to click on Video"
        print("--------- User naviagted to Video Successfully ---------")

    def switchToDetailsSection(self):
        # Select Details section from Video
        videoPage = Videos(self.driver)
        assert videoPage.isIn_PlayVideoPage(), "Not in Video Page"
        assert videoPage.scrollToVideoSection(), "Unable to Scroll"
        assert videoPage.click_DetailsSection(), "Unable to click on Details Section"

        assert videoPage.is_DetailThumbnail_displayed(
        ), " Video Thumbnail is not displayed in Details section"
        assert videoPage.get_Details_ProjectName(
        ) == "Test automation project", "Project name does not match"
        assert videoPage.get_Details_ProjectDescription(
        ) == "Enterprise set up *do not delete*", "Project description does not match"
        print("--------- User Switched to Details Section ---------")

    def switchToVideoSection(self):
        # Select Video section from Video
        videoPage = Videos(self.driver)
        assert videoPage.isIn_PlayVideoPage(), "Not in Video Page"
        assert videoPage.click_VideoSection(), "Unable to click on video section"
        assert videoPage.get_VideoTotalTime(
        ) == "11m 5.1 audio", "Total Video Time did not match"
        print("--------- User Switched to Video Section ---------")

    def playPauseVideo(self, timeout):
        # Play-Pause Video for given Timeout
        videoPage = Videos(self.driver)
        player = Player(self.driver)
        assert videoPage.click_PlayButton(), "Unable to click on play button"
        player.set_Player()
        assert self.__pauseAfterTimeOut(player, timeout)
        print(
            f"--------- User Successfully Played and Paused Video within {timeout} seconds ---------")
        # Implicit-Wait for Smooth Execution (:TODO Optional - Can be removed)
        time.sleep(2)

    def __pauseAfterTimeOut(self, player: Player, timeout):
        # Private method
        while True:
            lapsed_time = player.getLapsedTime()
            if lapsed_time < 0:  # To prevent Deadlock, If Time Plased is -1
                print(f">> Unable to get lapsed time: {lapsed_time}")
                return False

            # If lapsed time is valid and greater than 0 seconds
            if lapsed_time:
                try:
                    # Break Loop once Played-Duration exceed
                    if lapsed_time >= timeout:
                        print(
                            f"Video has played for {lapsed_time} seconds. Pausing now.")
                        player.pauseVideo()
                        return True
                except ValueError:
                    print(f"Unable to parse lapsed time: {lapsed_time}")
                    return False
            time.sleep(0.5)

    def resumeVideo(self):
        # Resume paused video of JW-Player
        continueWatchingPage = ContinueWatching(self.driver)
        assert continueWatchingPage.isIn_ContinueWatchingPage(
        ), "Not in Continue Watching Page, Looks like video didnt pause"
        assert continueWatchingPage.is_VideoThumbnail_Displayed(), "Video Thumbail not displayed"
        assert continueWatchingPage.click_ContinueWatchingButton(
        ), "Unable to click on resume button"
        print("--------- User Successfully resumed video ---------")

    def changeVolume(self, volume):
        # Change Volume of JW-Player
        player = Player(self.driver)
        player.set_Player()  # Set the player
        assert player.setVolume(volume), "Unable to adjust volume"
        print(
            f"--------- User Successfully changed Volume to {volume} ---------")

    def changeResolution(self, resolution):
        # Change Resolution of Video
        player = Player(self.driver)
        player.set_Player()  # Set the player
        assert player.setResolution(resolution), "Unable to change resolution"
        print(
            f"--------- User Successfully changed Volume to {resolution} ---------")

    def pauseAndExitPlayer(self):
        # Pause and Exit from player
        player = Player(self.driver)
        continueWatchingPage = ContinueWatching(self.driver)
        player.set_Player()  # Set the player
        assert player.pauseVideo(), "Unable to Click on Pause"
        assert continueWatchingPage.isIn_ContinueWatchingPage(
        ), "Not in Continue Watching Page, Looks like video didnt pause"
        assert continueWatchingPage.click_BackButton(), "Unable to Click on Exit"
        print("--------- User Successfully paused and exited video player ---------")

    def signOut(self):
        # Sign out and verify user is in Dashboard
        dashboardPage = Dashboard(self.driver)
        videos = Videos(self.driver)
        loginPage = LoginPage(self.driver)
        assert videos.isIn_PlayVideoPage(), "Not In Video Page"
        assert dashboardPage.Click_SignOut(), "Unable to click on sign out"
        assert loginPage.isIn_IndeeLoginPage(), "Not In Login Page"
        print("--------- User Successfully signed out ---------")
