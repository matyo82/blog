from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# create the app
app = Flask(__name__)

# create the extension
db = SQLAlchemy()
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


#creat model user...
class User(db.Model):
    id = db.Column(db.integer, primary_kay=True)
    userName = db.column(db.string, nullable=False, uniqu=True)
    email = db.Column(db.String)
     

@app.route('/hi')
def hi(name='matin'):
    return render_template('hi.html',name=name)
@app.route('/')
def home(name='matin'):
    return render_template('index.html',name=name)
