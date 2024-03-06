import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть сайт")
    def go_to_site(self, url):
        return self.driver.get(url)

    @allure.step("Нажать на кнопку 'Личный кабинет'")
    def click_on_account_button(self):
        return self.find_element(BasePageLocators.ACCOUNT_BUTTON).click()

    @allure.step("Дождаться появления элемента")
    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @allure.step("Перейти на страницу входа в ЛК")
    def go_on_login_page(self, url):
        self.go_to_site(url)
        return self.click_on_account_button()

    @allure.step("Получить атрибут элемента")
    def get_attribute(self, locator, attribute, time=3):
        element = self.find_element(locator, time)
        return element.get_attribute(attribute)

