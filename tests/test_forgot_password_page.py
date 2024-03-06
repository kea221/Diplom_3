import pytest
import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from constants import Urls, User


class TestForgotPasswordPage:
    @allure.title("Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_forgot_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.go_on_login_page(Urls.BASE_URL)
        login_page.click_on_recovery_password()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.check_button_recovery_is_visible()
        assert driver.current_url == Urls.FORGOT_PASSWORD_URL
