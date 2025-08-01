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
cors_origins = app.config.get('CORS_ORIGINS', ["*"])
cors_headers = app.config.get('CORS_ALLOW_HEADERS', ["Content-Type", "Authorization"])
cors_methods = app.config.get('CORS_METHODS', ["GET", "POST", "PUT", "DELETE", "OPTIONS"])
cors_supports_credentials = app.config.get('CORS_SUPPORTS_CREDENTIALS', False)

# Initialize CORS for production with file upload support
CORS(app, 
     origins=cors_origins, 
     supports_credentials=cors_supports_credentials, 
     allow_headers=cors_headers, 
     methods=cors_methods,
     expose_headers=["*"],
     max_age=3600,
     automatic_options=True)
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

# CORS preflight handler for all routes
@app.route('/api/<path:path>', methods=['OPTIONS'])
def handle_options(path):
    """Handle CORS preflight requests"""
    response = app.make_default_options_response()
    origin = request.headers.get('Origin')
    allowed_origins = app.config.get('CORS_ORIGINS', ["*"])
    
    if origin and origin in allowed_origins:
        response.headers['Access-Control-Allow-Origin'] = origin
    
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With, Accept'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Credentials'] = 'false'
    
    return response

# Route to serve uploaded images
@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    """Serve uploaded files"""
    return send_from_directory('uploads', filename)

# Route to serve profile photos
@app.route('/uploads/profile_photos/<path:filename>')
def profile_photo(filename):
    """Serve profile photos"""
    return send_from_directory('uploads/profile_photos', filename)

# Route to serve post photos
@app.route('/uploads/post_photos/<path:filename>')
def post_photo(filename):
    """Serve post photos"""
    return send_from_directory('uploads/post_photos', filename)

# Ensure CORS headers are properly set for production
@app.after_request
def after_request(response):
    # Get the origin from the request
    origin = request.headers.get('Origin')
    allowed_origins = app.config.get('CORS_ORIGINS', ["*"])
    
    if origin and origin in allowed_origins:
        response.headers['Access-Control-Allow-Origin'] = origin
    
    # Ensure other CORS headers are set (including file upload support)
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With, Accept'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Credentials'] = 'false'
    
    # Add additional headers for file uploads
    if request.method == 'POST' and 'photo' in request.files:
        response.headers['Access-Control-Expose-Headers'] = 'Content-Length, Content-Range'
    
    return response


def setup_database():
    """Setup database tables"""
    try:
        print("🔧 Setting up database...")
        
        # Ensure instance directory exists
        instance_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
        if not os.path.exists(instance_path):
            os.makedirs(instance_path, exist_ok=True)
            print(f"✅ Created instance directory: {instance_path}")
        
        # Import all models to ensure they're registered
        from models.user import User
        from models.post import Post, PostLike
        from models.job import Job
        from models.message import Message
        from models.profile import Profile, Skill, Experience, Education, Achievement, ProfilePhoto
        
        print("🔧 Models imported successfully")
        
        # Create tables using SQLAlchemy
        with app.app_context():
            print("🔧 Creating database tables...")
            db.create_all()
            print("✅ Database tables created successfully!")
            
            # Verify specific tables exist
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"🔧 Available tables: {tables}")
            
            # Check for critical tables
            critical_tables = ['user', 'profile', 'profile_photo', 'post', 'post_like', 'job', 'message']
            missing_tables = [table for table in critical_tables if table not in tables]
            
            if missing_tables:
                print(f"⚠️  Missing tables: {missing_tables}")
                print("🔧 Attempting to create missing tables...")
                db.create_all()
                print("✅ Missing tables created!")
            else:
                print("✅ All critical tables exist!")
        
        # Create test user if in production
        if os.environ.get('RENDER'):
            print("🚀 Production mode - creating test user...")
            try:
                print("🔧 Running create_test_user.py...")
                import subprocess
                import sys
                result = subprocess.run([sys.executable, 'create_test_user.py'], 
                                      capture_output=True, text=True, cwd=os.path.dirname(__file__))
                print(f"🔧 create_test_user.py stdout: {result.stdout}")
                print(f"🔧 create_test_user.py stderr: {result.stderr}")
                
                if result.returncode == 0:
                    print("✅ Test user created successfully")
                else:
                    print("⚠️  Test user creation failed, but continuing...")
            except Exception as e:
                print(f"⚠️  Test user creation error: {e}")
                
    except Exception as e:
        print(f"🔴 Database setup error: {e}")
        import traceback
        print(f"🔴 Full traceback: {traceback.format_exc()}")
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