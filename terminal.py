from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Remote Terminal</title>
</head>
<body>
    <form action="/command" method="post">
        <input type="text" name="command" placeholder="Enter your command">
        <input type="submit" value="Execute">
    </form>
    <div id="output"></div>
    <script>
        const form = document.querySelector('form');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            const response = await fetch('/command', {
                method: 'POST',
                body: formData
            });
            const result = await response.text();
            const output = document.getElementById('output');
            output.textContent = result;
        });
    </script>
</body>
</html>
"""

@app.route('/command', methods=['POST'])
def execute_command():
    command = request.form['command']
    result = subprocess.getoutput(command)
    return result

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
