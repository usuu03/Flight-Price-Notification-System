from twilio.rest import Client

TWILIO_SID = "ACce73b5762ab0590acfe16016ef2294b6"
TWILIO_TOKEN = "fc41a6e7e1793c0c3d287b1cb13cb021"
TWILIO_VIRTUAL_NUM = "+447458158157"
TWILIO_NUM = "+447490773218"


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
