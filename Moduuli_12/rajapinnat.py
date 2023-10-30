import requests
import json

hakusana = input("Anna hakusana: ")

# pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = f"https://api.tvmaze.com/search/shows?q={hakusana}"
vastaus = requests.get(pyyntö).json()

# print(json.dumps(vastaus, indent=2))

for a in vastaus:
    print(a["show"]["name"])
    print(a["show"]["genre"])