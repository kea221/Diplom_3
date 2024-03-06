import time

import pytest
import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from constants import Urls, User


class TestResetPasswordPage:
    @allure.title("Проверяем переход на страницу установки нового пароля")
    def test_go_to_reset_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.go_on_login_page(Urls.BASE_URL)
        login_page.click_on_recovery_password()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.enter_email(User.EMAIL)
        forgot_password_page.click_on_recovery_button()
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.check_button_save_is_visible()
        assert driver.current_url == Urls.RESET_PASSWORD_URL

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_click_on_show_password_makes_field_active(self, driver):
        login_page = LoginPage(driver)
        login_page.go_on_login_page(Urls.BASE_URL)
        login_page.click_on_recovery_password()
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.enter_email(User.EMAIL)
        forgot_password_page.click_on_recovery_button()
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.click_on_hide_icon()
        assert "input_status_active" in reset_password_page.get_attribute_new_password_field()
