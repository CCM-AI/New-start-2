# models.py
from app import db

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=True)
    weight = db.Column(db.Float, nullable=True)
    height = db.Column(db.Float, nullable=True)
    chronic_conditions = db.Column(db.String(200), nullable=False)
    medications = db.Column(db.String(300), nullable=True)
    input_data = db.Column(db.JSON, nullable=False)
    risk_score = db.Column(db.Float)
    care_plan = db.Column(db.JSON)
