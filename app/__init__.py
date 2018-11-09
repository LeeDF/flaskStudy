from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os, pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object('app.config')
db = SQLAlchemy(app)

from app import views, models
