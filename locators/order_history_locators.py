from selenium.webdriver.common.by import By


class OrderHistoryLocators:
    ORDER_HISTORY_DIV = (By.XPATH, "//div[@class='OrderHistory_orderHistory__qy1VB']")
    # LAST_ORDER - последний заказ из списка заказов
    LAST_ORDER = (By.XPATH, "//div[@class='OrderHistory_orderHistory__qy1VB']/ul/li[last()]")
    # NUMBER_OF_LAST_ORDER - номер последнего заказа
    NUMBER_OF_LAST_ORDER = (By.XPATH, "//div[@class='OrderHistory_orderHistory__qy1VB']/ul/li[last()]//p[@class='text text_type_digits-default']")
