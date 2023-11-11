from flask import Flask
from requests import *

app = Flask(__name__)

@app.route("/<path:message>")

def echo(message):
	try:
		url = get(message)
		return str(url.text)
	except:
		return "Ссылка не работает или не существует"
		
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)
