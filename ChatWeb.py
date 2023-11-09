from flask import Flask

app = Flask(__name__)

@app.route("/check")

def check():
 while True:
  global chat
  global num
  global num1
  if num == 1:
   num = 0
   with open("chat.txt", "r") as file:
    return str(file.read())
  else:
   num1 = 1
   
@app.route("/<message>")

while echo(message):
 global chat
 with open("chat.txt", "r") as file1:
  chat = file1.read()
 with open("chat.txt", "w") as file2:
  file2.write(chat)
if __name__ == "__main__":
    app.run(host="0.0.0.0" , port=8080)
