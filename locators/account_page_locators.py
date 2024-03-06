from selenium.webdriver.common.by import By


class AccountLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_HISTORY = (By.XPATH, "//a[@href='/account/order-history']")
