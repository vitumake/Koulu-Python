import math
def pizzaValue(r, cost):
    return cost/math.pi*(r**2)
if pizzaValue(int(input('Anna pizzan halkaisija: ')), int(input('Anna pizzan hinta: '))) > pizzaValue(int(input('Anna pizzan halkaisija: ')), int(input('Anna pizzan hinta: '))):
    print('Ensimmäien pizza on edullisempi pinta-alaa kohden')
else:
    print('Toinen pizza on edullisempi pinta-alaa kohden')