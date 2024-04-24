import json
import requests
import geocoder


def load_data(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


def get_current_ip():
    try:
        response = requests.get("https://api.ipify.org")
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.RequestException:
        return None


def get_current_location_coordinates():
    # Get current IP address
    current_ip = get_current_ip()
    if current_ip:
        try:
            # Get current location using IP address
            g = geocoder.ip(current_ip)
            # Extract latitude and longitude
            latitude, longitude = g.latlng
            return latitude, longitude
        except:
            return None
    else:
        return None
