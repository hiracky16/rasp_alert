import urllib.request
import json
import commands

city = '330010'

res = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%city).read()

res = res.decode('utf-8')

res = json.loads(res)

text = res['title']

for forecast in res['forecasts']:
	text = text + forecast['dateLabel']+'('+forecast['date']+')' + forecast['telop'] + forecast['temperature']['max']['celsius']

commands.getoutput("jsay "+ text)

