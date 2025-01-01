from datetime import datetime

class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date) -> None:
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = datetime.strptime(out_date, '%Y-%m-%d')  # Convert string to datetime
        self.return_date = datetime.strptime(return_date, '%Y-%m-%d')  # Convert string to datetime
