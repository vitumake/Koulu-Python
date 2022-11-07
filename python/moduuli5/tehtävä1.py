import random
summa=0
for i in range(int(input('Arpakuutioiden lukumäärä: '))):
    summa+=random.randint(1, 6)
print(summa)