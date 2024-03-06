import pytest
import allure
from pages.site_page import SitePage
from pages.login_page import LoginPage
from pages.order_feed_page import OrderFeedPage
from pages.account_page import AccountPage
from pages.order_history_page import OrderHistoryPage
from constants import Urls, User
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestOrderFeedPage:
    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_appears_modal_with_details_order(self, driver):
        site_page = SitePage(driver)
        site_page.go_on_login_page(Urls.BASE_URL)
        login_page = LoginPage(driver)
        login_page.fill_login_form(User.EMAIL, User.PASSWORD)
        site_page.collect_burger_go_on_order_feed()
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.click_on_first_order()
        order_feed_page.check_cross_in_modal_is_visible()
        assert "Modal_modal_opened__3ISw4" in order_feed_page.get_attribute_modal_order_details()

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_orders_from_order_history_displayed_in_order_feed(self, driver):
        site_page = SitePage(driver)
        site_page.go_on_login_page(Urls.BASE_URL)
        login_page = LoginPage(driver)
        login_page.fill_login_form(User.EMAIL, User.PASSWORD)
        site_page.collect_burger_go_on_order_feed()
        site_page.click_on_account_button()
        account_page = AccountPage(driver)
        account_page.click_on_order_history()
        order_history_page = OrderHistoryPage(driver)
        number_from_history = order_history_page.get_number_of_last_order()
        site_page.click_on_order_feed()
        locator_number_in_feed = (By.XPATH, f"//p[text()='{number_from_history}']")
        assert WebDriverWait(driver, 3).until(EC.presence_of_element_located(locator_number_in_feed))

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_counter_for_all_time_increases_when_new_order_created(self, driver):
        site_page = SitePage(driver)
        site_page.go_on_login_page(Urls.BASE_URL)
        login_page = LoginPage(driver)
        login_page.fill_login_form(User.EMAIL, User.PASSWORD)
        site_page.click_on_order_feed()
        order_feed_page = OrderFeedPage(driver)
        number_counter = order_feed_page.get_number_of_counter_for_all_time()
        site_page.click_on_constructor()
        site_page.collect_burger_go_on_order_feed()
        number_changed = order_feed_page.get_number_of_counter_for_all_time()
        assert number_changed > number_counter

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_counter_for_today_increases_when_new_order_created(self, driver):
        site_page = SitePage(driver)
        site_page.go_on_login_page(Urls.BASE_URL)
        login_page = LoginPage(driver)
        login_page.fill_login_form(User.EMAIL, User.PASSWORD)
        site_page.click_on_order_feed()
        order_feed_page = OrderFeedPage(driver)
        number_counter = order_feed_page.get_number_of_counter_for_today()
        site_page.click_on_constructor()
        site_page.collect_burger_go_on_order_feed()
        number_changed = order_feed_page.get_number_of_counter_for_today()
        assert number_changed > number_counter

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_number_of_order_appears_in_section_in_progress(self, driver):
        site_page = SitePage(driver)
        site_page.go_on_login_page(Urls.BASE_URL)
        login_page = LoginPage(driver)
        login_page.fill_login_form(User.EMAIL, User.PASSWORD)
        site_page.collect_burger()
        site_page.check_cross_in_modal_is_visible()
        number_of_order = site_page.get_number_of_order_from_modal
        site_page.click_on_cross_in_modal()
        site_page.click_on_order_feed()
        locator_number_in_feed = (By.XPATH, f"//div[@class='OrderFeed_ordersData__1L6Iv']//ul[2]/li[text()='{number_of_order}']")
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.check_in_progress_is_visible()
        assert WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator_number_in_feed))
