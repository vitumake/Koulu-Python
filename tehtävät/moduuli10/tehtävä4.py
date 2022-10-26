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

    def __str__(self):
        return f'{self.rekkari} \n Nopeus: {self.nopeus}km/h Kuljettu: {self.kuljettu}km \n'

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tuntiKuluu(self):
        for i in self.autot:
            i.kiihdytä(randint(-10, 15)) 
            i.kulje(1)
    
    def tulostaTilanne(self):
        for i in self.autot: print(i)

    def kilpailuOhi(self):
        for i in self.autot:
            if i.kuljettu > self.pituus: return True

autot = []
for i in range(10):
    auto = Auto(f'ABC-{i+1}', randint(100, 200))
    autot.append(auto)

kisa = Kilpailu('Suuri romuralli', 8000, autot)

kilpailuOhi = False
tunteja = 10
while not kilpailuOhi:
    kisa.tuntiKuluu()
    if kisa.kilpailuOhi():
        kisa.tulostaTilanne() 
        kilpailuOhi = True
    if tunteja == 10:
        tunteja = 0
        kisa.tulostaTilanne()    