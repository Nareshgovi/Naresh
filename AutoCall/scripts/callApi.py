# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from urllib.parse import urlencode
import time

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

account_sid = 'ACfc868bc10e0942878268e6bc85c40ee4'
auth_token = 'b6ae191dab27c59e470c16a96f7ce4cd'


account_sid = 'ACe640b5ff15021c930f663539a981d674'
auth_token = 'bbfea22617732e9d4304b4066bb2f1c0'
client = Client(account_sid, auth_token

call = client.calls.create(
                        to='+917411694426',
                        # from_='+12567279885',
                        from_='+918106723600',
                        url = 'https://handler.twilio.com/twiml/EHfbb90737b757304c9b3cbcb81ba73770?' + urlencode({'Message': "Incident INC12345 assigned to you "})
                        #url = 'https://www.twilio.com/console/twiml-bins/EHfbb90737b757304c9b3cbcb81ba73770'
                        
                    )

print(call.sid)
call_sid = call.sid

time.sleep(60)

call = client.calls(call_sid).fetch()
print(call.status)





# List all the call log from twilio API

'''client = Client(account_sid, auth_token)
calls = client.calls.list(limit=20)

for record in calls:
    print(record.sid)
'''

# You can also filter the results. This example only returns phone calls to the phone number "+16698001727" which had a call status of "busy" but you can filter on other call properties as well.

'''calls = client.calls.list(status='busy', to='+917411694426', limit=20)

for record in calls:
    print(record.sid)
'''

### check the status of the call for the SID ...

'''
call = client.calls('CAad384f2b2a0ca98ac8ac66211fe18334').fetch()
print(call.status)
'''

