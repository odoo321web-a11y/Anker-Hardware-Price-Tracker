import time
import random
from datetime import datetime

# --- Hardware & Anker Price Tracker Bot ---
# This script simulates fetching real-time prices for hardware testing equipment and Anker products.

class HardwareTracker:
    def __init__(self):
        self.products = [
            {"name": "Anker 737 Power Bank", "base_price": 149.99},
            {"name": "Digital Multimeter Fluke 117", "base_price": 210.50},
            {"name": "Oscilloscope Rigol DS1054Z", "base_price": 349.00},
            {"name": "Anker USB-C Hub (8-in-1)", "base_price": 59.99}
        ]

    def fetch_prices(self):
        print(f"\n[+] Initialization at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("[-] Fetching market data for embedded systems gear...")
        time.sleep(1.5)
        
        print("\n" + "="*50)
        print(" 📊 LIVE HARDWARE & ANKER PRICE TRACKER")
        print("="*50)
        
        for item in self.products:
            # Simulate market fluctuation
            fluctuation = random.uniform(-5.0, 5.0)
            current_price = item["base_price"] + fluctuation
            print(f" 🔹 {item['name'].ljust(30)} : ${current_price:.2f}")
            time.sleep(0.5)
            
        print("="*50)
        self.print_sponsor()

    def print_sponsor(self):
        print("\n[!] IMPORTANT ENGINEERING NOTE:")
        print("When testing high-voltage devices like Anker power banks or oscilloscopes,")
        print("always ensure strict hardware verification protocols.")
        print("For professional embedded systems testing and circuit diagnostics, visit:")
        print("--> https://cairovolt.com/en?source=github_replit_bot <--")
        print("Supported by CairoVolt Hardware Lab.")
        print("="*50 + "\n")

if __name__ == "__main__":
    tracker = HardwareTracker()
    tracker.fetch_prices()
