import requests

TEQUILA_URL = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = '7qB4xNHn2XIj12kc03IgEziLS3nQrU2C'

class FlightSearch:
    def get_iata_code(self, city):
      
        location = f"{TEQUILA_URL}/locations/query"
        headers = { "apikey": TEQUILA_API_KEY}
        query = {"term": city, "location_types": "city"}
        response = requests.get(url=location, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code
       
