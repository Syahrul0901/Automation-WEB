from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

from Home.Pages import HomePage
from Home.locator import Locators
from Home.Testdata import TestData


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

class HomeTest(BaseTest):

    def test_home_valid(self):
        self.home_page = HomePage(self.driver)
        self.home_page.home_valid()
        time.sleep(3)

    def test_contact_valid(self):
        self.home_page = HomePage(self.driver)
        self.home_page.contact_valid()
        time.sleep(3)

    def test_about_us_valid(self):
        self.home_page = HomePage(self.driver)
        self.home_page.about_us_valid()
        time.sleep(3)

    def test_cart_valid(self):
        self.home_page = HomePage(self.driver)
        self.home_page.cart_valid()
        time.sleep(4)

    def test_login_valid(self):
        self.home_page = HomePage(self.driver)
        self.home_page.login_valid()
        time.sleep(4)

    def test_sign_up_valid(self):
        self.home_page = HomePage(self.driver)
        self.home_page.sign_up_valid()
        time.sleep(3)
