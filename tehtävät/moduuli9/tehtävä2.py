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

    def __str__(self):
        return f'{self.rekkari} \n {self.huippu} \n {self.nopeus} \n {self.kuljettu}'

auto = Auto('ABC-123', 142)

print(auto)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)

print(auto)

auto.kiihdytä(-200)

print(auto)