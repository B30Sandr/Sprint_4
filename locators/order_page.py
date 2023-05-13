from selenium.webdriver.common.by import By


class OrderPageLocator:
    FIRST_NAME_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Имя')]"]
    INCORRECT_FIRST_NAME_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'Имя')]/parent::div/div"]
    LAST_NAME_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]"]
    INCORRECT_LAST_NAME_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'Фамилия')]/parent::div/div"]
    ADDRESS_INPUT = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]"]
    INCORRECT_ADDRESS_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'Адрес')]/parent::div/div"]
    SUBWAY_FIELD = [By.XPATH, ".//input[contains(@placeholder,'метро')]"]  # /parent::div
    INCORRECT_SUBWAY_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,"
                                          "'метро')]/parent::div/parent::div/parent::div/div[@class!='select-search']"]

    @staticmethod
    def SUBWAY_HINT_BUTTON(subway_name: str):
        return [By.XPATH, f".//div[text()='{subway_name}']/parent::button"]

    TELEPHONE_NUMBER_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]"]
    INCORRECT_TELEPHONE_NUMBER_MESSAGE = [By.XPATH, ".//input[contains(@placeholder,'Телефон')]/parent::div/div"]

    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]
    BACK_BUTTON = [By.XPATH, ".//button[text()='Назад']"]
    DATE_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Когда')]"]
    RENTAL_PERIOD_FIELD = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    RENTAL_PERIOD_LIST = [By.XPATH, ".//div[@class='Dropdown-option']"]
    COLOR_CHECKBOXES = [By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input"]
    COMMENT_FOR_COURIER_FIELD = [By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]"]
    ORDER_BUTTON = [By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"]
    ACCEPT_ORDER_BUTTON = [By.XPATH, ".//button[text()='Да']"]
    ORDER_COMPLETED_INFO = [By.XPATH, ".//div[contains(text(),'Номер заказа')]"]
    SHOW_STATUS_BUTTON = [By.XPATH, ".//button[text()='Посмотреть статус']"]
