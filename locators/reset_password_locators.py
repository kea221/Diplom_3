from selenium.webdriver.common.by import By


class ResetPasswordLocators:
    # SAVE_BUTTON - кнопка "Сохранить"
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")
    # PASSWORD_FIELD - поле ввода пароля с рамкой
    PASSWORD_FIELD = (By.XPATH, "//div[@class='input__icon input__icon-action']/parent::*")
    # SHOW_HIDE_PASSWORD - иконка показать/скрыть пароль
    SHOW_HIDE_PASSWORD = (By.XPATH, "//div[@class='input__icon input__icon-action']/child::*")
