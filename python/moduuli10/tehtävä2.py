class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = 0

    def kerrosYlös(self):
        self.kerros += 1 if self.kerros + 1 <= self.ylin else self.ylin
        print(f'Hissi kerroksessa {self.kerros}')
    
    def kerrosAlas(self):
        self.kerros -= 1 if self.kerros - 1 >= self.alin else self.alin
        print(f'Hissi kerroksessa {self.kerros}')

    def siirryKerrokseen(self, kerros):
        if kerros > self.kerros: 
            for i in range(kerros - self.kerros): self.kerrosYlös()
        elif kerros < self.kerros:
            for i in range(self.kerros - kerros): self.kerrosAlas()

class Talo:
    def __init__(self, hissiLkm, alin, ylin):
        self.hissit = []
        for i in range(hissiLkm): self.hissit.append(Hissi(alin, ylin))

    def ajaHissiä(self, hissi, kerros):
        self.hissit[hissi - 1].siirryKerrokseen(kerros)
    
t = Talo(2, 0, 10)

t.ajaHissiä(2, 5)
#print(t.hissit[1].kerros)