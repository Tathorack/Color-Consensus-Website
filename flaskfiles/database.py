from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flaskfiles import app

db = SQLAlchemy(app)


class Searches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    search = db.Column(db.String())
    search_api = db.Column(db.String())
    red = db.Column(db.Integer)
    green = db.Column(db.Integer)
    blue = db.Column(db.Integer)
    response_time = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

    def __init__(self, search, search_api, red, green, blue,
                 response_time, timestamp=None):
        self.search = search
        self.search_api = search_api
        self.red = red
        self.green = green
        self.blue = blue
        self.response_time = response_time
        if timestamp is None:
            timestamp = datetime.utcnow()
        self.timestamp = timestamp
