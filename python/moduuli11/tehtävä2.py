from random import randint


class Auto:
    def __init__(self, rekisteri, huiput):
        self.rekkari = rekisteri
        self.huippu = huiput
        self.nopeus = 0
        self.kuljettu = 0

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippu: self.nopeus = self.huippu
        if self.nopeus < 0: self.nopeus = 0

    def kulje(self, aika):
        muutos = aika * self.nopeus
        self.kuljettu += muutos

class Sähköauto(Auto):
    def __init__(self, rekisteri, huiput, akkukapasiteetti):
        Auto.__init__(self, rekisteri, huiput)
        self.akku = akkukapasiteetti
    
    def __str__(self):
        return f'{self.rekkari} \n Nopeus: {self.nopeus}km/h Kuljettu: {self.kuljettu}km \n Virtaa {self.akku}kWh \n'

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huiput, bensa):
        super().__init__(rekisteri, huiput)
        self.bensa = bensa

    def __str__(self):
        return f'{self.rekkari} \n Nopeus: {self.nopeus}km/h Kuljettu: {self.kuljettu}km \n Tankissa {self.bensa}l \n'

autot = [] 

#ABC-15, 180 km/h, 52.5 kWh
autot.append(Sähköauto('ABC-15', 180, 52.5))

#ACD-123, 165 km/h, 32.3 l
autot.append(Polttomoottoriauto('ACD-123', 165, 32.3))

for i in autot:
    i.kiihdytä(randint(60, 100))
    i.kulje(3)
    print(i)