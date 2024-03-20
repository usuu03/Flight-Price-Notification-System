from twilio.rest import Client


TWILIO_SID = "*************"
TWILIO_TOKEN = "************"
TWILIO_VIRTUAL_NUM = "******"
TWILIO_NUM = "********"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUM,
            to=TWILIO_NUM,
        )
        # Prints if successfully sent.
        print(message.sid)
