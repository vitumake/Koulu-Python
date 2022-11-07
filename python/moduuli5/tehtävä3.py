numero=int(input('Anna numero: '))
for i in range(numero-1, 0, -1):
    if i==1: print('Luku on alkuluku')
    elif numero%i==0: break