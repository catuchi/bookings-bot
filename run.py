from booking.booking import Booking

try:
    input_one = raw_input("Currency? (CAD/USD/EUR/GBP/ZAR): ")
    # input_two = raw_input("Language? (us/gb/fr/pt/es): ")
    input_three = raw_input("Where do you want to go?: ")
    input_four = raw_input("What is the check in date? (YYYY-MM-DD): ")
    input_five = raw_input("What is the check out date? (YYYY-MM-DD): ")
    input_six = int(raw_input("How many people? (Max 30): "))
    input_seven = int(raw_input("How many rooms? (Max 30): "))

    with Booking() as bot:
        bot.land_first_page()
        # bot.change_currency(currency="CAD")
        bot.change_currency(currency=input_one)
        bot.change_language(language="us")
        # bot.select_place_to_go(place_to_go="British Columbia")
        bot.select_place_to_go(place_to_go=input_three)
        # bot.select_dates(check_in_date="2023-01-16", check_out_date="2023-02-04")
        bot.select_dates(
            check_in_date=input_four,
            check_out_date=input_five,
        )
        # bot.select_adults(3)  # max 30
        bot.select_adults(input_six)  # max 30
        # bot.select_children(2)  # max 10
        # bot.select_rooms(1)  # max 30
        bot.select_rooms(input_seven)  # max 30
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
