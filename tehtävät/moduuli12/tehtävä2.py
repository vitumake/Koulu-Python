import requests

apiKey = 'ffebc38ae20030120f401e9a2f531d63'

kunta = input('Anna paikan nimi: ')

#Parametrit kirjastona
params = {
    'q':kunta,
    'appid':apiKey
}

#Haetaan rajapinnasta ensin kunnan koordinaatit
pos = requests.get('http://api.openweathermap.org/geo/1.0/direct', params)
result = pos.json()

#Jos vastaus on tyhjä poistu
if result == []: exit('Valintaa ei löytynyt')

#Otetaan koordinaatit talteen
lon = result[0]['lon']
lat = result[0]['lat']

#Uudet parametrit sää hakua varten
params = {
    'lon':lon,
    'lat':lat,
    'appid':apiKey
}

#Haetaan sää
weather = requests.get('https://api.openweathermap.org/data/2.5/weather', params)
result = weather.json()

#Jos vastaus on tyhjä
if result == []: print('Säätä ei saatavilla.')

desc = result['weather'][0]['description']
temp = result['main']['temp']

#Kelvinit Celcius asteiksi'
temp -= 273.15
temp = round(temp)

print(f'{kunta} \n {temp}°C \n {desc}')