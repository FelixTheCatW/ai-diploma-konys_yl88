import requests

def get_public_ip():    
    try:
        # Query a reliable and simple API
        response = requests.get("https://api.ipify.org", timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.text
    except requests.RequestException as e:
        print(f"An error occurred while fetching the IP address: {e}")
        return "127.0.0.1"
