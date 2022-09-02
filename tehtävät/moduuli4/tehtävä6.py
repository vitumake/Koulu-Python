import math
import random
n=0
N=i=int(input('Anna testattavien pistiden määrä: '))
while i>=0:
    pisteX = random.uniform(-1, 1)
    pisteY = random.uniform(-1, 1)
    if pow(pisteX, 2) + pow(pisteY, 2) < 1:
        n+=1
    i-=1
print('Pii:n likiarvo on: ' + str(4*n/N))
print('Pii:n vakio math librarysta: ' + str(math.pi))