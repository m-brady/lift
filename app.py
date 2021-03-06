from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api')
def api():
    return 'Welcome to APIv2'


if __name__ == '__main__':
    app.run(debug=True)
