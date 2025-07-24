
import time
import threading
import os
from scraper import get_prices_from_all_sites
from pushover import send_notification

hotel_name = os.getenv("HOTEL_NAME")
check_in = os.getenv("CHECK_IN")
check_out = os.getenv("CHECK_OUT")
try:
    threshold = float(os.getenv("PRICE_THRESHOLD"))
except (TypeError, ValueError):
    print("Invalid or missing PRICE_THRESHOLD. Exiting.")
    exit(1)

if not all([hotel_name, check_in, check_out]):
    print("Missing environment variables. Set HOTEL_NAME, CHECK_IN, CHECK_OUT.")
    exit(1)

print(f"Tracking '{hotel_name}' from {check_in} to {check_out} under €{threshold}...\n")

def price_watch_loop():
    while True:
        prices = get_prices_from_all_sites(hotel_name, check_in, check_out)
        for site, price in prices.items():
            if price and price <= threshold:
                send_notification(f"{site.upper()}: {hotel_name} is now €{price}!")
                return
        time.sleep(120)

threading.Thread(target=price_watch_loop, daemon=True).start()
input("\nPress ENTER to quit anytime.\n")
