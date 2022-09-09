import random
def heitaNoppa():
    return random.randint(1, 6)
noppa=heitaNoppa()
while noppa!=6:
    print(noppa)
    noppa=heitaNoppa()
print(noppa)