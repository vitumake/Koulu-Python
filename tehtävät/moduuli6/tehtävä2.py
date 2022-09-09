import random
def heitaNoppa(eyeInt):
    return random.randint(1, eyeInt)
tahkot=int(input('Anna nopan tahkojen määrä: '))
noppa=heitaNoppa(tahkot)
while noppa!=tahkot:
    print(noppa)
    noppa=heitaNoppa(tahkot)
print(noppa)