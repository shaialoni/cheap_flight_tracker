import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.getenv("TWILIO_NUMBER")
TWILIO_VERIFIED_NUMBER = os.getenv("MY_NUMBER")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

        def __init__(self):
            self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

        def send_sms(self, message):
            message = self.client.messages.create(
                body=message,
                from_=TWILIO_VIRTUAL_NUMBER,
                to=TWILIO_VERIFIED_NUMBER,
            )
            # Prints if successfully sent.
            print("SMS sent", message.sid)