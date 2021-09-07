from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from market.hidden import secret_key
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
s_key = secret_key()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = s_key

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
from market import routes


