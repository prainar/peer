from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User, db
from models.post import Post, PostLike
import os
import uuid
from werkzeug.utils import secure_filename

posts_bp = Blueprint('posts', __name__)

# Configure upload settings
UPLOAD_FOLDER = 'uploads/post_photos'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Create upload directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@posts_bp.route('/api/posts', methods=['POST'])
@jwt_required()
def create_post():
    """Create a new post"""
    try:
        user_id = int(get_jwt_identity())
        data = request.get_json()
        
        if not data or 'content' not in data:
            return jsonify({"message": "Content is required"}), 400
        
        # Ensure Post and PostLike tables exist
        try:
            inspector = db.inspect(db.engine)
            if 'post' not in inspector.get_table_names():
                print("🔧 Post table missing, creating it...")
                Post.__table__.create(db.engine, checkfirst=True)
                print("✅ Post table created!")
            if 'post_like' not in inspector.get_table_names():
                print("🔧 PostLike table missing, creating it...")
                PostLike.__table__.create(db.engine, checkfirst=True)
                print("✅ PostLike table created!")
        except Exception as e:
            print(f"⚠️  Error checking/creating Post tables: {e}")
        
        user = User.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 404
        
        post = Post(
            user_id=user_id,
            content=data['content'],
            image_url=data.get('image_url')
        )
        db.session.add(post)
        db.session.commit()
        
        return jsonify({
            "message": "Post created successfully",
            "post": {
                "id": post.id,
                "content": post.content,
                "image_url": post.image_url,
                "created_at": post.created_at.isoformat(),
                "user": {
                    "id": user.id,
                    "username": user.username
                },
                "likes_count": 0,
                "liked_by_user": False
            }
        }), 201
        
    except Exception as e:
        import traceback
        print(f"🔴 Post creation error: {e}")
        print(f"🔴 Full traceback: {traceback.format_exc()}")
        db.session.rollback()
        return jsonify({
            "message": "Error creating post",
            "error": str(e)
        }), 500

@posts_bp.route('/api/posts', methods=['GET'])
@jwt_required()
def get_posts():
    """Get all posts"""
    user_id = int(get_jwt_identity())
    
    posts = Post.query.order_by(Post.created_at.desc()).all()
    
    posts_data = []
    for post in posts:
        user = User.query.get(post.user_id)
        likes_count = PostLike.query.filter_by(post_id=post.id).count()
        liked_by_user = PostLike.query.filter_by(post_id=post.id, user_id=user_id).first() is not None
        
        posts_data.append({
            "id": post.id,
            "content": post.content,
            "image_url": post.image_url,
            "created_at": post.created_at.isoformat(),
            "user": {
                "id": user.id,
                "username": user.username
            },
            "likes_count": likes_count,
            "liked_by_user": liked_by_user
        })
    
    return jsonify({"posts": posts_data}), 200

@posts_bp.route('/api/posts/user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_posts(user_id):
    """Get posts by specific user"""
    current_user_id = int(get_jwt_identity())
    
    posts = Post.query.filter_by(user_id=user_id).order_by(Post.created_at.desc()).all()
    
    posts_data = []
    for post in posts:
        user = User.query.get(post.user_id)
        likes_count = PostLike.query.filter_by(post_id=post.id).count()
        liked_by_user = PostLike.query.filter_by(post_id=post.id, user_id=current_user_id).first() is not None
        
        posts_data.append({
            "id": post.id,
            "content": post.content,
            "image_url": post.image_url,
            "created_at": post.created_at.isoformat(),
            "user": {
                "id": user.id,
                "username": user.username
            },
            "likes_count": likes_count,
            "liked_by_user": liked_by_user
        })
    
    return jsonify({"posts": posts_data}), 200

@posts_bp.route('/api/posts/<int:post_id>/like', methods=['POST'])
@jwt_required()
def like_post(post_id):
    """Like or unlike a post"""
    user_id = int(get_jwt_identity())
    
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"message": "Post not found"}), 404
    
    existing_like = PostLike.query.filter_by(post_id=post_id, user_id=user_id).first()
    
    if existing_like:
        # Unlike
        db.session.delete(existing_like)
        action = "unliked"
    else:
        # Like
        like = PostLike(post_id=post_id, user_id=user_id)
        db.session.add(like)
        action = "liked"
    
    db.session.commit()
    
    likes_count = PostLike.query.filter_by(post_id=post_id).count()
    
    return jsonify({
        "message": f"Post {action} successfully",
        "likes_count": likes_count,
        "liked_by_user": action == "liked"
    }), 200

@posts_bp.route('/api/posts/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
    """Delete a post"""
    user_id = int(get_jwt_identity())
    
    post = Post.query.filter_by(id=post_id, user_id=user_id).first()
    if not post:
        return jsonify({"message": "Post not found or unauthorized"}), 404
    
    # Delete associated likes first
    PostLike.query.filter_by(post_id=post_id).delete()
    
    # Delete the post
    db.session.delete(post)
    db.session.commit()
    
    return jsonify({"message": "Post deleted successfully"}), 200

@posts_bp.route('/api/posts/photo', methods=['OPTIONS'])
def post_photo_options():
    """Handle CORS preflight for post photo upload"""
    response = jsonify({'status': 'ok'})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With, Accept'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    return response

@posts_bp.route('/api/posts/photo', methods=['POST'])
@jwt_required()
def upload_post_photo():
    """Upload photo for a post"""
    try:
        print(f"🔍 Post photo upload request - Method: {request.method}")
        print(f"🔍 Request headers: {dict(request.headers)}")
        print(f"🔍 Request files: {list(request.files.keys()) if request.files else 'No files'}")
        
        user_id = int(get_jwt_identity())
        print(f"🔍 User ID: {user_id}")
        
        if 'photo' not in request.files:
            return jsonify({"message": "No photo provided"}), 400
        
        file = request.files['photo']
        if file.filename == '':
            return jsonify({"message": "No file selected"}), 400
        
        # Validate file size (5MB limit)
        max_size = 5 * 1024 * 1024  # 5MB
        if file.content_length and file.content_length > max_size:
            return jsonify({"message": "File too large. Maximum size is 5MB"}), 400
        
        if file and allowed_file(file.filename):
            # Generate unique filename
            filename = secure_filename(file.filename)
            unique_filename = f"{user_id}_{uuid.uuid4().hex}_{filename}"
            file_path = os.path.join(UPLOAD_FOLDER, unique_filename)
            
            # Save the file
            file.save(file_path)
            
            # Return the URL that can be accessed
            photo_url = f"/uploads/post_photos/{unique_filename}"
            
            return jsonify({
                "message": "Photo uploaded successfully",
                "photo_url": photo_url
            }), 201
        else:
            return jsonify({"message": "Invalid file type. Allowed: png, jpg, jpeg, gif"}), 400
            
    except Exception as e:
        import traceback
        print(f"🔴 Post photo upload error: {e}")
        print(f"🔴 Full traceback: {traceback.format_exc()}")
        return jsonify({
            "message": "Error uploading photo",
            "error": str(e)
        }), 500 