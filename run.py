from booking.booking import Booking

# inst = Booking()
# inst.land_first_page()

with Booking() as bot:
    bot.land_first_page()
    print("Exiting ...")
