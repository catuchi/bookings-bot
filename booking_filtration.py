# This file will include a class with instance methods that will be
# responsible of interacting with our website after we have some results

import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(
            By.XPATH,
            '//div[@id="left_col_wrapper"]/div[2]/div/div/div[2]/div[@data-filters-group="class"]',
        )
        star_child_elements = star_filtration_box.find_elements(
            By.CSS_SELECTOR, 'div[data-filters-item^="class"]'
        )
        # print(len(star_child_elements))

        for star_value in star_values:
            for star_element in star_child_elements:
                if (
                    str(star_value)
                    in str(star_element.get_attribute("data-filters-item")).strip()
                ):
                    star_element.click()
        time.sleep(3)

    def sort_price_lowest_first(self):
        dropdown_element = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]'
        )
        dropdown_element.click()

        price_element = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-id="price"]'
        )
        price_element.click()

    def sort_by_rating_highest_first(self):
        dropdown_element = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]'
        )
        dropdown_element.click()

        price_element = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-id="class"]'
        )
        price_element.click()

    def sort_by_top_reviewed(self):
        dropdown_element = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]'
        )
        dropdown_element.click()

        price_element = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-id="bayesian_review_score"]'
        )
        price_element.click()

    def sort_by_best_reviewed_and_lowest_price(self):
        dropdown_element = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-testid="sorters-dropdown-trigger"]'
        )
        dropdown_element.click()

        price_element = self.driver.find_element(
            By.CSS_SELECTOR, 'button[data-id="review_score_and_price"]'
        )
        price_element.click()
