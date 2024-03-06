import pytest
import allure

from pages.account_page import AccountPage
from pages.login_page import LoginPage

from locators.account_page_locators import AccountLocators
from constants import Urls, User


class TestAccountPage:
    @allure.title("Проверяем переход в личный кабинет")
    def test_go_to_account(self, driver):
        login_page = LoginPage(driver)
        login_page.go_on_login_page(Urls.BASE_URL)
        login_page.fill_login_form(User.EMAIL, User.PASSWORD)
        login_page.click_on_account_button()
        account_page = AccountPage(driver)
        account_page.check_button_logout_is_visible()
        assert driver.current_url == Urls.ACCOUNT_URL

    @allure.title("Проверяем выход из ЛК")
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.go_on_login_page(Urls.BASE_URL)
        login_page.fill_login_form(User.EMAIL, User.PASSWORD)
        login_page.click_on_account_button()
        account_page = AccountPage(driver)
        account_page.click_on_logout_button()
        login_page.check_login_button_is_visible()
        assert driver.current_url == Urls.LOGIN_URL

