import requests, json

# Copy your channel ID number, API read key and API write key here
WRITE_KEY  = 'XXXXXXXXXXXXXXXX'
CHANNEL_ID = 'YYYYYYY'
READ_KEY   = 'ZZZZZZZZZZZZZZZZ'

# Request last three readings
response = requests.get('https://api.thingspeak.com/channels/' + CHANNEL_ID + 
                         '/feeds.json?api_key=' + READ_KEY + '&results=3')

if response.status_code == 200:     # HTTP status 200 = Successful request
    print("Request successful")
    data = response.json()
    print(f"Data received from channel: {data['channel']['name']}")
    for item in data['feeds']:
        print(f"{item['created_at']}: field1 = {item['field1']}, field2 = {item['field2']}")
else:
    print(f"HTTP request error: {response.status_code}")

uploadData = {'api_key': WRITE_KEY, 'field1':1, 'field2':1}
response = requests.post('https://api.thingspeak.com/update.json',
                           headers={'Content-Type': 'application/json'},
                           data=json.dumps(uploadData))
if response.status_code == 200:        # HTTP status code 200 = successful request
    print("Post operation succesful")
else:
    print(f"HTTP post error: {response.status_code}")
