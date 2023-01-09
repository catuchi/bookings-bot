# This file contains methods that parses specific data
# from each of the deal boxes

import time
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

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            # Pulling deal name
            deal_name = (
                deal_box.find_element(By.CSS_SELECTOR, 'div[data-testid="title"]')
                .get_attribute("innerHTML")
                .strip()
            )
            # print(deal_name)
            time.sleep(1)
            deal_price = (
                deal_box.find_element(
                    By.CSS_SELECTOR, 'span[data-testid="price-and-discounted-price"]'
                )
                .get_attribute("innerHTML")
                .strip()
            )
            time.sleep(1)
            try:
                deal_score = (
                    deal_box.find_element(By.CSS_SELECTOR, 'div[aria-label^="Scored"]')
                    .get_attribute("innerHTML")
                    .strip()
                )
            except:
                deal_score = "N/A"

            # collection.append([deal_name, deal_price, deal_score])
            collection.append(
                [
                    deal_name.encode("UTF8").replace("&amp;", "&"),
                    deal_price.encode("UTF8").replace("&nbsp;", " ").replace(",", ""),
                    deal_score.encode("UTF8"),
                ]
            )
        return collection
