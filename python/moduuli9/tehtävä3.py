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

auto = Auto('ABC-123', 60)
auto.kuljettu = 2000
auto.kiihdytä(60)

print(auto)

auto.kulje(1.5)

print(auto)