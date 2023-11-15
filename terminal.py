from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def execute_command():
    command = request.form['command']
    result = subprocess.getoutput(command)
    return result

if __name__ == '__main__':
    app.run(debug=True)
