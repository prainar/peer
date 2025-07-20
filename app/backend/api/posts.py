from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.post import Post, db
from models.user import User
from datetime import datetime
import base64

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/api/posts', methods=['GET'])
@jwt_required()
def get_posts():
    """Get all posts"""
    posts = Post.query.order_by(Post.created_at.desc()).all()
    
    # Get user data for each post
    result_posts = []
    for post in posts:
        user = User.query.get(post.user_id)
        # Convert LargeBinary to base64 string for frontend
        image_url = None
        if post.image_url:
            try:
                image_url = f"data:image/jpeg;base64,{base64.b64encode(post.image_url).decode('utf-8')}"
            except:
                image_url = None
        
        result_posts.append({
            "id": post.id,
            "content": post.content,
            "image_url": image_url,
            "user_id": post.user_id,
            "user": {
                "id": user.id,
                "username": user.username,
                "name": user.username  # Add name field for frontend compatibility
            },
            "created_at": post.created_at.isoformat(),
            "updated_at": post.updated_at.isoformat() if post.updated_at else None
        })
    
    return jsonify({
        "success": True,
        "posts": result_posts
    }), 200

@posts_bp.route('/api/posts/user/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user_posts(user_id):
    """Get posts by specific user"""
    posts = Post.query.filter_by(user_id=user_id).order_by(Post.created_at.desc()).all()
    
    result_posts = []
    for post in posts:
        user = User.query.get(post.user_id)
        image_url = None
        if post.image_url:
            try:
                image_url = f"data:image/jpeg;base64,{base64.b64encode(post.image_url).decode('utf-8')}"
            except:
                image_url = None
        
        result_posts.append({
            "id": post.id,
            "content": post.content,
            "image_url": image_url,
            "user_id": post.user_id,
            "user": {
                "id": user.id,
                "username": user.username,
                "name": user.username
            },
            "created_at": post.created_at.isoformat(),
            "updated_at": post.updated_at.isoformat() if post.updated_at else None
        })
    
    return jsonify({
        "success": True,
        "posts": result_posts
    }), 200

@posts_bp.route('/api/posts', methods=['POST'])
@jwt_required()
def create_post():
    """Create a new post"""
    current_user_id = get_jwt_identity()
    data = request.get_json()
    
    if not data or not data.get('content'):
        return jsonify({"success": False, "message": "Content is required"}), 400
    
    # Handle image_url if provided
    image_url = None
    if data.get('image_url'):
        try:
            # Remove data URL prefix and decode base64
            if data['image_url'].startswith('data:image'):
                # Extract base64 data
                base64_data = data['image_url'].split(',')[1]
                image_url = base64.b64decode(base64_data)
        except Exception as e:
            return jsonify({"success": False, "message": f"Invalid image data: {str(e)}"}), 400
    
    post = Post(
        user_id=current_user_id,
        content=data['content'],
        image_url=image_url,
        post_type='photo' if image_url else 'text'
    )
    
    try:
        db.session.add(post)
        db.session.commit()
        
        # Get user data for response
        user = User.query.get(current_user_id)
        response_image_url = None
        if post.image_url:
            try:
                response_image_url = f"data:image/jpeg;base64,{base64.b64encode(post.image_url).decode('utf-8')}"
            except:
                response_image_url = None
        
        return jsonify({
            "success": True,
            "message": "Post created successfully",
            "post": {
                "id": post.id,
                "content": post.content,
                "image_url": response_image_url,
                "user_id": post.user_id,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "name": user.username
                },
                "created_at": post.created_at.isoformat(),
                "updated_at": post.updated_at.isoformat() if post.updated_at else None
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "message": f"Error creating post: {str(e)}"}), 500

@posts_bp.route('/api/posts/photo', methods=['POST'])
@jwt_required()
def create_photo_post():
    """Create a photo post"""
    return create_post()

@posts_bp.route('/api/posts/<int:post_id>', methods=['PUT'])
@jwt_required()
def update_post(post_id):
    """Update a post"""
    current_user_id = get_jwt_identity()
    data = request.get_json()
    
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"success": False, "message": "Post not found"}), 404
    
    if post.user_id != current_user_id:
        return jsonify({"success": False, "message": "Unauthorized"}), 403
    
    # Update content if provided
    if data.get('content'):
        post.content = data['content']
    
    # Update image if provided
    if data.get('image_url'):
        try:
            if data['image_url'].startswith('data:image'):
                base64_data = data['image_url'].split(',')[1]
                post.image_url = base64.b64decode(base64_data)
            else:
                post.image_url = None
        except Exception as e:
            return jsonify({"success": False, "message": f"Invalid image data: {str(e)}"}), 400
    
    post.updated_at = datetime.utcnow()
    
    try:
        db.session.commit()
        
        # Get user data for response
        user = User.query.get(current_user_id)
        response_image_url = None
        if post.image_url:
            try:
                response_image_url = f"data:image/jpeg;base64,{base64.b64encode(post.image_url).decode('utf-8')}"
            except:
                response_image_url = None
        
        return jsonify({
            "success": True,
            "message": "Post updated successfully",
            "post": {
                "id": post.id,
                "content": post.content,
                "image_url": response_image_url,
                "user_id": post.user_id,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "name": user.username
                },
                "created_at": post.created_at.isoformat(),
                "updated_at": post.updated_at.isoformat() if post.updated_at else None
            }
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "message": f"Error updating post: {str(e)}"}), 500

@posts_bp.route('/api/posts/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
    """Delete a post"""
    current_user_id = get_jwt_identity()
    
    post = Post.query.get(post_id)
    if not post:
        return jsonify({"success": False, "message": "Post not found"}), 404
    
    if post.user_id != current_user_id:
        return jsonify({"success": False, "message": "Unauthorized"}), 403
    
    try:
        db.session.delete(post)
        db.session.commit()
        return jsonify({"success": True, "message": "Post deleted successfully"}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"success": False, "message": f"Error deleting post: {str(e)}"}), 500 