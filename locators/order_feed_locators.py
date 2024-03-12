from selenium.webdriver.common.by import By
from constants import Order


class OrderFeedLocators:
    # ORDER_FIRST - первый заказ в Ленте заказов
    ORDER_FIRST = (By.XPATH, "//ul[@class='OrderFeed_list__OLh59']/li[1]")
    # MODAL_DETAILS - модальное окно с деталями
    MODAL_DETAILS_ORDER = (By.XPATH, "//div[@class='App_App__aOmNj']/section[2]")
    # CLOSE_DETAILS - кнопка закрытия модального окна с деталями
    CLOSE_DETAILS_ORDER = (By.XPATH, "//div[@class='App_App__aOmNj']/section[2]//button")
    # COUNTER_FOR_ALL_TIME - счётчик "Выполнено за всё время"
    COUNTER_FOR_ALL_TIME = (By.XPATH, "//p[@class='text text_type_main-medium' and text()='Выполнено за все время:']/following-sibling::p")
    # COUNTER_FOR_TODAY - счётчик "Выполнено за сегодня"
    COUNTER_FOR_TODAY = (By.XPATH, "//p[@class='text text_type_main-medium' and text()='Выполнено за сегодня:']/following-sibling::p")
    # IN_PROGRESS - Заголовок В работе
    IN_PROGRESS = (By.XPATH, "//p[@class='text text_type_main-medium' and text()='В работе:']")

    NUMBER_IN_FEED = (By.XPATH, Order.NUMBER_IN_FEED)
