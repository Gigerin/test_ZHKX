import requests
import datetime

API_BASE_URL = "http://127.0.0.1:8000/api"
EMAIL = "test@example.com"
PASSWORD = "ghbdtn123"


def random_date_2025():
    start_date = datetime.date(2025, 1, 1)
    return start_date


def generate_ten_readings():
    start_date = random_date_2025()

    date_list = []

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
    url = f"{API_BASE_URL}/buildings/{building_number}/apartments/"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_water_meters_in_apartment(token, apartment_id):
    url = f"{API_BASE_URL}/apartments/{apartment_id}/water_meters/"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def submit_reading(token, water_meter, reading, date):
    url = f"{API_BASE_URL}/water_meters/{water_meter}/submit_reading/"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"reading": reading, "date": date}
    response = requests.put(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()


def main():
    try:
        token = get_token(EMAIL, PASSWORD)

        apartments = get_apartments_in_building(token, 1)

        readings = generate_ten_readings()

        for apartment in apartments:
            apartment_id = apartment["pk"]
            print(apartment)
            water_meters = get_water_meters_in_apartment(token, apartment_id)
            for water_meter in water_meters["water_meters"]:
                water_meter_id = water_meter["pk"]
                for reading in readings:
                    result = submit_reading(
                        token, water_meter_id, reading[1], str(reading[0])
                    )
                    print(result)

        print("All readings have been submitted successfully.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
