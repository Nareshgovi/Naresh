from twilio.rest import Client
from urllib.parse import urlencode
import time

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACfc868bc10e0942878268e6bc85c40ee4'
auth_token = 'b6ae191dab27c59e470c16a96f7ce4cd'
client = Client(account_sid, auth_token)

def makeCall():
    call = client.calls.create(
        to='+917411694426',
        from_='+12567279885',
        url='https://handler.twilio.com/twiml/EHfbb90737b757304c9b3cbcb81ba73770?' + urlencode(
            {'Message': "hey sorry to say that application has failed"})
        # url = 'https://www.twilio.com/console/twiml-bins/EHfbb90737b757304c9b3cbcb81ba73770'

    )

    print(call.sid)
    call_sid = call.sid

    time.sleep(30)

    call = client.calls(call_sid).fetch()
    print(call.status)


def sendSMS(msg):
    message = client.messages \
        .create(
        body=msg,
        from_='+12567279885',
        to='+917411694426'
    )

    print(message.sid)

