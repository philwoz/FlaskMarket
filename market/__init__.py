from enum import unique
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from market.hidden import secret_key
s_key = secret_key()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = s_key

db = SQLAlchemy(app)
from market import routes


