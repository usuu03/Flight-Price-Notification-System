from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()



if sheet_data[0]['iataCode'] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row['iataCode'] = flight_search.get_iata_code(row['city'])
    print(sheet_data)
    
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
    