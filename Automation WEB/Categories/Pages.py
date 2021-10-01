import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Categories.Testdata import TestData
from Categories.locator import Locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains

    # function input data
    def enter_text(self, locator, teks):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).send_keys(teks)

    def get_text(self, locator):

        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).text

    # function click Locator
    def move_element_to(self, locator):
        hover = self.driver.find_element_by_xpath(locator)
        self.action.move_to_element(hover).perform()

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

class CategoriesPage(BasePage) :
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def categories_valid(self):
        self.click(Locators.BUTTON_CATEGORIES)

    def phones_valid(self):
        self.click(Locators.BUTTON_PHONES)

    def laptops_valid(self):
        self.click(Locators.BUTTON_LAPTOPS)

    def monitors_valid(self):
        self.click(Locators.BUTTON_MONITORS)