import weather
import os

if __name__=="__main__":
	text = ""
	w = weather.rasp_weather()
	text = text + w.getWeather()

	cmd = "jsay " + text
	os.system(cmd)
