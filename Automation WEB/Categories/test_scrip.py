from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

from Categories.Pages import CategoriesPage
from Categories.locator import Locators
from Categories.Testdata import TestData


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

class CategoriesTest(BaseTest):
    def test_categories_valid(self):
        self.categories_page = CategoriesPage(self.driver)
        self.categories_page.categories_valid()
        time.sleep(3)

    def test_phones_valid(self):
        self.categories_page = CategoriesPage(self.driver)
        self.categories_page.phones_valid()
        time.sleep(3)

    def test_laptops_valid(self):
        self.categories_page = CategoriesPage(self.driver)
        self.categories_page.laptops_valid()
        time.sleep(3)

    def test_monitors_valid(self):
        self.categories_page = CategoriesPage(self.driver)
        self.categories_page.monitors_valid()
        time.sleep(3)
