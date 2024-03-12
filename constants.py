from selenium.webdriver.common.by import By


class Urls:
    BASE_URL = "https://stellarburgers.nomoreparties.site/"
    ACCOUNT_URL = "https://stellarburgers.nomoreparties.site/account/profile"
    FORGOT_PASSWORD_URL = "https://stellarburgers.nomoreparties.site/forgot-password"
    RESET_PASSWORD_URL = "https://stellarburgers.nomoreparties.site/reset-password"
    ORDER_HISTORY_URL = "https://stellarburgers.nomoreparties.site/account/order-history"
    LOGIN_URL = "https://stellarburgers.nomoreparties.site/login"
    ORDER_FEED_URL = "https://stellarburgers.nomoreparties.site/feed"


class User:
    NAME = "Korben"
    EMAIL = "korbendallas@yandex.ru"
    PASSWORD = "451289"


class Order:
    XPATH = By.XPATH
    NUMBER_IN_FEED = f"//p[text()='a']"
    NUMBER_IN_PROGRESS = f"//ul[2]/li[text()='a']"
