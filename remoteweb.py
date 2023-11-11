from flask import Flask
from requests import *

num = 0

app = Flask(__name__)

@app.route("/<path:message>")

def echo(message):
	global num
	if message[0:8] == "https://":
		num = 8
		while True:
			num = num + 1
			text1 = message[0:int(num)]
			if text1[int(num):int(num) + 1] == "/":
				text1 = f"{text1}/"
				break
	elif message[0:7] == "http://":
		num = 7
		while True:
			num = num + 1
			text1 = message[0:int(num)]
			if text1[int(num):int(num) + 1] == "/":
				text1 = f"{text1}/"
				break
	try:
		if message[0:8] == "https://" or message[0:7] == "http://":
			url = get(message)
			return str(url.text)
		else:
			url = get(f"{text1}{message}")
			return str(url.text)
	except:
		return "Ссылка не работает или не существует"
		
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)
