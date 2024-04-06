### Flight Price Notification System

This project is a flight price notification system designed to retrieve flight details from an external API, check for low prices, and send notifications to users about potential deals.

#### Features:

1. **FlightSearch Class:** This class is responsible for interacting with the Kiwi.com API to search for flights between specified origin and destination cities. It includes methods to retrieve IATA codes for cities and search for available flights within a specified date range.

2. **NotificationManager Class:** This class handles the sending of SMS notifications to users. It utilizes the Twilio API to send messages containing flight deal details.

3. **DataManager Class:** This class communicates with a Google Sheet to retrieve and update flight data. It fetches flight details from the Google Sheet and updates IATA codes based on retrieved data.

4. **FlightData Class:** This class structures the flight data retrieved from the Kiwi.com API. It contains attributes such as price, origin city, origin airport, destination city, destination airport, departure date, and return date.

#### Files:

1. **flight_search.py:** Contains the FlightSearch class, responsible for searching for flights using the Kiwi.com API.

2. **notification_manager.py:** Contains the NotificationManager class, which handles the sending of SMS notifications using the Twilio API.

3. **data_manager.py:** Contains the DataManager class, responsible for interacting with Google Sheets to retrieve and update flight data.

4. **flight_data.py:** Contains the FlightData class, which structures the flight data retrieved from the Kiwi.com API.

5. **main.py:** The main script that orchestrates the entire flight price notification process. It retrieves destination data, checks for flight deals, and sends notifications to users.

#### External APIs:

1. **Kiwi.com API:** Used for searching for available flights between specified origin and destination cities.

2. **Twilio API:** Utilized for sending SMS notifications to users about flight deals.

#### Setup:

1. Ensure all required packages are installed. You can install them using pip:

   ```
   pip install requests twilio
   ```

2. Set up Twilio by obtaining your account SID, authentication token, and virtual phone number.

3. Update the Twilio SID, token, and phone numbers in the code to match your Twilio account details.

4. Ensure you have access to the Google Sheet containing flight data, and update the Google Sheet URL in the DataManager class.

5. Run the main.py script to start the flight price notification system.

#### Usage:

1. Run the main.py script to initiate the flight price notification system.

2. Receive SMS notifications about low-priced flight deals based on the criteria specified in the Google Sheet.

3. Monitor the terminal for logging information about the flight search and notification process.

#### Note:

This project is designed to provide users with notifications about low-priced flight deals based on data retrieved from Google Sheets and flight searches conducted through the Kiwi.com API. Make sure to adhere to the terms of use of the external APIs and services utilized in this project.
