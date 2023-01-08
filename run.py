from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency="USD")
    bot.change_language(language="us")
    bot.select_place_to_go(place_to_go="Rio De Janeiro")
