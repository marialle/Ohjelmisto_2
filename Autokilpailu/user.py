from Autokilpailu import game
import settings
import random


def create():
    print("\n RALLIROMU")
    print("...........\n")
    player = input("H\n e\n  i\n\nSyötä nimesi:  ")
    settings.game["player"] = player
    create_cars()


def create_cars():
    autot = []
    aloitus = input("\nAloittaaksesi pelin, kerro vitsi ja paina Enter\n")
    print('')
    for i in range(10):
        auto = game.Auto(f"Auto {1 + i}", f"ABC-{1 + i}", random.randint(100, 200))
        autot.append(auto)
    settings.game['cars'] = autot
    settings.game['input'] = aloitus
