import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = "AC00a76a35951189edcc9eee70a71f4c76"
TWILIO_AUTH_TOKEN = "f34f8e6f0b88ca71adccb87a519b30da"

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

message = client.messages.create(
    body=article,
    from_='+15097693727',
    to='+16394702628',
)

print(message.sid)