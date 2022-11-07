import random
def heitaNoppa(eyeInt):
    return random.randint(1, eyeInt)
tahkot=int(input('Anna nopan tahkojen määrä: '))
noppa=0
while noppa!=tahkot:
        noppa=heitaNoppa(tahkot)
        print(noppa)