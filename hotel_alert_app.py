import time
import threading
from scraper import get_prices_from_all_sites
from pushover import send_notification

print("Welcome to Hotel Price Watcher!")
hotel_name = input("Enter hotel name: ").strip()
check_in = input("Enter check-in date (YYYY-MM-DD): ").strip()
check_out = input("Enter check-out date (YYYY-MM-DD): ").strip()
threshold = float(input("Alert me when price is below (EUR): ").strip())

print(f"\nTracking '{hotel_name}' from {check_in} to {check_out} under €{threshold}...")

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
