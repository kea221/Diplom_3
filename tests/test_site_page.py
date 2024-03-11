import pytest
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.site_page import SitePage
from pages.login_page import LoginPage
from constants import Urls, User
from locators.site_page_locators import SitePageLocators


class TestSitePage:
    @allure.title("Проверяем переход на 'Конструктор'")
    @pytest.mark.parametrize("url", [Urls.BASE_URL,
                                     Urls.LOGIN_URL,
                                     Urls.RESET_PASSWORD_URL,
                                     Urls.FORGOT_PASSWORD_URL])
    def test_go_to_constructor(self, driver, url):
        site_page = SitePage(driver)
        site_page.go_to_site(Urls.BASE_URL)
        site_page.click_on_account_button()
        login_page = LoginPage(driver)
        login_page.fill_login_form(User.EMAIL, User.PASSWORD)
        site_page.check_order_button_is_visible()
        site_page.go_to_site(url)
        site_page.click_on_constructor()
        assert site_page.get_current_url(driver) == Urls.BASE_URL

    @allure.title("Проверяем переход на 'Ленту заказов'")
    @pytest.mark.parametrize("url", [Urls.BASE_URL,
                                     Urls.LOGIN_URL,
                                     Urls.RESET_PASSWORD_URL,
                                     Urls.FORGOT_PASSWORD_URL])
    def test_go_to_order_feed(self, driver, url):
        site_page = SitePage(driver)
        site_page.go_to_site(Urls.BASE_URL)
        site_page.click_on_account_button()
        login_page = LoginPage(driver)
        login_page.fill_login_form(User.EMAIL, User.PASSWORD)
        site_page.check_order_button_is_visible()
        site_page.go_to_site(url)
        site_page.click_on_order_feed()
        assert site_page.get_current_url(driver) == Urls.ORDER_FEED_URL

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_appears_modal_with_details(self, driver):
        site_page = SitePage(driver)
        site_page.go_to_site(Urls.BASE_URL)
        site_page.click_on_account_button()
        login_page = LoginPage(driver)
        login_page.fill_login_form(User.EMAIL, User.PASSWORD)
        site_page.click_on_crater_bun()
        site_page.check_cross_in_modal_is_visible()
        assert "Modal_modal_opened__3ISw4" in site_page.get_attribute_modal_ingredient_details()

    @allure.title("Всплывающее окно с деталями закрывается кликом по крестику")
    def test_modal_window_closed_by_click_on_cross(self, driver):
        site_page = SitePage(driver)
        site_page.go_to_site(Urls.BASE_URL)
        site_page.click_on_account_button()
        login_page = LoginPage(driver)
        login_page.fill_login_form(User.EMAIL, User.PASSWORD)
        site_page.click_on_crater_bun()
        site_page.click_on_cross_in_modal()
        site_page.check_crater_bun_is_visible()
        assert "Modal_modal_opened__3ISw4" not in site_page.get_attribute_modal_ingredient_details()

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается")
    def test_ingredient_counter_increases(self, driver):
        site_page = SitePage(driver)
        site_page.go_to_site(Urls.BASE_URL)
        value_default = site_page.get_counter_value()
        site_page.add_bun_in_order()
        new_value = site_page.get_counter_value()
        assert new_value > value_default

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_authorized_user_can_place_order(self, driver):
        site_page = SitePage(driver)
        site_page.go_to_site(Urls.BASE_URL)
        site_page.click_on_account_button()
        login_page = LoginPage(driver)
        login_page.fill_login_form(User.EMAIL, User.PASSWORD)
        site_page.collect_burger()
        assert site_page.find_element(SitePageLocators.ORDER_ID)
