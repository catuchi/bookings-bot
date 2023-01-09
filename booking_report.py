# This file contains methods that parses specific data
# from each of the deal boxes

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __init__(self, boxes_selection_element):
        self.boxes_selection_element = boxes_selection_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        # return self.boxes_selection_element.find_elements(By.CLASS_NAME, "da89aeb942")
        return self.boxes_selection_element.find_elements(
            By.CSS_SELECTOR, 'div[data-testid="property-card"]'
        )
        # self.deal_boxes = self.boxes_selection_element.find_elements(
        #     By.CSS_SELECTOR, 'div[data-testid="property-card"]'
        # )

    def pull_titles(self):
        for deal_box in self.deal_boxes:
            deal_name = (
                deal_box.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]')
                .get_attribute("innerHTML")
                .strip()
            )
            print(deal_name)
