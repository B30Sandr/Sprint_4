import pytest

import allure

from locators.order_page_locators import OrderPageLocator
from page_objects.order_page import OrderPage
from test_data.order_data import orderPageData, ValidationErrors
from test_data.urls import Urls


@allure.story('Тестирование страницы оформления заказа')
class TestYaScooterOrderPage:
    @allure.description(ValidationErrors.NAME)
    def test_order_page_first_name_input_incorrect_show_error_message(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        order_page.input_first_name('KOlya')
        order_page.go_next()
        error_div = order_page.find_element(OrderPageLocator.INCORRECT_FIRST_NAME_MESSAGE)
        assert error_div.is_displayed() and error_div.text == ValidationErrors.NAME

    @allure.description(ValidationErrors.LAST_NAME)
    def test_order_page_last_name_input_incorrect_show_error_message(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        order_page.input_last_name('Lunin')
        order_page.go_next()
        error_div = order_page.find_element(OrderPageLocator.INCORRECT_LAST_NAME_MESSAGE)
        assert error_div.is_displayed() and error_div.text == ValidationErrors.LAST_NAME

    @allure.description(ValidationErrors.ADDRESS)
    def test_order_page_address_input_incorrect_show_error_message(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        order_page.input_address('Moscow')
        order_page.go_next()
        error_div = order_page.find_element(OrderPageLocator.INCORRECT_ADDRESS_MESSAGE)
        assert error_div.is_displayed() and error_div.text == ValidationErrors.ADDRESS

    @allure.description(ValidationErrors.SUBWAY)
    def test_order_page_subway_input_empty_show_error_message(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        order_page.go_next()
        error_div = order_page.find_element(OrderPageLocator.INCORRECT_SUBWAY_MESSAGE)
        assert error_div.is_displayed() and error_div.text == ValidationErrors.SUBWAY

    @allure.description(ValidationErrors.PHONE_NUMBER)
    def test_order_page_telephone_number_input_incorrect_show_error_message(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        order_page.input_telephone_number('123')
        order_page.go_next()
        error_div = order_page.find_element(OrderPageLocator.INCORRECT_TELEPHONE_NUMBER_MESSAGE)
        assert error_div.is_displayed() and error_div.text == ValidationErrors.PHONE_NUMBER

    @allure.description('Заполнить данные на этапе "Для кого самокат" и перейти на этап "Про аренду"')
    def test_order_page_go_to_choose_scooter_user_data_correct_open_about_rent(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        order_page.fill_user_data(orderPageData[0])
        order_page.go_next()
        assert len(order_page.find_elements(OrderPageLocator.ORDER_BUTTON)) > 0

    @allure.description('Заполнить данные на этапе "Про аренду" и оформить заказ')
    @pytest.mark.parametrize('data_set', [1, 2])
    def test_order_page_about_rent_input_correct_data_and_order_show_order_number(self, driver, data_set):
        data_set_index = data_set - 1
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        order_page.fill_user_data(orderPageData[data_set_index])
        order_page.go_next()
        order_page.fill_rent_data(orderPageData[data_set_index])
        order_page.click_order()
        order_page.click_accept_order()
        assert len(order_page.find_elements(OrderPageLocator.ORDER_COMPLETED_INFO)) > 0

    @allure.description('Заполнить данные на этапе "Про аренду", оформить заказ и перейти на статус заказа')
    @pytest.mark.parametrize('data_set', [1, 2])
    def test_order_page_create_order_and_go_order_status(self, driver, data_set):
        data_set_index = data_set - 1
        order_page = OrderPage(driver)
        order_page.go_to_site(Urls.ORDER_PAGE)
        order_page.fill_user_data(orderPageData[data_set_index])
        order_page.go_next()
        order_page.fill_rent_data(orderPageData[data_set_index])
        order_page.click_order()
        order_page.click_accept_order()
        order_number = order_page.get_order_number()
        order_page.click_go_to_status()
        current_url = order_page.current_url()
        assert (Urls.ORDER_STATUS_PAGE in current_url) and (order_number in current_url)
