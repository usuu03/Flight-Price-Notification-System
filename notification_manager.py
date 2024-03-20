from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        # Get Twilio credentials from environment variables
        twilio_sid = os.getenv("TWILIO_SID")
        twilio_token = os.getenv("TWILIO_TOKEN")
        twilio_virtual_num = os.getenv("TWILIO_VIRTUAL_NUM")
        twilio_num = os.getenv("TWILIO_NUM")

        # Initialize Twilio client
        self.client = Client(twilio_sid, twilio_token)
        self.twilio_virtual_num = twilio_virtual_num
        self.twilio_num = twilio_num

    def send_sms(self, message):
        # Send SMS using Twilio
        message = self.client.messages.create(
            body=message,
            from_=self.twilio_virtual_num,
            to=self.twilio_num,
        )
        # Print if successfully sent
        print(message.sid)
