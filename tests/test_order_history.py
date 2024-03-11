import pytest
import allure
from pages.site_page import SitePage
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.order_history_page import OrderHistoryPage

from locators.account_page_locators import AccountLocators
from constants import Urls, User


class TestOrderHistoryPage:
    @allure.title("Проверяем переход в 'Историю заказов'")
    def test_go_to_order_history(self, driver):
        site_page = SitePage(driver)
        site_page.go_to_site(Urls.BASE_URL)
        site_page.click_on_account_button()
        login_page = LoginPage(driver)
        login_page.fill_login_form(User.EMAIL, User.PASSWORD)
        site_page.click_on_account_button()
        account_page = AccountPage(driver)
        account_page.click_on_order_history()
        order_history_page = OrderHistoryPage(driver)
        assert order_history_page.get_current_url(driver) == Urls.ORDER_HISTORY_URL
