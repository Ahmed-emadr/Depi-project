from flask import Flask

app = Flask(__depi__)

@app.route('/')
def home():
    return "Hello, World! This is my simple web app."

if __depi__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

