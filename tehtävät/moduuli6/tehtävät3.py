def galToL(val):
    return val*3.78541178
gal=float(input('Anna gallonat: '))
while gal>0:
    print(f'{galToL(gal):6.2f} litraa')
    gal = float(input('Anna gallonat: '))