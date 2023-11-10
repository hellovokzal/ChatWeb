from flask import Flask

chat = ""
num = 0
num1 = 1

app = Flask(__name__)

@app.route("/check")
def check():
    global chat
    global num
    global num1
    num = 0
    while True:
        if num == 1:
            num = 0
            with open("chat.txt", "r") as file:
                chat = file.read()
            return chat.replace("favicon.ico", "\n")
        else:
            num1 = 1

@app.route("/<message>")
def echo(message):
    global chat
    global num
    chat = ""
    with open("chat.txt", "r") as file1:
        chat = file1.read()
    with open("chat.txt", "w") as file2:
        file2.write(f"{chat}\n{message}")
        num = 1
    return "Отправлено"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
