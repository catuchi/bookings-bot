import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import BASE_URL


class Booking(webdriver.Chrome):
    def __init__(
        self, driver_path=r":/Users/catuchi/lighthouse/SeleniumDrivers", teardown=False
    ):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]'
        )

        currency_element.click()

        selected_currency_element = self.find_element(
            By.CSS_SELECTOR,
            'a[data-modal-header-async-url-param*="selected_currency={}"]'.format(
                currency.upper()
            ),
        )
        selected_currency_element.click()

    def change_language(self, language=None):
        language_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your language"]'
        )
        language_element.click()

        selected_language_element = self.find_element(
            By.CSS_SELECTOR, "a[data-lang*={}]".format(language.lower())
        )
        selected_language_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.ID, "ss")
        search_field.clear()
        search_field.send_keys(place_to_go)
