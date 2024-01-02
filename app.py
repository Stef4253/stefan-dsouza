from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return 'Name: Stefan Dsouza\nUSN: 1BM20IS158'


if __name__ == "__main__":
    app.run(debug=True)