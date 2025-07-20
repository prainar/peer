from datetime import datetime
from models.user import db

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text)
    image_url = db.Column(db.LargeBinary)  # Changed from String(500) to LargeBinary to handle base64 images
    post_type = db.Column(db.String(50), default='text')  # 'text', 'photo', 'video'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Post {self.id}>' 