import os
from picam import app

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.root_path, 'picam.db')
DEBUG = True
