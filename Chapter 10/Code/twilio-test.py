from twilio.rest import Client

account_sid = '<<your account_sid>>'
auth_token = '<<your auth_token>>'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Twilio says hello!',
                              from_='<<your Twilio number>>',
                              to='<<your cell number'>>
                          )

print(message.sid)