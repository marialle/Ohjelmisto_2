import settings
from Autokilpailu import game


def create():
    romu = game.Kilpailu("Suuri romuralli", 8000, settings.game['cars'])
    settings.game["race"] = romu

