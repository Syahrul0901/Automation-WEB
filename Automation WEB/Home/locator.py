from selenium.webdriver.common.by import By


class Locators: 
    BUTTON_HOME = (By.XPATH, "//body[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]")
    BUTTON_CONTACT = (By.XPATH, "//body[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]")
    BUTTON_ABOUT_US = (By.XPATH, "//body[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]")
    BUTTON_CART = (By.XPATH, "//body[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]")
    BUTTON_LOGIN = (By.XPATH, "//body[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]")
    BUTTON_SIGN_UP = (By.XPATH, "//body[1]/nav[1]/div[1]/ul[1]/li[8]/a[1]")