from app import db
from datetime import datetime
from flask_login import UserMixin
from app import login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'))
    is_host = db.Column(db.Boolean)
    user_class = db.Column(db.String(15))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Room(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(4), index=True, unique=True)
    host_id = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    users = db.relationship('User', backref='client', lazy='dynamic')

    def __repr__(self):
        return '<Room with name {} has user {} as a host>'.format(self.room_name, self.host_id)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
