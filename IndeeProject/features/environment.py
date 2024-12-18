from selenium import webdriver
from selenium.webdriver.chrome.service import Service

"""
    THIS FILE IS USED FROM DRIVER CREATION, STARTING & STOPING BROWSER SESSION.
"""


def before_scenario(context, scenario):
    """
    To create Chrome Driver session
    """
    try:
        # driver_path = ChromeDriverManager().install()
        driver_path = "./chromedriver.exe"
        service = Service(driver_path)
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        context.driver = webdriver.Chrome(service=service, options=options)
        print("----------** DRIVER INITIATED **------------")

    except Exception as e:
        print(f"Driver Not Initiated: {e}")
        context.driver = None
        raise e


def after_scenario(context, scenario):
    """
    To Close Chrome Driver session
    """
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
        print("----------**  Browser closed **------------")
    else:
        print(" >>>>> Driver was not initialized <<<<<")
