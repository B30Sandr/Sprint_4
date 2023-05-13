import allure
import pytest

from locators.main_page import MainPageLocator
from page_objects.main_page import MainPage
from test_data.faq_answers import FAQ_Answers_Array, orderNum
from test_data.urls import Urls


@allure.story('Тестирование главной страницы')
class TestMainPage:
    @allure.description('Нажатие на верхнюю кнопку заказа')
    def test_click_top_order_button_show_order_page(self, driver):
        home_page = MainPage(driver)
        home_page.go_to_site()
        home_page.click_top_order_button()
        assert home_page.current_url() == Urls.ORDER_PAGE

    @allure.description('Нажатие на нижнюю кнопку заказа')
    def test_click_bottom_order_button_show_order_page(self, driver):
        home_page = MainPage(driver)
        home_page.go_to_site()
        home_page.click_bottom_order_button()

        assert home_page.current_url() == Urls.ORDER_PAGE

    @allure.description('Перейти на страницу Яндекса')
    def test_click_yandex_button_go_to_yandex(self, driver):
        home_page = MainPage(driver)
        home_page.go_to_site()
        home_page.click_yandex_button()
        home_page.switch_window(1)
        home_page.wait_url_until_not_about_blank()
        current_url = home_page.current_url()

        assert (Urls.YANDEX_HOME_PAGE in current_url) or (Urls.DZEN_HOME_PAGE in current_url) or (
                Urls.YANDEX_CAPTCHA_PAGE in current_url)

    @allure.description('Тесты текста аккордионов')
    @pytest.mark.parametrize('order_item_number', orderNum)
    def test_faq_click_on(self, driver, order_item_number):
        # синхронизация порядкового номера с индексом массива
        order_number = order_item_number - 1
        home_page = MainPage(driver)

        home_page.go_to_site()
        home_page.click_faq_question(order_number)

        answers = home_page.find_elements(MainPageLocator.FAQ_ANSWERS)
        answer = answers[order_number]

        assert answer.text == FAQ_Answers_Array[order_number]
