import pytest
import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginLocators


class LoginPage(BasePage):
    @allure.step("Кликнуть на ссылку 'Зарегистрироваться'")
    def click_on_link_register(self):
        return self.find_element(LoginLocators.LINK_TEXT_REGISTRATION).click()

    @allure.step("Кликнуть на кнопку 'Войти'")
    def click_on_login_button(self):
        return self.find_element(LoginLocators.LOGIN_BUTTON).click()

    @allure.step("Кликнуть на ссылку 'Восстановить пароль'")
    def click_on_recovery_password(self):
        return self.find_element(LoginLocators.RECOVER_PASSWORD).click()

    @allure.step("Ввести email")
    def enter_email(self, email):
        return self.find_element(LoginLocators.EMAIL_FIELD_LOG).send_keys(email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        return self.find_element(LoginLocators.PASSWORD_FIELD_LOG).send_keys(password)

    @allure.step("Заполнить форму для входа")
    def fill_login_form(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        return self.click_on_login_button()

    @allure.step("Найти кнопку 'Войти'")
    def check_login_button_is_visible(self):
        return self.find_element(LoginLocators.LOGIN_BUTTON)
