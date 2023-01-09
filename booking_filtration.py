# This file will include a class with instance methods that will be
# responsible of interacting with our website after we have some results

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingFiltration:
    def __init__(self, driver):
        self.driver = driver

    def apply_star_rating(self, *star_values):
        star_filtration_box = self.driver.find_element(
            By.XPATH, '//div[@id="left_col_wrapper"]/div[2]/div/div/div[2]/div[6]'
        )
        star_child_elements = star_filtration_box.find_elements(
            By.CSS_SELECTOR, 'div[data-filters-item^="class"]'
        )

        for star_value in star_values:
            for star_element in star_child_elements:
                if (
                    str(star_value)
                    in str(star_element.get_attribute("data-filters-item")).strip()
                ):
                    star_element.click()
