import random


class Hissi:
    def __init__(self, alin=1, ylin=40, kerros=1):
        self.alin = alin
        self.ylin = ylin
        self.kerros = kerros

    def siirry_kerrokseen(self, kerrokseen):
        go = True
        if kerrokseen > self.kerros:
            print("Siirrytään ylöspäin.")
        elif kerrokseen < self.kerros:
            print("Siirrytään alaspäin.")
        while go:
            if kerrokseen > self.kerros:
                Hissi.kerros_ylös(self)
            elif kerrokseen < self.kerros:
                Hissi.kerros_alas(self)
            elif kerrokseen == self.kerros:
                go = False

    def kerros_ylös(self):
        self.kerros += 1
        print(f"Kerros {self.kerros}.")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Kerros {self.kerros}.")


class Talo:

    def __init__(self, nimi, talo_alin=1, talo_ylin=40):
        self.nimi = nimi
        self.talo_alin = talo_alin
        self.talo_ylin = talo_ylin
        self.hissit = []

    def luo_hissit(self):
        n = int(self.talo_ylin / 4)
        for i in range(n):
            hissi = Hissi(1, self.talo_ylin)
            self.hissit.append(hissi)

    def palohälytys(self):
        for h in self.hissit:
            Hissi.siirry_kerrokseen(h, 1)


class Naapurusto:

    def __init__(self):
        self.talot = []

    def uusi_talo(self, talo):
        self.talot.append(talo)

    def poista_talo(self, talo):
        self.talot.remove(talo)


def luodaan_talo(n):
    for i in range(n):
        nimi = input("Minkä niminen talosi on? \n")
        talo = Talo(f"{nimi}", 1, (random.randint(4, 20) * 2))
        Talo.luo_hissit(talo)
        naapurusto.uusi_talo(talo)


naapurusto = Naapurusto()

luodaan_talo(2)
print(len(naapurusto.talot))