from selenium.webdriver.common.by import By


class LoginLocators:
    # LINK_TEXT_REGISTRATION - текстовая ссылка "Зарегистрироваться" на странице входа
    LINK_TEXT_REGISTRATION = (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/register']")
    # LOGIN_BUTTON - кнопка "Войти" в форме входа
    LOGIN_BUTTON = (By.XPATH, "//form[@class]/button")
    # RECOVER_PASSWORD - текстовая ссылка "Восстановить пароль"
    RECOVER_PASSWORD = (By.XPATH, "//a[@href='/forgot-password']")
    # EMAIL_FIELD_LOG - поле ввода Email в форме для входа
    EMAIL_FIELD_LOG = (By.XPATH, "//input[@name='name']")
    # PASSWORD_FIELD_LOG - поле ввода Пароля в форме для входа
    PASSWORD_FIELD_LOG = (By.XPATH, "//input[@type='password']")
