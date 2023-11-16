import requests
from key import weather_API_key


def get_weather():
    key = weather_API_key

    paikkakunta = input("Syötä paikkakunnan nimi: ")
    pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&lang=fi&appid={key}&units=metric"
    vastaus = requests.get(pyyntö).json()

    print(vastaus["weather"][0]["description"].capitalize())
    print(f'{vastaus["main"]["temp"]} C')


get_weather()