import requests

URL = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights"

def get_flight_price(source_airport_code, destination_airport_code, departure_date, number_people, return_date=None):
    querystring = {
        "sourceAirportCode": source_airport_code,
        "destinationAirportCode": destination_airport_code,
        "date": departure_date,
        "itineraryType": "ONE_WAY" if return_date is None else "ROUND_TRIP",
        "sortOrder": "PRICE",
        "numAdults": number_people,
        "numSeniors": "0",
        "classOfService": "ECONOMY",
        "pageNumber": "1",
        "currencyCode": "GBP"
    }

    if return_date:
        querystring['returnDate'] = return_date

    headers = {
        "X-RapidAPI-Key": "ce4025f581msh671d0d550d83460p17ee11jsn201673161249",
        "X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }

    response = requests.get(URL, headers=headers, params=querystring)

    data = response.json()

    if data.get('status'):
        flights_data = data['data']['flights']

        print("Flights:")
        for flight in flights_data:
            print("\t---")
            for segment in flight['segments']:
                print("\tSegment:")
                for leg in segment['legs']:
                    print(f"\t\tDeparture: {leg['originStationCode']}")
                    print(f"\t\tDestination: {leg['destinationStationCode']}")
                    print(f"\t\tDeparture Date: {leg['departureDateTime']}")
                    print(f"\t\tArrival Date: {leg['arrivalDateTime']}")
                    print(f"\t\tMarketing Carrier: {leg['marketingCarrier']['displayName']}")
                print("\t---")
            print(f"\tTotal Price: £{flight['purchaseLinks'][0]['totalPrice']}")
            print(f"\tURL: {flight['purchaseLinks'][0]['url']}")

            # Print return date if it exists
            if 'returnDate' in querystring:
                print(f"\tReturn Date: {querystring['returnDate']}")
    else:
        print("No flights found.")

# Example usage
get_flight_price("LGW", "AGP", "2024-04-11", 1)
