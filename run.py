from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        # bot.change_currency(currency="CAD")
        # bot.change_language(language="us")
        bot.select_place_to_go(place_to_go="British Columbia")
        bot.select_dates(check_in_date="2023-01-16", check_out_date="2023-02-04")
        bot.select_adults(3)  # max 30
        # bot.select_children(2)  # max 10
        bot.select_rooms(1)  # max 30
        bot.click_search()
        bot.apply_filtrations()
        bot.refresh()  # A workaround to let bot grab data properly
        bot.report_results()

except Exception as e:
    if "in PATH" in str(e):
        print(
            "You are trying to run the bot from command line \n"
            "Please add to PATH your Selenium Drivers \n"
            "Windows: \n"
            "     set PATH=%PATH%;C:path-to-your-folder\ \n \n"
            "Linux: \n"
            "     PATH=$PATH:/path/to/your/folder/ \n"
        )
    else:
        raise
