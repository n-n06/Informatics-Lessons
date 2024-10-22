import requests

x = 5
s = "word"

response = requests.get("https://open.spotify.com/")

if response != None:
    print(response.content)
