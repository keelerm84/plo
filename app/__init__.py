from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='')
app.config.from_object('config')
db = SQLAlchemy(app)


from app.models import testimonial
from app.models import doctor
from app.models import resource
from app.routes import index

from app.routes import testimonials
from app.routes import doctors
from app.routes import resources
