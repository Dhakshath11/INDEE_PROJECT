import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from tests.utils.indeeUtility import indeeUtility

"""
Executable Class if User wish to start execution from PyTest
"""

@pytest.fixture(scope="function")
def driver():
    try:
         # driver_path = ChromeDriverManager().install()
        driver_path = "./chromedriver.exe"

        # Setting Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")  # Opening Chrome in maximum resolution

        # Setting up ChromeDriver using WebDriver Manager
        service = Service(driver_path)

        # Launching Chrome browser
        driver = webdriver.Chrome(service=service, options=chrome_options)

        yield driver  # Yield the driver to the test

        # Close the browser after the test
        driver.close()
        driver.quit()
    except Exception as e:
        print(f"Failure : {e}")

#Start Test Run From here
def test_indee(driver: webdriver.Chrome):
    try:
        utility = indeeUtility(driver)
        # Navigate to the Indee TV URL
        assert utility.navigate("https://indeedemo-fyc.watch.indee.tv/"), "Navigation failed"
        utility.signInToIndee("WVMVHWBS")
        utility.navigateToVideo()
        utility.switchToDetailsSection()
        utility.switchToVideoSection()
        utility.playPauseVideo(10)
        utility.resumeVideo()
        utility.changeVolume(50)
        utility.changeResolution("480p")
        utility.pauseAndExitPlayer()
        utility.signOut()

    except Exception as e:
        print(f"Error during test: {e}")
        pytest.fail("Test failed unexpectedly")
