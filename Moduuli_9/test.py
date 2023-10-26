class Koira:

    yhteensä = 0

    def __init__(self, nimi, syntymavuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.haukahdus = haukahdus
        Koira.yhteensä += 1

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(f"{self.nimi} haukkuu {self.haukahdus}!")
        return


class Hoitola:
    def __init__(self):
        self.koirat = []

    def koira_sisään(self, koira):
        self.koirat.append(koira)
        print(f"{koira.nimi} kirjattu sisään.")

    def koira_ulos(self, koira):
        self.koirat.remove(koira)
        print(f"{koira.nimi} kirjattu ulos.")

    def tervehdi_koiria(self):
        for koira in self.koirat:
            koira.hauku(1)

    def listaa_koirat(self):
        for koira in self.koirat:
            print(f"{koira.nimi} ", end='')


iines = Koira("Iines", 2018)
minni = Koira("Minni", 2022, "Viu viu viu")
petteri = Koira("Petteri", 2017, "Hau, hau")

hoitola = Hoitola()

hoitola.koira_sisään(iines)
hoitola.koira_sisään(minni)
hoitola.koira_sisään(petteri)
hoitola.tervehdi_koiria()

hoitola.listaa_koirat()

