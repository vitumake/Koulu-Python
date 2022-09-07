suuri = pieni = luku = input('Anna luku: ')
while ((luku.strip('-')).replace('.', '')).isnumeric():
    if float(luku)<float(pieni):
        pieni=float(luku)
    elif float(luku)>float(suuri):
        suuri=float(luku)-1
    luku=input('Anna luku: ')
print('Suurin luku: ' + str(suuri) + '\nPienin luku: ' + str(pieni))