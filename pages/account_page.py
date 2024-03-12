import pytest
import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountLocators


class AccountPage(BasePage):
    @allure.step("Найти на странице кнопку 'Выход'")
    def check_button_logout_is_visible(self):
        return self.find_element(AccountLocators.LOGOUT_BUTTON)

    @allure.step("Кликнуть на 'Историю заказов'")
    def click_on_order_history(self):
        return self.find_element(AccountLocators.ORDER_HISTORY).click()

    @allure.step("Кликнуть на кнопку 'Выход'")
    def click_on_logout_button(self):
        return self.find_element(AccountLocators.LOGOUT_BUTTON).click()
