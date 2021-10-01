from selenium.webdriver.common.by import By


class Locators: 
    BUTTON_CATEGORIES = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[1]/a[1]")
    BUTTON_PHONES = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[1]/a[2]")
    BUTTON_LAPTOPS = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[1]/a[3]")
    BUTTON_MONITORS = (By.XPATH, "//body[1]/div[5]/div[1]/div[1]/div[1]/a[4]")