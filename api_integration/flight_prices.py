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
        flights_data = []
        for flight in data['data']['flights']:
            flight_info = {}
            segments = []
            for segment in flight['segments']:
                legs = []
                for leg in segment['legs']:
                    leg_info = {
                        'departure': leg['originStationCode'],
                        'destination': leg['destinationStationCode'],
                        'departure_date_time': leg['departureDateTime'],
                        'arrival_date_time': leg['arrivalDateTime'],
                        'marketing_carrier': leg['marketingCarrier']['displayName']
                    }
                    legs.append(leg_info)
                segments.append(legs)
            flight_info['segments'] = segments
            flight_info['total_price'] = flight['purchaseLinks'][0]['totalPrice']
            flight_info['url'] = flight['purchaseLinks'][0]['url']
            if 'returnDate' in querystring:
                flight_info['return_date'] = querystring['returnDate']
            flights_data.append(flight_info)
        return flights_data
    else:
        return None


# Example usage
get_flight_price("LGW", "AGP", "2024-04-11", 1)
