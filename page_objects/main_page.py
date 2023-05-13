import allure

from locators.main_page import MainPageLocator
from page_objects.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Нажать на кнопку заказа вверху страницы')
    def click_top_order_button(self):
        return self.find_element(MainPageLocator.TOP_ORDER_BUTTON).click()

    @allure.step('Нажать на кнопку заказа внизу страницы')
    def click_bottom_order_button(self):
        return self.find_element(MainPageLocator.BOTTOM_ORDER_BUTTON).click()

    @allure.step('Нажать на вопрос в "Вопросы о важном"')
    def click_faq_question(self, question_number: int):
        elements = self.find_elements(MainPageLocator.FAQ_BUTTONS, 3)
        element = elements[question_number]
        element.click()
