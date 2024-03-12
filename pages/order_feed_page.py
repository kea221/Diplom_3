import pytest
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators
from constants import Order


class OrderFeedPage(BasePage):
    @allure.step("Кликнуть на первый заказ в ленте")
    def click_on_first_order(self):
        return self.find_element(OrderFeedLocators.ORDER_FIRST).click()

    @allure.step("Получить атрибут элемента 'Модальное окно с деталями'")
    def get_attribute_modal_order_details(self):
        return self.get_attribute(OrderFeedLocators.MODAL_DETAILS_ORDER, "class")

    @allure.step("Кликнуть на кнопку закрытия модального окна")
    def click_on_cross_order_details(self):
        return self.find_element(OrderFeedLocators.CLOSE_DETAILS_ORDER).click()

    @allure.step("Найти кнопку закрытия модального окна")
    def check_cross_in_modal_is_visible(self):
        return self.find_element(OrderFeedLocators.CLOSE_DETAILS_ORDER)

    @allure.step("Получить число заказов за всё время")
    def get_number_of_counter_for_all_time(self):
        number = self.find_element(OrderFeedLocators.COUNTER_FOR_ALL_TIME).text
        return number

    @allure.step("Получить число заказов за сегодня")
    def get_number_of_counter_for_today(self):
        number = self.find_element(OrderFeedLocators.COUNTER_FOR_TODAY).text
        return number

    @allure.step("Найти на странице заголовок 'В работе'")
    def check_in_progress_is_visible(self):
        return self.find_element(OrderFeedLocators.IN_PROGRESS)

    @allure.step("Получить локатор для номера заказа в ленте")
    def get_locator_for_number_of_order_in_feed(self, number_from_history):
        new_xpath = Order.NUMBER_IN_FEED.replace("a", f"{number_from_history}")
        locator_number_in_feed = (Order.XPATH, new_xpath)
        return locator_number_in_feed

    @allure.step("Получить локатор для номера заказа из раздела В работе")
    def get_locator_for_number_of_order_in_progress(self, number_of_order):
        changed_xpath = Order.NUMBER_IN_PROGRESS.replace("a", f"{number_of_order}")
        locator_number_in_progress = (Order.XPATH, changed_xpath)
        return locator_number_in_progress
