import random
def heitaNoppa():
    return random.randint(1, 6)
noppa=0
while noppa!=6:
    noppa=heitaNoppa()
    print(noppa)