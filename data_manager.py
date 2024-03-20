import requests

URL = "https://api.sheety.co/5c8c64d5c544a3a7f27625f7ea4ad4bc/flightDealsUsu/prices"


class DataManager:
    def __init__(self) -> None:
        self.destination_data = {}
    # This class is responsible for talking to the Google Sheet.
    def get_destination_data(self):
        response = requests.get(url=URL)
        data = response.json()
        self.destination_data = data['prices']  # Access the 'prices' key directly
    
        return self.destination_data


    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":{
                    "iataCode": city['iataCode']
                }
            }
            response = requests.put(
                url=f"{URL}/{city['id']}",
                json=new_data
            )
            print(response.text)