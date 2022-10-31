class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivu):
        Julkaisu.__init__(self, nimi)
        self.kirjoittaja = kirjoittaja
        self.sivu = sivu

    def tulosta_tiedot(self):
        print(f'Julkaisu {self.nimi} \n Kirjoittaja {self.kirjoittaja} \n Sivuja {self.sivu} \n')

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        Julkaisu.__init__(self, nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f'Julkaisu {self.nimi} \n Päätoimittaja {self.päätoimittaja} \n')

julkaisu1 = Lehti('Aku Ankka', 'Aki Hyyppä')
julkaisu2 = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)

julkaisu1.tulosta_tiedot()
julkaisu2.tulosta_tiedot()