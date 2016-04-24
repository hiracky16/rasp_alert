import urllib.request
import json
import os

city = '330010'

res = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%city).read()

res = res.decode('utf-8')

res = json.loads(res)

text = res['title']
text = "".join(text.split(" ")[1:])

for forecast in res['forecasts']:
	text = text + forecast['dateLabel'] + forecast['date'] + forecast['telop']

print(text)

cmd = "jsay " + text

os.system(cmd)

