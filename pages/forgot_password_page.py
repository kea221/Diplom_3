import pytest
import allure
from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):
    @allure.step("Найти на странице кнопку 'Восстановить'")
    def check_button_recovery_is_visible(self):
        return self.find_element(ForgotPasswordLocators.RECOVERY_BUTTON)

    @allure.step("Ввести email в поле ввода")
    def enter_email(self, email):
        return self.find_element(ForgotPasswordLocators.EMAIL_FIELD).send_keys(email)

    @allure.step("Кликнуть по кнопке 'Восстановить'")
    def click_on_recovery_button(self):
        return self.find_element(ForgotPasswordLocators.RECOVERY_BUTTON).click()
