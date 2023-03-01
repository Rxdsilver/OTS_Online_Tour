from app import db
from datetime import datetime


class Tournament(db.Model):
    __tablename__ = 'tournament'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Tournament('{self.name}', '{self.code}, '{self.date}')"


class Player(db.Model):
    __tablename__ = 'player'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    team = db.Colmun(db.String(50), nullable=False)
    code = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"Player('{self.name}','{self.team}','{self.code}')"
