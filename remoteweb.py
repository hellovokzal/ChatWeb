from flask import Flask
from requests import *

app = Flask(__name__)

@app.route("/<message>")

def echo(message):
	try:
		url = get(f"https://{message}")
		return url
	except:
		return "Ссылка не работает или не существует"
		
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)
