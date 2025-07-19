from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import Config
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import models and db
from models.user import User, db
from models.profile import Profile, Skill, Experience, Education, Achievement, ProfilePhoto

# Import blueprints
from api.auth import auth_bp
from api.profile import profile_bp

# Create Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
CORS(app)
db.init_app(app)
jwt = JWTManager(app)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(profile_bp)


def setup_database():
    """Setup database tables"""
    with app.app_context():
        db.create_all()
        print("✅ Database tables created successfully!")

# Create a function to initialize the app
def create_app():
    """Application factory function"""
    return app

if __name__ == '__main__':
    # Setup database tables
    setup_database()
    
    # Run the app
    app.run(debug=True) 