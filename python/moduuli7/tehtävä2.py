nimi = input('Anna nimi: ')
nimet = set()
while nimi != '':
    for i in nimet:
        if nimi == i: print('Aiemmin syötetty nimi')
    else: print('Uusi nimi')
    nimet.add(nimi)
    nimi = input('Anna nimi: ')
for i in nimet:
    print(i)