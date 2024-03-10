import requests

URL = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights"

def get_flight_price(source_airport_code, destination_airport_code, departure_date, number_people):
    querystring = {
        "sourceAirportCode": source_airport_code,
        "destinationAirportCode": destination_airport_code,
        "date": departure_date,
        "itineraryType": "ONE_WAY",
        "sortOrder": "PRICE",
        "numAdults": number_people,
        "numSeniors": "0",
        "classOfService": "ECONOMY",
        "pageNumber": "1",
        "currencyCode": "GBP"
    }

    headers = {
        "X-RapidAPI-Key": "ce4025f581msh671d0d550d83460p17ee11jsn201673161249",
        "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }

    response = requests.get(URL, headers=headers, params=querystring)

    data = response.json()

    if data.get('status'):
        session_data = data['data']['session']
        flights_data = data['data']['flights']

        print("Session:")
        print(f"\tSearch Hash: {session_data['searchHash']}")
        print(f"\tPage Load UID: {session_data['pageLoadUid']}")
        print(f"\tSearch ID: {session_data['searchId']}")

        print("Flights:")
        for flight in flights_data:
            print("\t---")
            print(f"\tDeparture: {flight['segments'][0]['legs'][0]['originStationCode']}")
            print(f"\tDestination: {flight['segments'][-1]['legs'][-1]['destinationStationCode']}")
            print(f"\tDeparture Date: {flight['segments'][0]['legs'][0]['departureDateTime']}")
            print(f"\tArrival Date: {flight['segments'][-1]['legs'][-1]['arrivalDateTime']}")
            print(f"\tMarketing Carrier: {flight['segments'][0]['legs'][0]['marketingCarrier']['displayName']}")
            print(f"\tTotal Price: {flight['purchaseLinks'][0]['totalPrice']}")
            print(f"\tURL: {flight['purchaseLinks'][0]['url']}")
    else:
        print("No flights found.")

get_flight_price("MAD", "LHR", "2024-04-25", 1)
