from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    # bot.change_currency(currency="USD")
    # bot.change_language(language="us")
    bot.select_place_to_go(place_to_go="Rio De Janeiro")
    bot.select_dates(check_in_date="2023-01-16", check_out_date="2023-02-04")
