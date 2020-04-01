from app import db

apple = "123"
class Name(db.Model):
    id = db.Column(db.Integer, nullable=True, primary_key=True)
    text = db.Column(db.String(20), nullable=False)