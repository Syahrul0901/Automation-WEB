from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains

    def alert_js(self):
        WebDriverWait(self.driver, 3000).until(
            EC.alert_is_present()
        )

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()
