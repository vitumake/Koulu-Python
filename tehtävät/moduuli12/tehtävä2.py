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

#Jos vastaus ei ok
if not pos.ok : exit('Valintaa ei löytynyt')

result = pos.json()

#Otetaan koordinaatit talteen
lon = result[0]['lon']
lat = result[0]['lat']

#Uudet parametrit sää hakua varten
params = {
    'lon':lon,
    'lat':lat,
    'appid':apiKey,
    'lang':'FI'
}

#Haetaan sää
weather = requests.get('https://api.openweathermap.org/data/2.5/weather', params)

#Jos vastaus ei ok
if not weather.ok: exit('Säätä ei saatavilla')

result = weather.json()

desc = result['weather'][0]['description']
temp = result['main']['temp']

print(f'{kunta} \n {round(temp - 273.15)}°C \n {desc}')