import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Login.Testdata import TestData
from Login.locator import Locators


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

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def login_valid(self):
        self.click(Locators.BUTTON_LOGIN)
        time.sleep(2)
        self.enter_text(Locators.LOGIN_USER_NAME_FIELD, TestData.LOGIN_USER_NAME)
        time.sleep(2)
        self.enter_text(Locators.LOGIN_PASSWORD_FIELD, TestData.LOGIN_PASSWORD)
        time.sleep(2)
        self.click(Locators.BUTTON_LOGIN1)
        time.sleep(2)

    def click_button_home(self):
        self.click(Locators.BUTTON_LOGIN)
        self.enter_text(Locators.LOGIN_USER_NAME_FIELD, TestData.LOGIN_USER_NAME)
        time.sleep(2)
        self.enter_text(Locators.LOGIN_PASSWORD_FIELD, TestData.LOGIN_PASSWORD)
        time.sleep(2)
        self.click(Locators.BUTTON_LOGIN1)
        time.sleep(2)
        self.click(Locators.BUTTON_HOME)
        time.sleep(3)

    def click_button_contact(self):
        self.click(Locators.BUTTON_LOGIN)
        self.enter_text(Locators.LOGIN_USER_NAME_FIELD, TestData.LOGIN_USER_NAME)
        time.sleep(2)
        self.enter_text(Locators.LOGIN_PASSWORD_FIELD, TestData.LOGIN_PASSWORD)
        time.sleep(2)
        self.click(Locators.BUTTON_LOGIN1)
        time.sleep(2)
        self.click(Locators.BUTTON_CONTACT)
        time.sleep(2)
        self.enter_text(Locators.CONTACT_FIELD, TestData.CONTACT_DATA)
        time.sleep(2)
        self.enter_text(Locators.CONTACT_NAME_FIELD, TestData.CONTACT_NAME_DATA)
        time.sleep(2)

    def click_button_about_us(self):
        self.click(Locators.BUTTON_LOGIN)
        self.enter_text(Locators.LOGIN_USER_NAME_FIELD, TestData.LOGIN_USER_NAME)
        time.sleep(2)
        self.enter_text(Locators.LOGIN_PASSWORD_FIELD, TestData.LOGIN_PASSWORD)
        time.sleep(2)
        self.click(Locators.BUTTON_LOGIN1)
        time.sleep(2)
        self.click(Locators.BUTTON_ABOUT_US)
        time.sleep(3)
        self.click(Locators.BUTTON_CLOSE)
        time.sleep(2)

    def click_button_cart(self):
        self.click(Locators.BUTTON_LOGIN)
        self.enter_text(Locators.LOGIN_USER_NAME_FIELD, TestData.LOGIN_USER_NAME)
        time.sleep(2)
        self.enter_text(Locators.LOGIN_PASSWORD_FIELD, TestData.LOGIN_PASSWORD)
        time.sleep(2)
        self.click(Locators.BUTTON_LOGIN1)
        time.sleep(2)
        self.click(Locators.BUTTON_CART)
        time.sleep(2)
        self.click(Locators.BUTTON_PLACE_ORDER)
        time.sleep(2)
        self.enter_text(Locators.PLACE_ORDER_NAME_FIELD, TestData.PLACE_ORDER_NAME)
        time.sleep(2)
        self.enter_text(Locators.PLACE_ORDER_COUNTRY_FIELD, TestData.PLACE_ORDER_COUNTRY)
        time.sleep(2)
        self.enter_text(Locators.PLACE_ORDER_CITY_FIELD, TestData.PLACE_ORDER_CITY)
        time.sleep(2)
        self.enter_text(Locators.PLACE_ORDER_CREDIT_CARD_FIELD, TestData.PLACE_ORDER_CREDIT_CARD)
        time.sleep(2)
        self.enter_text(Locators.PLACE_ORDER_MONTH, TestData.PLACE_ORDER_MONTH)
        time.sleep(2)
        self.enter_text(Locators.PLACE_ORDER_YEAR, TestData.PLACE_ORDER_YEAR)
        time.sleep(2)
        self.click(Locators.BUTTON_PURCHASE)

    def click_button_log_out(self):
        self.click(Locators.BUTTON_LOGIN)
        self.enter_text(Locators.LOGIN_USER_NAME_FIELD, TestData.LOGIN_USER_NAME)
        time.sleep(2)
        self.enter_text(Locators.LOGIN_PASSWORD_FIELD, TestData.LOGIN_PASSWORD)
        time.sleep(2)
        self.click(Locators.BUTTON_LOGIN1)
        time.sleep(3)
        self.click(Locators.BUTTON_LOG_OUT)