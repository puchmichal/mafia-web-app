from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))


    def __repr__(self):
        return '<User {}>'.format(self.username)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(4), index=True, unique=True)
    host_id = db.Column(db.Intiger, index=True, unique=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    users = db.relationship('Username', backref='client', lazy='dynamic')

    def __repr__(self):
        return '<Room {}>'.format(self.room_name)





    def __repr__(self):
        return '<Room with code{} has a host {}>'.format(self.code, self.host)