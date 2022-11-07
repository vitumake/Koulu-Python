from ctypes import alignment


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
        
h = Hissi(0, 10)

h.siirryKerrokseen(8)

h.siirryKerrokseen(0)