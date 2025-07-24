from flask import Flask, send_from_directory, request
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import Config
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import models and db
from models.user import User, db
from models.profile import Profile, Skill, Experience, Education, Achievement, ProfilePhoto
from models.post import Post, PostLike

# Import blueprints
from api import auth_bp, profile_bp, posts_bp, feed_bp, jobs_bp, messaging_bp

# Create Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
# Initialize CORS with configuration from config
CORS(app, 
     origins=app.config.get('CORS_ORIGINS', ["*"]), 
     supports_credentials=False, 
     allow_headers=["Content-Type", "Authorization"], 
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
     expose_headers=["*"],
     max_age=3600)
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
app.register_blueprint(posts_bp)
app.register_blueprint(feed_bp)
app.register_blueprint(jobs_bp)
app.register_blueprint(messaging_bp)

# Health check endpoint
@app.route('/')
def health_check():
    """Health check endpoint"""
    return {'status': 'healthy', 'message': 'Peer backend is running!'}

# Route to serve uploaded images
@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    """Serve uploaded files"""
    return send_from_directory('uploads', filename)

# Add CORS headers to all responses
@app.after_request
def after_request(response):
    # Get the origin from the request
    origin = request.headers.get('Origin')
    allowed_origins = app.config.get('CORS_ORIGINS', ["*"])
    
    # Check if the origin is in our allowed list
    if origin in allowed_origins:
        response.headers.add('Access-Control-Allow-Origin', origin)
    elif origin and 'localhost' in origin:
        # For development, allow localhost origins
        response.headers.add('Access-Control-Allow-Origin', origin)
    
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'false')
    return response


def setup_database():
    """Setup database tables"""
    try:
        # First try to use our working init_db script
        import subprocess
        import sys
        result = subprocess.run([sys.executable, 'init_db.py'], 
                              capture_output=True, text=True, cwd=os.path.dirname(__file__))
        if result.returncode == 0:
            print("✅ Database initialized using init_db.py")
        else:
            print("⚠️  init_db.py failed, trying SQLAlchemy fallback...")
            with app.app_context():
                db.create_all()
                print("✅ Database tables created successfully using SQLAlchemy!")
    except Exception as e:
        print(f"⚠️  Database setup error: {e}")
        print("✅ Continuing anyway - database might already exist")

# Create a function to initialize the app
def create_app():
    """Application factory function"""
    return app

if __name__ == '__main__':
    # Setup database tables
    setup_database()
    
    # Run the app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False) 