import math
from fractions import Fraction

def ratkaise2ay(a, b, c):
    try:
        posX=(((-1)*b)+math.sqrt(pow(b,2)-4*a*c))/(2*a)
    except: posX='null'
    try:
        negX=(((-1)*b)-math.sqrt(pow(b,2)-4*a*c))/(2*a)
    except: negX='null'
    return[posX, negX]

while True:
    a=float(input('Anna a komponentti '))
    b=float(input('Anna b komponentti '))
    c=float(input('Anna c komponentti '))
    vast=ratkaise2ay(a, b, c)
    if vast[0] and vast[1] == 'null': vastS='{}'
    elif vast[0]==vast[1]: vastS='{' + str(Fraction(vast[0]).limit_denominator()) + '}'
    else: vastS = '{' + f'{Fraction(vast[0]).limit_denominator()}, {Fraction(vast[1]).limit_denominator()}' + '}'
    print(vastS)
    if input('type e to exit: ').upper()=='E': break