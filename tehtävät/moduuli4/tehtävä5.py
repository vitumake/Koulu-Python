tries=0
while tries<5 and (input('Käyttäjä: ')!='python' or input('Salasana: ')!='rules'):
    tries+=1
if tries<5:
    print('Tervetuloa')
else:
    print('Pääsy evätty')