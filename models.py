from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True) #primary key means it is unique
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class Pitcher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    release_velocity = db.Column(db.Float)
    extension = db.Column(db.Float)
    tilt = db.Column(db.Float)
    vaa = db.Column(db.Float)
    spin_rate = db.Column(db.Float)
    release_height = db.Column(db.Float)
    ivb = db.Column(db.Float)
    ihb = db.Column(db.Float)

    def __repr__(self):
        return f'<Pitcher {self.name}>'