import requests
import time

API_BASE_URL = "http://127.0.0.1:8000/api"
EMAIL = "test@example.com"
PASSWORD = "ghbdtn123"


def get_token(email, password):
    url = f"{API_BASE_URL}/token/"
    response = requests.post(url, data={"email": email, "password": password})
    response.raise_for_status()
    return response.json()["access"]


def start_calculation(token, building_number, year, month):
    url = f"{API_BASE_URL}/buildings/{building_number}/calculate_rent/{year}/{month}/"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, headers=headers)
    response.raise_for_status()
    return response.json()["progress_id"]


def check_calculation_progress(token, building_number, progress_id):
    url = f"{API_BASE_URL}/buildings/{building_number}/check_progress/{progress_id}/"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def get_total_rent(token, building_number, year, month):
    url = f"{API_BASE_URL}/buildings/{building_number}/calculate_rent/{year}/{month}/total/"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


def main():
    month = 6
    year = 2025
    try:
        token = get_token(EMAIL, PASSWORD)

        progress_id = start_calculation(token, 1, year, month)
        print(f"Calculation started with progress ID: {progress_id}")

        while True:
            progress = check_calculation_progress(token, 1, progress_id)
            print(
                f"Progress: {progress['completed_apartments']}/{progress['total_apartments']} - Status: {progress['status']}"
            )
            if progress["status"] == "completed":
                print(f"Total rent for {month}/{year}: {progress['total_rent']}")
                break
            if progress["status"] == "error":
                print(f"Error: {progress['error']}")
                break
            time.sleep(1)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
