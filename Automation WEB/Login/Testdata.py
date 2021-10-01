from faker import Faker


class TestData:
    fake = Faker(["id_ID"])

    BASE_URL = "https://www.demoblaze.com"

    LOGIN_USER_NAME = 'Gakpunya@gmail.com'
    LOGIN_PASSWORD = '7654321'
    CONTACT_DATA = 'Punya@gmail.com'
    CONTACT_NAME_DATA = 'Hanya test saja'
    PLACE_ORDER_NAME = 'Hanya Test'
    PLACE_ORDER_COUNTRY = 'INDONESIA'
    PLACE_ORDER_CITY = 'BANTEN'
    PLACE_ORDER_CREDIT_CARD = '112234567'
    PLACE_ORDER_MONTH = 'FEBRUARY'
    PLACE_ORDER_YEAR = '2020'