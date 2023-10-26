import settings
import random


class Kilpailu:
    def __init__(self, nimi, pituus, osallistujat):
        self.nimi = nimi
        self.pituus = pituus
        self.osallistujat = osallistujat

    # nIIn kutsuttu TuNtI kUlUu
    # mut siis periaatteessa sama juttsu
    def tunti_kuluu(self):
        for i in self.osallistujat:
            Auto.kiihdytä(i)
            Auto.kulje(i, 1)
        update_time()
        update_counter()
        self.kilpailu_ohi()
        if settings.game["counter"] == 10:
            self.tulosta_tilanne()

    def tulosta_tilanne(self):
        for i in self.osallistujat:
            Auto.print_all(i)
        print("-----------------------------------------------------\n")
        return

    def kilpailu_ohi(self):
        for i in self.osallistujat:
            kuljettu = Auto.hae_matka(i)
            if kuljettu >= self.pituus:
                settings.game["winner"] = Auto.hae_numero(i)
                settings.game["go"] = False
                self.tulosta_tilanne()
                return


class Auto:

    def __init__(self, numero, rekisteritunnus, huippunopeus, nopeus=0, matka=0):
        self.numero = numero
        self.rekisteritunnus = rekisteritunnus
        # km/h
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka

    def kiihdytä(self):
        muutos = random.randint(-10, 15)
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunti):
        self.matka += self.nopeus * tunti

    def hae_matka(self):
        return self.matka

    def hae_numero(self):
        return self.numero

    def print_all(self):
        print(f"{self.numero}, {self.rekisteritunnus}, huippunopeus {self.huippunopeus}km/h,\n"
            f"tämänhetkinen nopeus {self.nopeus}km/h ja kuljettu matka {self.matka}km.\n")


def update_time():
    settings.game["time"] += 1


def update_counter():
    settings.game["counter"] += 1
    if settings.game["counter"] > 10:
        settings.game["counter"] = 1
    return