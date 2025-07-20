from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import Config
from models.user import User, db
from models.post import Post
from models.profile import Profile
from models.job import Job
from models.message import Message

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
CORS(app, origins=['http://localhost:5173', 'http://localhost:5174', 'http://localhost:5175'], supports_credentials=True)
db.init_app(app)
jwt = JWTManager(app)
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Import and register blueprints
from api.auth import auth_bp
from api.profile import profile_bp
from api.posts import posts_bp
from api.jobs import jobs_bp
from api.messaging import messaging_bp

app.register_blueprint(auth_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(jobs_bp)
app.register_blueprint(messaging_bp)

def setup_database():
    """Create database tables"""
    with app.app_context():
        try:
            db.create_all()
            print("✅ Database tables created successfully!")
        except Exception as e:
            print(f"❌ Error creating database tables: {e}")

if __name__ == '__main__':
    setup_database()
    app.run(debug=True, host='127.0.0.1', port=5000) 