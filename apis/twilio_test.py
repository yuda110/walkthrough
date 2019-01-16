from twilio.rest import Client

TWILIO_ACCOUNT_SID = ''
TWILIO_AUTH_TOKEN = ''

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

client.messages.create(
    to="+82",
    from_="+15",
    body="트윌리오 테스트"
)
