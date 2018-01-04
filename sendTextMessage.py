from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3ac159505baffa3285f95639ee3cd6a2"
# Your Auth Token from twilio.com/console
auth_token  = "815eb9530a795f94d0780ed1830eb7d6"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+905398563187", 
    from_="+17792013063",
    body="Hello from Python! Test begins! ")

print(message.sid)

#anaconda prompt - pip install twilio
#Browser – www.twilio.com/try-twilio
#(register and get the account_sid & auth_token number)
