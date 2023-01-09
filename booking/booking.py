import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import BASE_URL
from booking_filtration import BookingFiltration
from booking_report import BookingReport
from prettytable import PrettyTable


class Booking(webdriver.Chrome):
    def __init__(
        self, driver_path=r":/Users/catuchi/lighthouse/SeleniumDrivers", teardown=False
    ):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ["PATH"] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # options.add_argument("incognito")
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(2)
        self.maximize_window()

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(BASE_URL)

    def change_currency(self, currency=None):
        try:
            currency_element = self.find_element(
                By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]'
            )
        except:
            pass

        try:
            currency_element = self.find_element(
                By.CSS_SELECTOR, 'button[data-testid="header-currency-picker-trigger"]'
            )
        except:
            pass

        currency_element.click()

        selected_currency_element = self.find_element(
            By.CSS_SELECTOR,
            'a[data-modal-header-async-url-param*="selected_currency={}"]'.format(
                currency.upper()
            ),
        )
        selected_currency_element.click()

    def change_language(self, language=None):
        try:
            language_element = self.find_element(
                By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your language"]'
            )
        except:
            pass

        try:
            language_element = self.find_element(
                By.CSS_SELECTOR, 'button[data-testid="header-language-picker-trigger"]'
            )
        except:
            pass

        language_element.click()

        selected_language_element = self.find_element(
            By.CSS_SELECTOR, "a[data-lang*={}]".format(language.lower())
        )
        selected_language_element.click()

    def select_place_to_go(self, place_to_go):
        search_field = self.find_element(By.NAME, "ss")
        search_field.clear()
        search_field.send_keys(place_to_go)

        try:
            first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        except:
            # print("couldn't find element using css selector")
            pass

        try:
            first_result = self.find_element(
                By.XPATH, "//ul[@data-testid='autocomplete-results']/li[1]/div"
            )
        except:
            # print("couldn't find element using xpath")
            pass

        first_result.click()

    def select_dates(self, check_in_date, check_out_date):

        check_in_date_clicked = False

        while not check_in_date_clicked:
            try:
                try:
                    check_in_element = self.find_element(
                        By.CSS_SELECTOR, 'span[data-date="{}"]'.format(check_in_date)
                    )
                except:
                    pass

                try:
                    check_in_element = self.find_element(
                        By.CSS_SELECTOR, 'td[data-date="{}"]'.format(check_in_date)
                    )
                except:
                    pass

                check_in_element.click()
                check_in_date_clicked = True
            except:
                try:
                    next_element = self.find_element(By.CLASS_NAME, "be298b15fa")
                except:
                    pass

                try:
                    next_element = self.find_element(
                        By.CSS_SELECTOR, 'div[data-bui-ref="calendar-next"]'
                    )
                except:
                    pass

                next_element.click()

        check_out_date_clicked = False

        while not check_out_date_clicked:
            try:
                try:
                    check_out_element = self.find_element(
                        By.CSS_SELECTOR, 'span[data-date="{}"]'.format(check_out_date)
                    )
                except:
                    pass

                try:
                    check_out_element = self.find_element(
                        By.CSS_SELECTOR, 'td[data-date="{}"]'.format(check_out_date)
                    )
                except:
                    pass

                check_out_element.click()
                check_out_date_clicked = True
            except:

                try:
                    next_element = self.find_element(By.CLASS_NAME, "be298b15fa")
                except:
                    # print("couldn't find element using classname")
                    pass

                try:
                    next_element = self.find_element(
                        By.CSS_SELECTOR, 'div[data-bui-ref="calendar-next"]'
                    )
                except:
                    # print("couldn't find element using second css selector")
                    pass

                next_element.click()

    def select_adults(self, count=1):

        try:
            selection_element = self.find_element(
                By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]'
            )
        except:
            pass

        try:
            selection_element = self.find_element(By.ID, "xp__guests__toggle")
        except:
            pass

        selection_element.click()

        while True:
            try:
                decrease_adults_element = self.find_element(
                    By.XPATH,
                    '//div[@data-testid="occupancy-popup"]/div/div/div[2]/button[1]',
                )
            except:
                pass

            try:
                decrease_adults_element = self.find_element(
                    By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]'
                )
            except:
                pass

            decrease_adults_element.click()

            # if statement
            adults_value_element = self.find_element(By.ID, "group_adults")
            adults_value = adults_value_element.get_attribute(
                "value"
            )  # should give back the adults count

            if int(adults_value) == 1:
                break

        try:
            increase_button_element = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]'
            )
        except:
            pass

        try:
            increase_button_element = self.find_element(
                By.XPATH,
                '//div[@data-testid="occupancy-popup"]/div/div[1]/div[2]/button[2]',
            )
        except:
            pass

        for _ in range(count - 1):
            increase_button_element.click()

    def select_children(self, count=0):

        try:
            increase_button_element = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Increase number of Children"]'
            )
        except:
            pass

        try:
            increase_button_element = self.find_element(
                By.XPATH,
                '//div[@data-testid="occupancy-popup"]/div/div[2]/div[2]/button[2]',
            )
        except:
            pass

        for _ in range(count):
            increase_button_element.click()

    def select_rooms(self, count=1):

        try:
            increase_button_element = self.find_element(
                By.CSS_SELECTOR, 'button[aria-label="Increase number of Rooms"]'
            )
        except:
            pass

        try:
            increase_button_element = self.find_element(
                By.XPATH,
                '//div[@data-testid="occupancy-popup"]/div/div[3]/div[2]/button[2]',
            )
        except:
            pass

        for _ in range(count - 1):
            increase_button_element.click()

    def click_search(self):
        search_button = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        search_button.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(4, 5)

        filtration.sort_price_lowest_first()

    def report_results(self):

        hotel_boxes = self.find_element(
            By.XPATH, '//div[@id="search_results_table"]/div[2]/div/div/div/div[4]'
        )

        report = BookingReport(hotel_boxes)
        report_rows = report.pull_deal_box_attributes()

        table = PrettyTable()
        table.field_names = ["Hotel Name", "Hotel Price", "Hotel Score"]
        # table = PrettyTable(field_names=["Hotel Name", "Hotel Price", "Hotel Score"])

        while report_rows:
            # print("------", report_rows)
            for i in report_rows:
                table.add_row(i)
            break

        print(table)
