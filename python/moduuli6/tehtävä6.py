import math
def pizzaValue(d, cost):
    return math.pi*(d/2/100)**2/cost
pizza1=[int(input('Anna pizzan halkaisija senttimetreinä: ')), int(input('Anna pizzan hinta: '))]
pizza2=[int(input('Anna pizzan halkaisija senttimetreinä: ')), int(input('Anna pizzan hinta: '))]
if pizzaValue(pizza1[0], pizza1[1])>pizzaValue(pizza2[0], pizza2[1]):
    print('Ensimmäien pizza on edullisempi pinta-alaa kohden')
else:
    print('Toinen pizza on edullisempi pinta-alaa kohden')