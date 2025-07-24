import random
import time

def get_prices_from_all_sites(hotel, check_in, check_out):
    return {
        "booking": mock_price("booking"),
        "marriott": mock_price("marriott"),
        "expedia": mock_price("expedia")
    }

def mock_price(site):
    print(f"Checking {site}...")
    time.sleep(1)
    return random.randint(150, 250)
