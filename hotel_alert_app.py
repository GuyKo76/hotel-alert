
import time
import threading
import sys
from scraper import get_prices_from_all_sites
from pushover import send_notification

print("Welcome to Hotel Price Watcher!")

print("Enter hotel name: ", end="", flush=True)
hotel_name = input().strip()

print("Enter check-in date (YYYY-MM-DD): ", end="", flush=True)
check_in = input().strip()

print("Enter check-out date (YYYY-MM-DD): ", end="", flush=True)
check_out = input().strip()

print("Alert me when price is below (EUR): ", end="", flush=True)
try:
    threshold = float(input().strip())
except ValueError:
    print("Invalid price. Exiting.")
    exit(1)

print(f"\nTracking '{hotel_name}' from {check_in} to {check_out} under €{threshold}...\n")

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
