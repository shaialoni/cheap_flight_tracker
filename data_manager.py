import os
from dotenv import load_dotenv
from pprint import pprint
import requests

load_dotenv()

API_KEY = os.getenv("SHEETY_TOKEN")
URL_EP = os.getenv("SHEETY_URL")

auth = {
    "Authorization": f"Bearer {API_KEY}"
}

#pprint(data)

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(URL_EP, headers=auth)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data['flightsData']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "flightsDatum": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{URL_EP}/{city['id']}",
                json=new_data,
                headers=auth
            )
            print(response.text)
