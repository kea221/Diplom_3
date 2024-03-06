import pytest
import allure
from pages.base_page import BasePage
from locators.order_history_locators import OrderHistoryLocators


class OrderHistoryPage(BasePage):
    @allure.step("Найти на странице список заказов")
    def check_order_history_div_is_visible(self):
        return self.find_element(OrderHistoryLocators.ORDER_HISTORY_DIV)

    @allure.step("Получить номер последнего заказа")
    def get_number_of_last_order(self):
        number_of_order = self.find_element(OrderHistoryLocators.NUMBER_OF_LAST_ORDER).text
        return number_of_order
