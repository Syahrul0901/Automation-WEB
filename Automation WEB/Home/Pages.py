import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Home.Testdata import TestData
from Home.locator import Locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains

    def move_element_to(self, locator):
        hover = self.driver.find_element_by_xpath(locator)
        self.action.move_to_element(hover).perform()

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

class HomePage(BasePage) :
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def home_valid(self):
        self.click(Locators.BUTTON_HOME) 

    def contact_valid(self):
        self.click(Locators.BUTTON_CONTACT)

    def about_us_valid(self):
        self.click(Locators.BUTTON_ABOUT_US)

    def cart_valid(self):
        self.click(Locators.BUTTON_CART)

    def login_valid(self):
        self.click(Locators.BUTTON_LOGIN)

    def sign_up_valid(self):
        self.click(Locators.BUTTON_SIGN_UP)