import os
from selenium import webdriver
from constants import BASE_URL


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r":/Users/catuchi/lighthouse/SeleniumDrivers"):
        self.driver_path = driver_path
        os.environ["PATH"] += self.driver_path
        super(Booking, self).__init__()

    def land_first_page(self):
        self.get(BASE_URL)
