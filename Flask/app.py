from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/f')
def f():
    celsius = 40
    fahrenheit = (celsius * 9/5) + 32
    return "{} ".format(fahrenheit)


if __name__ == '__main__':
    app.run()
