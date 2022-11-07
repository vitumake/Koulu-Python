luvut=[]
summa=0
luku=input('Anna luku: ')
while luku!='':
    luvut.append(float(luku))
    luku = input('Anna luku: ')
luvut.sort(reverse=True)
for i in range(5):
    summa+=luvut[i]
print(summa)