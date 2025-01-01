from flask import Flask
from flask_cors import CORS
from models import db
from routes import api_routes
from flask_jwt_extended import JWTManager

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flights.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')



db.init_app(app)
CORS(app)
jwt = JWTManager(app)

app.register_blueprint(api_routes)

import os

print("JWT_SECRET_TOKEN:", os.getenv("JWT_SECRET_KEY"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all() #Create database tables
    app.run(debug=True)

