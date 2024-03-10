import requests

URL = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights"



def get_flight_price(source_airport_code, destination_airport_code, departure_date,
					 return_date, number_people ):
	querystring = {f"sourceAirportCode": {source_airport_code}, "destinationAirportCode": {destination_airport_code}, "date": "2024-06-21",
				   "itineraryType": "ONE_WAY", "sortOrder": "PRICE", "numAdults": "1", "numSeniors": "0",
				   "classOfService": "ECONOMY", "pageNumber": "1", "currencyCode": "USD"}

	headers = {
		"X-RapidAPI-Key": "ce4025f581msh671d0d550d83460p17ee11jsn201673161249",
		"X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
	}

	response = requests.get(URL, headers=headers, params=querystring)

	print(response.json())

get_flight_price("MAD", 'LHR')