import requests
import datetime
import random

API_BASE_URL = "http://127.0.0.1:8000/api"
EMAIL = "test@example.com"
PASSWORD = ("ghbdtn123")


def random_date_2025():
    start_date = datetime.date(2025, 1, 1)
    return start_date


def generate_ten_readings():
    start_date = random_date_2025()

    # List to hold the dates and assigned numbers
    date_list = []

    # Generate 10 dates, each one month apart, with an increasing number assigned
    for i in range(10):
        date = start_date + datetime.timedelta(days=30 * i)
        date_list.append((date, i + 20))
    return date_list

def get_token(email, password):
    url = f"{API_BASE_URL}/token/"
    response = requests.post(url, data={"email": email, "password": password})
    response.raise_for_status()
    return response.json()["access"]

def get_apartments_in_building(token, building_number):
    url = f"{API_BASE_URL}/building/{building_number}/apartments"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_building_address(token, building_number):
    url = f"{API_BASE_URL}/building/{building_number}/address"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_building_rent(token, year, month, building_number):
    url = f"{API_BASE_URL}/building/{building_number}/calculate_rent/{year}/{month}"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def submit_reading(token, water_meter, reading, date):
    url = f"{API_BASE_URL}/water_meter/{water_meter}/submit_reading"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"reading": reading, "date": date}
    response = requests.put(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()
    pass

def main():
    try:
        token = get_token(EMAIL, PASSWORD)

        apartments = get_apartments_in_building(token, 1)
        print(apartments)
        building_address = get_building_address(token, 1)
        print(building_address)
        readings = generate_ten_readings()
        for reading in readings:
            result = submit_reading(token, 1, reading[1], str(reading[0]))
            print(result)
        rent = get_building_rent(token, 2025, 9, 1)
        print(rent)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()