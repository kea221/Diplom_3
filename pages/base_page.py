import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть сайт")
    def go_to_site(self, url):
        return self.driver.get(url)

    @allure.step("Дождаться появления элемента")
    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @allure.step("Получить атрибут элемента")
    def get_attribute(self, locator, attribute, time=3):
        element = self.find_element(locator, time)
        return element.get_attribute(attribute)

    @allure.step("Убедиться, что элемент кликабельный")
    def check_element_clicable(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    @allure.step("Захватить и переместить элемент")
    def drag_and_drop_element(self, drag_locator, drop_locator):
        drag = self.find_element(drag_locator)
        drop = self.find_element(drop_locator)
        return ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    @allure.step("Получить текущий урл")
    def get_current_url(self):
        return self.driver.current_url
