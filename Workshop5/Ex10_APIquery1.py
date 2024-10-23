import requests

response = requests.get("https://api.github.com/search/users",
                        params = {'q': 'drtim'})

if response.ok:
   respDict = response.json()
   for user in respDict['items']:
       print(user['login'])
