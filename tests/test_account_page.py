import pytest
import allure

from pages.site_page import SitePage
from pages.account_page import AccountPage
from pages.login_page import LoginPage

from locators.account_page_locators import AccountLocators
from constants import Urls, User


class TestAccountPage:
    @allure.title("Проверяем переход в личный кабинет")
    def test_go_to_account(self, driver):
        site_page = SitePage(driver)
        site_page.go_to_site(Urls.BASE_URL)
        site_page.click_on_account_button()
        login_page = LoginPage(driver)
        login_page.fill_login_form(User.EMAIL, User.PASSWORD)
        site_page.click_on_account_button()
        account_page = AccountPage(driver)
        account_page.check_button_logout_is_visible()
        assert account_page.get_current_url(driver) == Urls.ACCOUNT_URL

    @allure.title("Проверяем выход из ЛК")
    def test_logout(self, driver):
        site_page = SitePage(driver)
        site_page.go_to_site(Urls.BASE_URL)
        site_page.click_on_account_button()
        login_page = LoginPage(driver)
        login_page.fill_login_form(User.EMAIL, User.PASSWORD)
        site_page.click_on_account_button()
        account_page = AccountPage(driver)
        account_page.click_on_logout_button()
        login_page.check_login_button_is_visible()
        assert login_page.get_current_url(driver) == Urls.LOGIN_URL
