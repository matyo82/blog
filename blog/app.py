from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hi')
def hi(name='matin'):
    return render_template('hi.html',name=name)
@app.route('/')
def home(name='matin'):
    return render_template('index.html',name=name)
