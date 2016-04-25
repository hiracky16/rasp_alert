import urllib.request
import json
import os

class rasp_weather:
	def __init__(self):
		self.city = '330010'

	def getWeather(self):
		res = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%self.city)
		res = res.read().decode('utf-8')
		res = json.loads(res)
		text = res['title']
		text = "".join(text.split(" ")[1:])
		for forecast in res['forecasts']:
			text = text + forecast['dateLabel'] + forecast['telop']

		return text


#if __name__=="__main__":
#	w = rasp_weather()
#	text = w.getWeather()
#	print(text)


#cmd = "jsay " + text

#os.system(cmd)

