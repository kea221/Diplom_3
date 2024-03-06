from selenium.webdriver.common.by import By


class BasePageLocators:
    # ACCOUNT_BUTTON - кнопка "Личный Кабинет"
    ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")
    # CONSTRUCTOR - кнопка "Конструктор"
    CONSTRUCTOR = (By.XPATH, "//nav//li/a[@href='/']")
    # ORDER_FEED -кнопка "Лента заказов"
    ORDER_FEED = (By.XPATH, "//a[@href='/feed']/p")
