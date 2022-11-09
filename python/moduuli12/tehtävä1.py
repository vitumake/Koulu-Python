import requests

request = requests.get('https://api.chucknorris.io/jokes/random')
result = request.json()

print(result['value'])