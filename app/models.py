from app import db
from datetime import datetime


class Report(db.Model):
    id = db.Column(db.String(2), primary_key=True)
    name = db.Column(db.String(64))
    flag = db.Column(db.String(120))
    reports = db.Column(db.Integer)
    cases = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    recovered = db.Column(db.Integer)
    lat = db.Column(db.Integer)
    lng = db.Column(db.Integer)
    deltaCases = db.Column(db.Integer)
    deltaDeaths = db.Column(db.Integer)

    def __repr__(self):
        return '<Report {}>'.format(self.name)


class Date(db.Model):
    id = db.Column(db.String(2), primary_key=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Date {} {}>'.format(self.id, self.timestamp)
