from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    # RECOVERY_BUTTON - кнопка "Восстановить"
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    # EMAIL_FIELD - поле для ввода email
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
