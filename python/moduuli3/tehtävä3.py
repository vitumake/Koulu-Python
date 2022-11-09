sukupuoli=input('Kerro biologinen sukupuolesi: ')[0:1].upper()
hemoG=int(input('Anna hemoglobiiniarvo: '))
if sukupuoli=='M':
    ala=134
    yla=195
elif sukupuoli=='N':
    ala=117
    yla=175
else:
    print('Virheellinen sukupuoli.')
    exit()
if hemoG < ala:
    print('Hemoglobiiniarvo on alhainen')
elif hemoG > yla:
    print('Hemoglobiiniarvp on korkea')
else:
    print('Hemoglobiiniarvo on normaali')