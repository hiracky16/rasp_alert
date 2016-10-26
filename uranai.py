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
		s = all_result[index]

		rank = '今日のさそり座の運勢は'+str(s['rank'])+'位。'
		content = s['content']+'。'
		job = '仕事運'+str(s['job'])+'位。'
		love = '恋愛運'+str(s['love'])+'位。'
		money = '金銭運'+str(s['money'])+'位。'
		item = 'ラッキーアイテム'+s['item']+'です。'
		color = 'ラッキーカラー'+s['color']+'です。'
		result = rank + content + job + love + money + item + color

		return result
		
