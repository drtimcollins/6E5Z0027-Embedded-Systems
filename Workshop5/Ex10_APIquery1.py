import requests, html

response = requests.get("https://opentdb.com/api.php",
                        params = {'amount': 1, 'type': 'boolean'})

if response.ok:
   respDict = response.json()           # Decode response - returns a Python dictionary
   question = respDict['results'][0]['question']   # Get the question from the dictionary
   print(html.unescape(question))                  # Print after decoding the HTML format
