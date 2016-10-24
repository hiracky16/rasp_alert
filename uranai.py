import urllib.request
import datetime
import json
import os

class rasp_uranai:
	def __init__(self):
		today = datetime.date.today()
		self.year = today.year
		self.month = today.month
		self.day = today.day

	def getUranai(self):
		date = '%s/%s/%s'%(self.year, self.month, self.day)
		url = 'http://api.jugemkey.jp/api/horoscope/free/' + date
		res = urllib.request.urlopen(url)
		result_json = res.read().decode('utf-8')
		result = json.loads(result_json)
		all_result = result['horoscope'][date]
		signs = [a['sign'] for a in all_result]
		index = signs.index('蠍座')
		scorpion = all_result[index]

		print(scorpion)
'''		
		res = res.read().decode('utf-8')
		res = json.loads(res)
		text = res['title']
		text = "".join(text.split(" ")[1:])
		for forecast in res['forecasts']:
			text = text + forecast['dateLabel'] + forecast['telop']

		return text
'''
u = rasp_uranai()
u.getUranai()
