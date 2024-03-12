import pytest
import allure
from pages.site_page import SitePage
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from constants import Urls, User


class TestForgotPasswordPage:
    @allure.title("Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_forgot_password_page(self, driver):
        site_page = SitePage(driver)
        site_page.go_to_site(Urls.BASE_URL)
        site_page.click_on_account_button()
        login_page = LoginPage(driver)
        login_page.click_on_recovery_password()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.check_button_recovery_is_visible()
        assert forgot_password_page.get_current_url() == Urls.FORGOT_PASSWORD_URL
