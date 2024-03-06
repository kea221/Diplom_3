import pytest
import allure

from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.site_page_locators import SitePageLocators

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class SitePage(BasePage):
    @allure.step("Кликнуть на 'Конструктор'")
    def click_on_constructor(self):
        return self.find_element(BasePageLocators.CONSTRUCTOR).click()

    @allure.step("Найти на странице кнопку 'Оформить заказ'")
    def check_order_button_is_visible(self):
        return self.find_element(SitePageLocators.ORDER_BUTTON)

    @allure.step("Кликнуть на 'Ленту заказов'")
    def click_on_order_feed(self):
        return self.find_element(BasePageLocators.ORDER_FEED).click()

    @allure.step("Кликнуть на кратерную булку")
    def click_on_crater_bun(self):
        return self.find_element(SitePageLocators.CRATER_BUN).click()

    @allure.step("Убедиться в видимости кратерной булки")
    def check_crater_bun_is_visible(self):
        return self.find_element(SitePageLocators.CRATER_BUN)

    @allure.step("Убедиться, что кнопка закрытия модального окна кликабельна")
    def check_cross_in_modal_is_visible(self):
        return WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(SitePageLocators.CLOSE_DETAILS))

    @allure.step("Получить атрибут элемента 'Модальное окно с деталями ингредиента'")
    def get_attribute_modal_ingredient_details(self):
        return self.get_attribute(SitePageLocators.MODAL_DETAILS, "class")

    @allure.step("Кликнуть на крестик закрытия окна с деталями")
    def click_on_cross_in_modal(self):
        return self.find_element(SitePageLocators.CLOSE_DETAILS).click()

    @allure.step("Переместить кратерную булку в заказ")
    def add_bun_in_order(self):
        drag = self.find_element(SitePageLocators.CRATER_BUN)
        drop = self.find_element(SitePageLocators.BURGER_CONSTRUCTOR)
        return ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    @allure.step("Получить значение счётчика кратерной булки")
    def get_counter_value(self):
        value = self.find_element(SitePageLocators.COUNTER_CRATER_BUN).text
        return value

    @allure.step("Кликнуть на раздел Начинки")
    def click_on_fillings(self):
        return self.find_element(SitePageLocators.FILLINGS).click()

    @allure.step("Переместить биокотлету в заказ")
    def add_filling_in_order(self):
        drag = self.find_element(SitePageLocators.BIO_CUTLET)
        drop = self.find_element(SitePageLocators.BURGER_CONSTRUCTOR)
        return ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    @allure.step("Кликнуть на раздел 'Соусы'")
    def click_on_sauces(self):
        return self.find_element(SitePageLocators.SAUCES).click()

    @allure.step("Переместить соус 'Spicy-X' в заказ")
    def add_sauce_in_order(self):
        drag = self.find_element(SitePageLocators.SPICY_X_SAUCE)
        drop = self.find_element(SitePageLocators.BURGER_CONSTRUCTOR)
        return ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    @allure.step("Кликнуть на кнопку 'Оформить заказ'")
    def click_on_order_button(self):
        return self.find_element(SitePageLocators.ORDER_BUTTON).click()

    @allure.step("Собрать бургер")
    def collect_burger(self):
        self.add_bun_in_order()
        self.click_on_fillings()
        self.add_filling_in_order()
        self.click_on_sauces()
        self.add_sauce_in_order()
        return self.click_on_order_button()

    @allure.step("Собрать бургер и перейти на Ленту заказов")
    def collect_burger_go_on_order_feed(self):
        self.collect_burger()
        self.check_cross_in_modal_is_visible()
        self.click_on_cross_in_modal()

        return self.click_on_order_feed()

    @allure.step("Получить номер заказа из модального окна, появляющегося после оформления заказа")
    def get_number_of_order_from_modal(self):
        number = self.find_element(SitePageLocators.NUMBER_OF_ORDER).text
        return number
