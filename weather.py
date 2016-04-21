import urllib.request
import json

city = '330010'

res = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%city).read()

res = res.decode('utf-8')

res = json.loads(res)

print(res['title'])

for forecast in res['forecasts']:
	print(forecast['dateLabel']+'('+forecast['date']+')')
	print(forecast['telop'])
	print(forecast['temperature']['max']['celsius'])
