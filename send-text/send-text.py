from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
client = TwilioRestClient(account = 'ACdfc004a349aae3b7c406499ce649a36e', token = 'a87348eb5fc761b965bab50cdb24a473')
message = client.messages.create(body="Ola Mariao", to="+553182250859", from_="7784035666") # Replace with your Twilio number
print message.sid