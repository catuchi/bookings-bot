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
        search_field = self.find_element(By.NAME, "ss")
        search_field.clear()
        search_field.send_keys(place_to_go)

        # xpath_path = "/html/body/div[1]/div[2]/div/div/div/form/div[1]/div[1]/div/div/div[2]/ul/li[1]/div"
        # xpath_path_two = "//ul[@class='b530332a61']/li[1]"
        # xpath_path_three = "//ul[@data-testid='autocomplete-results']/li[1]"

        # selected_place_to_go = self.find_element(By.XPATH, xpath_path_three)
        # selected_place_to_go = self.find_element(By.CSS_SELECTOR, "li:first-child")
        # selected_place_to_go.click()

        # first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        # first_result.click()

        try:
            first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        except:
            print("couldn't find element using css selector")

        try:
            first_result = self.find_element(
                By.XPATH, "//ul[@data-testid='autocomplete-results']/li[1]/div"
            )
        except:
            print("couldn't find element using xpath")

        first_result.click()

    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element(
            By.CSS_SELECTOR, 'span[data-date="{}"]'.format(check_in_date)
        )
        check_in_element.click()

        check_out_element = self.find_element(
            By.CSS_SELECTOR, 'span[data-date="{}"]'.format(check_out_date)
        )
        check_out_element.click()
