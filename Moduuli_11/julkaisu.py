class Julkaisu:

    julkaisut_lukumäärä = 0

    def __init__(self, nimi):
        Julkaisu.julkaisut_lukumäärä += 1
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"{self.nimi}, ", end='')


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumäärä):
        self.kirjailija = kirjailija
        self.sivumäärä = sivumäärä
        Julkaisu.__init__(self, nimi)

    def tulosta_tiedot(self):
        Julkaisu.tulosta_tiedot(self)
        print(f"kirjailija {self.kirjailija}, {self.sivumäärä} sivua.")


class Lehti(Julkaisu):

    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        Julkaisu.__init__(self, nimi)

    def tulosta_tiedot(self):
        Julkaisu.tulosta_tiedot(self)
        print(f"päätoimittaja {self.päätoimittaja}.")


lehdet = []
kirjat = []
lehdet.append(Lehti("Aku Ankka", "Aki Hyyppä"))
kirjat.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))

for l in lehdet:
    l.tulosta_tiedot()

for k in kirjat:
    k.tulosta_tiedot()