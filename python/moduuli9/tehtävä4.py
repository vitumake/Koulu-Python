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
        return f'{self.rekkari} \n {self.huippu} \n {self.nopeus} \n {self.kuljettu}'

autot = []
for i in range(10):
    auto = Auto(f'ABC-{i+1}', randint(100, 200))
    autot.append(auto)

kilpailu = True
while kilpailu:
    for i in autot:
        i.kiihdytä(randint(-10, 15))
        i.kulje(1)
        if i.kuljettu > 10000:
            kilpailu = False

for i in autot:
    print(f'{i}\n')