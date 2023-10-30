import requests


def get_weather():
    key = "19a760ec7a75608b0da7908b41f30fe0"

    paikkakunta = input("Syötä paikkakunnan nimi: ")
    pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&lang=fi&appid={key}&units=metric"
    vastaus = requests.get(pyyntö).json()

    print(vastaus["weather"][0]["description"].capitalize())
    print(f'{vastaus["main"]["temp"]} C')


