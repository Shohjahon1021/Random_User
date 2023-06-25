import requests


url = 'https://randomuser.me/api/'
poyload = {
    'results':5,
    'gender':'female',
    'nat':'us,gb'
}

r = requests.get(url,params=poyload)
data = r.json()['results']

for i in data:
    print(i['name'],i['nat'])
