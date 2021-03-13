from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say(name):
    return f'Hi {name}'   

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    return f'{word} '*int(num)

if __name__ == '__main__':
    app.run(debug=True)