from selenium.webdriver.common.by import By


class SitePageLocators:
    # ORDER_BUTTON -кнопка "Оформить заказ"
    ORDER_BUTTON = (By.CSS_SELECTOR, "button.button_button_size_large__G21Vg")
    # CRATER_BUN - Кратерная булка N-200i
    CRATER_BUN = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']")
    # BURGER_CONSTRUCTOR - 'Перетяните булочку сюда'
    BURGER_CONSTRUCTOR = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
    # COUNTER_CRATER_BUN - счётчик добавления кратерной булки
    COUNTER_CRATER_BUN = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']//p[@class='counter_counter__num__3nue1']")
    # FILLINGS - раздел Начинки
    FILLINGS = (By.XPATH, "//div[@style]/div[@class][3]")
    # BIO_CUTLET - Биокотлета из марсианской Магнолии
    BIO_CUTLET = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa71']")
    # SAUCES - раздел Соусы
    SAUCES = (By.XPATH, "//div[@style]/div[@class][2]")
    # Соус Spicy-X
    SPICY_X_SAUCE = (By.XPATH, "//a[@href='/ingredient/61c0c5a71d1f82001bdaaa72']")
    # ORDER_ID - надпись "Идентификатор заказа"
    ORDER_ID = (By.XPATH, "//p[text()='идентификатор заказа']")

    # MODAL_DETAILS - модальное окно с деталями
    MODAL_DETAILS = (By.XPATH, "//div[@class='App_App__aOmNj']/section[1]")
    # CLOSE_DETAILS - кнопка закрытия модального окна с деталями
    CLOSE_DETAILS = (By.XPATH, "//div[@class='App_App__aOmNj']/section[1]//button")
    # NUMBER_OF_ORDER - номер заказа в модальном окне "Ваш заказ начали готовить"
    NUMBER_OF_ORDER = (By.XPATH, "//div[@class='App_App__aOmNj']/section[2]//h2")

