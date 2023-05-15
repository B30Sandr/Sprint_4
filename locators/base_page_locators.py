from selenium.webdriver.common.by import By


class BasePageLocator:
    COOKIE_ACCEPT_BUTTON = [By.XPATH, ".//button[text()='да все привыкли']"]
    YANDEX_SITE_BUTTON = [By.XPATH, ".//img[@alt='Yandex']/parent::a"]
    ORDER_STATUS_BUTTON = [By.XPATH, ".//button[text()='Статус заказа']"]
    ORDER_STATUS_INPUT_ORDER_NUMBER_FIELD = [By.XPATH, ".//input[@placeholder='Введите номер заказа']"]
    GO_TO_ORDER_STATUS_PAGE = [By.XPATH, ".//button[text()='Go!']"]