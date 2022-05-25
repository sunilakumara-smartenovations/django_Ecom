from django.conf import settings
import os
from twilio.rest import Client
import random 

class MessaHandler:
    phone_no =   None
    otp = None

    def __init__(self, phone_no, otp) -> None:
        client = Client(settings.ACCOUNT_SID),settings.AUTH_TOKEN
        message = client.messages.create(
                              body=f'your otp is {self.otp}',
                              from_='+13512136460',
                              to=self.phone_no
                          )
