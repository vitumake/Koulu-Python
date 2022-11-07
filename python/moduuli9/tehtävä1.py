class Auto:
    def __init__(self, rekisteri, huiput):
        self.rekkari = rekisteri
        self.huippu = huiput
        self.nopeus = 0
        self.kuljettu = 0
    
    def __str__(self):
        return f'{self.rekkari} \n {self.huippu} \n {self.nopeus} \n {self.kuljettu}'

auto = Auto('ABC-123', 142)
print(auto)