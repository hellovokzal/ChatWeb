from flask import Flask
from requests import get

app = Flask(__name__)
num = 0

@app.route("/<path:message>")
def echo(message):
    global num
    global num1
    if message.startswith("https://"):
        num = 8
        num1 = 0
        while True:
            num = num + 1
            text1 = message[:num]
            if message[num1:num] == "/":
                text1 = text1
                break
            num1 = num + 1
    elif message.startswith("http://"):
        num = 7
        num1 = 0
        while True:
            num += 1
            text1 = message[:num]
            if message[num1:num] == "/":
                text1 = text1
                break
            num1 += 1
    try:
        if message.startswith("https://") or message.startswith("http://"):
            url = get(message)
            return str(url.text)
        else:
            url = get(f"{text1}{message}")
            return str(url.text)
    except:
        return "Ссылка не работает или не существует"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
