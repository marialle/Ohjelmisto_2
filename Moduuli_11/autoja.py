import random


class Auto:

    # ihan vaan huvikseen ettei oo kaikki ABC,
    # vois toki olla joku cvs tähän asiaan for more variety
    # rekisteri = ["HJK-", "EFK-", "KSF-", "PKS-", "RTK-", "ÅSP-", "DFE-", "RPK-", "AKI-"]
    # self.rekisteritunnus = f"{random.choice(Auto.rekisteri)}{random.randint(100,999)}"

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus # km/h
        self.nopeus = 0
        self.matka = 0

    def kiihdytä(self):
        muutos = random.randint(50, 150)
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunti):
        self.matka += self.nopeus * tunti

    def tulosta_tiedot(self):
        print(f"Auto rekisterinumerolla: {self.rekisteritunnus}\nHuippunopeus {self.huippunopeus}km/h,"
            f"tämänhetkinen nopeus {self.nopeus}km/h, kuljettu matka {self.matka}km, ", end='')


class Sähköauto(Auto):

    t = []

    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        # kWh
        self.akkukapasiteetti = f"{akkukapasiteetti} kWh"
        self.t.append(self)
        Auto.__init__(self, rekisteritunnus, huippunopeus)

    def tulosta_tiedot(self):
        Auto.tulosta_tiedot(self)
        print(f"ja akkukapasiteetti {self.akkukapasiteetti}\n")


class Polttomoottoriauto(Auto):

    t = []

    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        # l
        self.bensatankki = f"{bensatankki} l"
        self.t.append(self)
        Auto.__init__(self, rekisteritunnus, huippunopeus)

    def tulosta_tiedot(self):
        Auto.tulosta_tiedot(self)
        print(f"ja bensatankin koko {self.bensatankki}.\n")


(Sähköauto("ABC-15", 180, 52.5))
(Polttomoottoriauto("ACD-123", 165, 32))

for s in Sähköauto.t:
    Auto.kiihdytä(s)
    Auto.kulje(s, 3)
    s.tulosta_tiedot()
for p in Polttomoottoriauto.t:
    Auto.kiihdytä(p)
    Auto.kulje(p, 3)
    p.tulosta_tiedot()
