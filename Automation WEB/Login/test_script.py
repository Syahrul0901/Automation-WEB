from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

from Login.Pages import LoginPage
from Login.locator import Locators
from Login.Testdata import TestData


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

class LoginTest(BaseTest):

    def test_login_valid(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.login_valid()
        time.sleep(4)

    def test_click_button_home(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.click_button_home()
        time.sleep(4)

    def test_click_button_contact(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.click_button_contact()
        time.sleep(4)

    def test_click_button_about_us(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.click_button_about_us()
        time.sleep(4)

    def test_click_button_cart(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.click_button_cart()
        time.sleep(4)

    def test_click_button_log_out(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.click_button_log_out()
        time.sleep(4)
    