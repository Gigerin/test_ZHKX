import requests

API_BASE_URL = "http://127.0.0.1:8000/api"
EMAIL = "test@example.com"
PASSWORD = ("ghbdtn123")


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

def main():
    try:
        token = get_token(EMAIL, PASSWORD)

        apartments = get_apartments_in_building(token, 1)
        print(apartments)
        building_address = get_building_address(token, 1)
        print(building_address)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()