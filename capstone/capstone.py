import requests
from boltiot import Sms, Bolt
import json

# Bolt IoT and Twilio credentials
API_KEY = "your_bolt_api_key"
DEVICE_ID = "your_bolt_device_id"
SID = "your_twilio_sid"
AUTH_TOKEN = "your_twilio_auth_token"
FROM_NUMBER = "your_twilio_phone_number"
TO_NUMBER = "your_phone_number"

# Crypto API details
CRYPTO_API_URL = "https://api.coingecko.com/api/v3/simple/price"
PARAMS = {"ids": "bitcoin", "vs_currencies": "usd"}

# Threshold
UPPER_THRESHOLD = 30000
LOWER_THRESHOLD = 20000

def fetch_price():
    try:
        response = requests.get(CRYPTO_API_URL, params=PARAMS)
        data = response.json()
        return data['bitcoin']['usd']
    except Exception as e:
        print(f"Error: {e}")
        return None

def send_alert(message):
    sms = Sms(SID, AUTH_TOKEN, FROM_NUMBER, TO_NUMBER)
    sms.send_sms(message)

def main():
    price = fetch_price()
    if price:
        print(f"Current Price: ${price}")
        if price > UPPER_THRESHOLD:
            send_alert(f"Bitcoin price crossed ${UPPER_THRESHOLD}! Current price: ${price}")
        elif price < LOWER_THRESHOLD:
            send_alert(f"Bitcoin price dropped below ${LOWER_THRESHOLD}! Current price: ${price}")

if __name__ == "__main__":
    main()
