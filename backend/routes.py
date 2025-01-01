from flask import Blueprint, request, jsonify
from models import db, User, Flight, SavedFlight
from flight_search import FlightSearch
from flask_jwt_extended import create_access_token
import bcrypt

# from flask_jwt_extended import jwt_required, get_jwt_identity

# @api_routes.route("/api/protected", methods=["GET"])
# @jwt_required()
# def protected():
#     current_user = get_jwt_identity()
#     return jsonify({"message": f"Hello, {current_user['email']}!"}), 200



api_routes = Blueprint("api", __name__)
flight_search = FlightSearch()


@api_routes.route("/api/register", methods=["POST"])
def register():
    data = request.json
    hashed_password = bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())
    new_user = User(email=data["email"], password=hashed_password.decode("utf-8"))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201


@api_routes.route("/api/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    
    if user and bcrypt.checkpw(data["password"].encode("utf-8"), user.password.encode("utf-8")):
        #Generate a JWT Token
        access_token = create_access_token(identity={"id": user.id, "email": user.email})
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401