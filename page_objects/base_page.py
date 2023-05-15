import allure
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocator
from locators.main_page_locators import MainPageLocator
from test_data.urls import Urls
from selenium.webdriver.support import expected_conditions


class BasePage:
    driver = None

    def __init__(self, driver):
        self.driver = driver
        self.base_url = Urls.MAIN_PAGE

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def click_to_element(self, locator):
        return self.find_element(locator).click()

    @allure.step('Перейти по адресу')
    def go_to_site(self, url=None):
        if url is None:
            url = self.base_url
        self.driver.get(url)
        return self.click_cookie_accept()

    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, window_number: int = 1):
        return self.driver.switch_to.window(self.driver.window_handles[window_number])

    def wait_url_until_not_about_blank(self, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.url_contains(Urls.DZEN_HOME_PAGE))

    @allure.step('Принять куки')
    def click_cookie_accept(self):
        return self.click_to_element(BasePageLocator.COOKIE_ACCEPT_BUTTON)

    @allure.step('Перейти на страницу яндекса')
    def click_yandex_button(self):
        return self.click_to_element(BasePageLocator.YANDEX_SITE_BUTTON)
