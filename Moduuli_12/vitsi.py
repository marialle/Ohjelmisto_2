import requests
import json

vitsi = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(vitsi).json()

#print(json.dumps(vastaus, indent=1))

print(vastaus["value"])