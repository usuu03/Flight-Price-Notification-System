Sure, here's the revised README with the correct download link:

# Flight Deals Notifier

This Python program notifies users about flight deals via SMS using the Twilio API. It fetches flight data from the Kiwi Tequila API and Google Sheets, and then sends notifications about deals based on user-defined criteria.

## Prerequisites

To use this program, you'll need:

- Python installed on your system.
- Accounts on Twilio, Kiwi Tequila, and Google Sheets.
- API keys and credentials for Twilio, Kiwi Tequila, and Google Sheets.

## Setup

1. Clone the repository.
2. Install the required dependencies:
   ```
   pip install twilio
   ```
3. Obtain API keys for Twilio and Kiwi Tequila.
4. Replace `TWILIO_SID`, `TWILIO_TOKEN`, `TWILIO_VIRTUAL_NUM`, `TWILIO_NUM`, and `TEQUILA_API_KEY` with your respective API keys.
5. Ensure your Google Sheet with destination data is properly formatted and accessible.
6. Update the Google Sheet URL in the code to fetch destination data.

## Usage

Run the Python script `main.py`. This will trigger the program to check for flight deals based on predefined criteria and send SMS notifications for any deals found.

## Example SMS Notifications

Below are examples of the text messages you may receive from the program:

![Example SMS Notification](<[text](https://drive.google.com/file/d/1dx2HzWQFJLFt8jO6R-gz5nHv2keqfHDD/view?usp=sharing)>)

## Acknowledgements

- **Twilio**: For providing the SMS service.
- **Kiwi Tequila**: For supplying flight data.
- **Google Sheets API**: For accessing destination data.

## Troubleshooting

- If you encounter any issues with the program, ensure that your API keys and credentials are correctly configured.
- Check for any errors in the code or dependencies.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
