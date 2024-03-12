import pytest
import allure
from pages.base_page import BasePage
from locators.register_page_locators import RegisterLocators


class RegisterPage(BasePage):
    @allure.step("Ввести Имя в форме регистрации")
    def enter_name(self, name):
        return self.find_element(RegisterLocators.NAME_FIELD_REG).send_keys(name)

    @allure.step("Ввести Email в форме регистрации")
    def enter_email(self, email):
        return self.find_element(RegisterLocators.EMAIL_FIELD_REG).send_keys(email)

    @allure.step("Ввести Пароль в форме регистрации")
    def enter_password(self, password):
        return self.find_element(RegisterLocators.PASSWORD_FIELD_REG).send_keys(password)

    @allure.step("Кликнуть на кнопку 'Зарегистрироваться'")
    def click_register_button(self):
        return self.find_element(RegisterLocators.REGISTER).click()

    @allure.step("Зарегистрировать пользователя")
    def register_user(self, name, email, password):
        self.enter_name(name)
        self.enter_email(email)
        self.enter_password(password)
        return self.click_register_button()

