import requests, json, datetime
import mykeys

class SmartHeating:
    def __init__(self):
        self.actualTemperature = 20     # Initialise states of fields
        self.targetTemperature = 20
        self.isHeatingEnabled = True
        self.isBoilerOn = False
        self.lastID = 0
        self.uploadData = {'api_key': mykeys.WRITE_KEY}
        self.timeOfLastPost = datetime.datetime(1970,1,1)   # Forces first post
    def updateFromIoT(self):
        response = requests.get('https://api.thingspeak.com/channels/' +
                         mykeys.CHANNEL_ID + '/feeds.json?api_key=' +
                         mykeys.READ_KEY + '&minutes=2').json()
        print(f"{len(response['feeds'])} received.")
        for feed in response['feeds']:
            if feed['entry_id'] > self.lastID:	         # Not seen this entry yet
                self.lastID = feed['entry_id']
                if feed['field2'] is not None:	         # Skip empty feeds
                    self.isBoilerOn = (feed['field2'] == 'True')
                    print("Boiler State:", self.isBoilerOn)
                if feed['field3'] is not None:
                    self.actualTemperature = int(feed['field3'])
                    print("Actual Temperature:",self.actualTemperature)
                print('State updated')					# Show new state data        
    def postData(self):
        if (datetime.datetime.now() - self.timeOfLastPost).total_seconds() < 30:
            return False            # Fail if trying to repost too soon
        self.uploadData['field1'] = 'True' if self.isHeatingEnabled else 'False'
        self.uploadData['field4'] = str(self.targetTemperature)
        response = requests.post('https://api.thingspeak.com/update.json',
                       headers={'Content-Type': 'application/json'},
                       data=json.dumps(self.uploadData))
        if response.status_code == 200 and response.json() != 0:
            print("Post operation successful")
            self.timeOfLastPost = datetime.datetime.now()
            return True
        else:
            return False
