import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='lentopeli',
         user='root',
         password='salasana1234',
         autocommit=True
         )

def countAirportByIsoNType(yhteys, iso, type):
    kursori = yhteys.cursor()
    kursori.execute(f"SELECT COUNT(*) FROM airport WHERE iso_country='{iso}' AND type='{type}';")
    return kursori.fetchone()[0]
iso=input('Anna maan ISO koodi: ').upper()
print(
    f'ISO koodilla "{iso}" löytyi:'
    f'\n{countAirportByIsoNType(yhteys, iso, "large_airport")} suurta kenttää'
    f'\n{countAirportByIsoNType(yhteys, iso, "medium_airport")} keskisuurta kenttää'
    f'\n{countAirportByIsoNType(yhteys, iso, "small_airport")} pientä kenttää'
    f'\n{countAirportByIsoNType(yhteys, iso, "heliport")} helikopteri kenttää'
    f'\n{countAirportByIsoNType(yhteys, iso, "seaplane_base")} vesilentokenttää'
    f'\n{countAirportByIsoNType(yhteys, iso, "closed")} suljettua kenttää'
)
