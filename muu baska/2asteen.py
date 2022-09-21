import math

def ratkaise2ay(a, b, c):
    try:
        posX=(((-1)*b)+math.sqrt(pow(b,2)-4*a*c))/(2*a)
    except: posX='null'
    try:
        negX=(((-1)*b)-math.sqrt(pow(b,2)-4*a*c))/(2*a)
    except: negX='null'
    return "{" + f'{posX}, {negX}' + "}"

a=float(input('Anna a komponentti '))
b=float(input('Anna b komponentti '))
c=float(input('Anna c komponentti '))
if ratkaise2ay(-1, 1, -2)=='{null, null}': print('{}')
else: print(ratkaise2ay(a, b, c))
