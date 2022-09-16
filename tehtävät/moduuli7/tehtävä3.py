lentoKt={}
doExit=True
while doExit:
    komento=input('Kirjoita "T" tallentaaksesi uusi lentokenttä \n Kirjoita "E" etsiäksesi lentokentää \n Lopeta jättämällä kenttä tyhjäksi\nKomento: ').upper()
    if komento=='T':
        lentoKt[input('Anna lentokentän ICAO: ')]=input('Anna lentokentän nimi: ')
    elif komento=='E':
        nimi = input('Anna etsittävän lentokentän ICAO koodi: ')
        if nimi in lentoKt: print(lentoKt[nimi])
        else: print('Lentokenttää ei löytynyt')
    else: doExit=False