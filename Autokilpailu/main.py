import settings
import user
from Autokilpailu import game
import race
import misc


def main():
    user.create()
    race.create()
    while settings.game["go"]:
        game.Kilpailu.tunti_kuluu(settings.game["race"])
    misc.finished()
    misc.bye()


main()