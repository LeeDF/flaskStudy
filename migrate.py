from flask_migrate import Migrate
from app import db, app
migrate = Migrate(app, db)
