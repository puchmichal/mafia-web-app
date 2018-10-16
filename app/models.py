from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=False)
    room_in = db.Column(db.Integer, index=True)
    is_host = db.Column(db.Boolean, index=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(4), index=True, unique=True)
    host = db.Column(db.String(10), index=True, unique=False)

    def __repr__(self):
        return '<Room with code{} has a host {}>'.format(self.code, self.host)