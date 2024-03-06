import pytest
import allure
from pages.base_page import BasePage
from locators.reset_password_locators import ResetPasswordLocators


class ResetPasswordPage(BasePage):
    @allure.step("Найти на странице кнопку 'Сохранить'")
    def check_button_save_is_visible(self):
        return self.find_element(ResetPasswordLocators.SAVE_BUTTON)

    @allure.step("Кликнуть на иконку глаза")
    def click_on_hide_icon(self):
        return self.find_element(ResetPasswordLocators.SHOW_HIDE_PASSWORD).click()

    @allure.step("Получить атрибут элемента 'Поле ввода нового пароля'")
    def get_attribute_new_password_field(self):
        return self.get_attribute(ResetPasswordLocators.PASSWORD_FIELD, "class")
