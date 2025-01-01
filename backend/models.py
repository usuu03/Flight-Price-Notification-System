from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    notifications_enabled = db.Column(db.Boolean, default=True)
    
class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    origin_city = db.Column(db.String(50), nullable=False)
    destination_city = db.Column(db.String(50), nullable=False)
    departure_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime, nullable=False)
    booking_url = db.Column(db.String(500), nullable=False)

class SavedFlight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flight.id"), nullable=False)
    user = db.relationship("User", backref="saved_flights")
    flight = db.relationship("Flight", backref="saved_by")