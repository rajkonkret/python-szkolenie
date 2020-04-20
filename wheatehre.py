import requests
page = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Warszawa&appid=99a24a78addf4a2c41947189fcff67f7&&lang=p&format=jsonl')
json = page.json()
temp = json['main']['temp']
print(round(temp-273.5,2))
print(json['name'])
print(json['sys']['country'])