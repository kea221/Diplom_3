import pytest
import allure
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.order_history_page import OrderHistoryPage

from locators.account_page_locators import AccountLocators
from constants import Urls, User


class TestOrderHistoryPage:
    @allure.title("Проверяем переход в 'Историю заказов'")
    def test_go_to_order_history(self, driver):
        login_page = LoginPage(driver)
        login_page.go_on_login_page(Urls.BASE_URL)
        login_page.fill_login_form(User.EMAIL, User.PASSWORD)
        login_page.click_on_account_button()
        account_page = AccountPage(driver)
        account_page.click_on_order_history()
        order_history_page = OrderHistoryPage(driver)
        order_history_page.check_order_history_div_is_visible()
        assert driver.current_url == Urls.ORDER_HISTORY_URL
