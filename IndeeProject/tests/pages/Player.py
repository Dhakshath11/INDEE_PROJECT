
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as wait
import time


class Player:
    """
    POM Class of Video Player
    This class-method is mostly executed by JavaScripts

    Attributes:
        attribute1 (driver): Chrome WebDriver
    """

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

    def set_Player(self):
        """
        Set_Player Method : 
        Browser plays video in JWPlayer, which is present inside iframe.
        Driver needs to be switched into iframe and explicit-wait is used to dynamically wait until JW-Player is ready
        """
        try:
            # Switch Inside iframe
            iframe = WebDriverWait(self.driver, 10).until(
                wait.presence_of_element_located((By.CSS_SELECTOR, "iframe#video_player")))
            self.driver.switch_to.frame(iframe)

            # Wait until JW-Player is defined as it is load dynamically
            player_ready = WebDriverWait(self.driver, 20).until(
                lambda driver: driver.execute_script("return (typeof jwplayer !== 'undefined' && typeof jwplayer === 'function');"))

            if player_ready:
                print("--> JWPlayer is ready.")
                # Wait until the loading spinner disappears
                WebDriverWait(self.driver, 10).until(
                    wait.invisibility_of_element_located((By.CSS_SELECTOR, '.jw-icon-display[aria-label="Loading"]')))
                print("--> Player is ready and loading screen disappeared.")

                # Implicit-Wait for Smooth Execution (:TODO Optional - Can be removed)
                time.sleep(1)
                return True
            else:
                print("--> JWPlayer is not loaded.")
                return False
        except Exception as e:
            print(f"Oops..!! Error while setting video player. {e}")
            return False

    def pauseVideo(self):
        # To Pause the JW-Player
        try:
            self.driver.execute_script("jwplayer().pause(true);")
            state = self.driver.execute_script("return jwplayer().getState();")
            # Wait until the player state is 'PAUSED'
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.execute_script(
                    "return jwplayer().getState();") == 'paused'
            )
            print("--> Paused the player.")
            return True
        except Exception as e:
            print(f"Oops..!! Video didn't pause. {e}")
            return False

    def playVideo(self):
        # To Play the JW-Player
        try:
            self.driver.execute_script("jwplayer().play(true);")
            state = self.driver.execute_script("return jwplayer().getState();")
            # Wait until the player state is 'PLAYING'
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.execute_script(
                    "return jwplayer().getState();") == 'playing'
            )
            print("--> Playing the player.")
            return True
        except Exception as e:
            print(f"Oops..!! Video didn't play. {e}")
            return False

    def setVolume(self, volume_level):
        """
        Attributes: Integer value from 1 to 100
        """
        # To Set Volume the JW-Player
        try:
            self.driver.execute_script(
                f"jwplayer().setVolume({volume_level});")
            # Wait until the volume is set (optional: you can validate this with some custom JavaScript)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.execute_script(
                    f"return jwplayer().getVolume();") == volume_level
            )
            print(f"--> Set volume to {volume_level}%.")
            return True
        except Exception as e:
            print(f"Oops..!! Volume didn't set. {e}")
            return False

    def setResolution(self, resolution_level):
        """
        Attributes: Resolution value : Auto, 320p, 480p 720p
        """
        # To Change Resolution of Video
        try:
            # Get the available reslution quality levels
            quality_levels = self.driver.execute_script(
                "return jwplayer().getQualityLevels();")
            print("--> Available quality levels:", quality_levels)

            # Find the index for the desired resolution quality label
            quality_index = next((i for i, q in enumerate(
                quality_levels) if q['label'] == resolution_level), None)

            if quality_index is not None:
                self.driver.execute_script(
                    f"jwplayer().setCurrentQuality({quality_index});")

                # Wait until the quality is set
                WebDriverWait(self.driver, 10).until(
                    lambda driver: driver.execute_script(
                        "return jwplayer().getCurrentQuality();") == quality_index
                )
                print(f"--> Set quality to {resolution_level}.")
                return True
            else:
                print(f"--> Quality label '{resolution_level}' not found.")
                return False
        except Exception as e:
            print(f"Oops..!! Resolution didn't set. {e}")
            return False

    def getLapsedTime(self):
        # To get duration of Video played
        try:
            # Get the current elapsed time from the player
            elapsed_time = self.driver.execute_script(
                "return jwplayer().getPosition();")
            print(f"--> Elapsed time: {elapsed_time} seconds")
            return elapsed_time
        except Exception as e:
            print(f"Oops..!! Error getting video lapsed time. {e}")
            return -1
