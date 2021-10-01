from selenium.webdriver.common.by import By


class Locators:
    BUTTON_LOGIN = (By.XPATH, "//a[@id='login2']")
    LOGIN_USER_NAME_FIELD = (By.XPATH, "//input[@id='loginusername']")
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@id='loginpassword']")
    BUTTON_LOGIN1 = (By.XPATH, "//button[contains(text(),'Log in')]")
    BUTTON_HOME = (By.XPATH, "//body/nav[@id='narvbarx']/div[@id='navbarExample']/ul[1]/li[1]/a[1]")
    BUTTON_CONTACT = (By.XPATH, "//a[contains(text(),'Contact')]")
    CONTACT_FIELD = (By.XPATH, "//input[@id='recipient-email']")
    CONTACT_NAME_FIELD = (By.XPATH, "//input[@id='recipient-name']")
    BUTTON_ABOUT_US = (By.XPATH, "//a[contains(text(),'About us')]")
    BUTTON_CLOSE = (By.XPATH, "//body/div[@id='videoModal']/div[1]/div[1]/div[3]/button[1]")
    BUTTON_CART = (By.XPATH, "//a[@id='cartur']")
    BUTTON_PLACE_ORDER = (By.XPATH, "//button[contains(text(),'Place Order')]")
    PLACE_ORDER_NAME_FIELD = (By.XPATH, "//input[@id='name']")
    PLACE_ORDER_COUNTRY_FIELD = (By.XPATH, "//input[@id='country']")
    PLACE_ORDER_CITY_FIELD = (By.XPATH, "//input[@id='city']")
    PLACE_ORDER_CREDIT_CARD_FIELD = (By.XPATH, "//input[@id='card']")
    PLACE_ORDER_MONTH = (By.XPATH, "//input[@id='month']")
    PLACE_ORDER_YEAR = (By.XPATH, "//input[@id='year']")
    BUTTON_PURCHASE = (By.XPATH, "//button[contains(text(),'Purchase')]")
    BUTTON_LOG_OUT = (By.XPATH, "//a[@id='logout2']")