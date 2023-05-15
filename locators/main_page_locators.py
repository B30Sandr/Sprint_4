from selenium.webdriver.common.by import By


class MainPageLocator:
    TOP_ORDER_BUTTON = [By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']"]
    BOTTOM_ORDER_BUTTON = [By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']"]
    FAQ_BUTTONS = [By.XPATH, ".//div[@class='accordion__button']"]
    FAQ_ANSWERS = [By.CSS_SELECTOR, ".accordion__panel"]
    YANDEX_SEARCH_FRAME = [By.XPATH,
                           ".//form[contains(@action,'yandex.ru/search')]/iframe[@aria-label='Поиск Яндекса']"]
