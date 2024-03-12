from selenium.webdriver.common.by import By


class RegisterLocators:
    # NAME_FIELD_REG - поле ввода Имени в форме регистрации
    NAME_FIELD_REG = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # EMAIL_FIELD_REG - поле ввода Email в форме регистрации
    EMAIL_FIELD_REG = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # PASSWORD_FIELD_REG - поле ввода пароля в форме регистрации
    PASSWORD_FIELD_REG = (By.XPATH, "//input[@type='password']")
    # REGISTER - кнопка "Зарегистрироваться" на экране регистрации
    REGISTER = (By.CSS_SELECTOR, "button.button_button__33qZ0")
