import os

basedir = os.path.abspath(os.path.dirname(__file__))

MYSQL_HOST = "127.0.0.1"
MYSQL_USER = "root"
MYSQL_PWD = "123456"
MYSQL_DB = "test"

SQLALCHEMY_DATABASE_URI = "mysql://" + MYSQL_USER + ":" + MYSQL_PWD + "@" + MYSQL_HOST + "/" + MYSQL_DB
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True


UPLOAD_FOLDER = os.path.join(basedir, 'static/images')
IMGURL = 'http://10.0.0.87:83/'

SECRET_KEY = '_5#y2L"F4Q8z\n\xec]/'

