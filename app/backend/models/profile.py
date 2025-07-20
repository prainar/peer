from datetime import datetime
from models.user import db

class Profile(db.Model):
    __tablename__ = 'profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    bio = db.Column(db.Text)
    location = db.Column(db.String(100))
    website = db.Column(db.String(200))
    profile_photo = db.Column(db.LargeBinary)
    achievements = db.Column(db.Text)  # JSON string of achievements
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Profile {self.id}>'

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    name = db.Column(db.String(80), nullable=False)

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    company = db.Column(db.String(120), nullable=False)
    start_date = db.Column(db.String(50))  # Changed to string to handle various date formats
    end_date = db.Column(db.String(50))    # Changed to string to handle various date formats
    description = db.Column(db.Text)

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    school = db.Column(db.String(120), nullable=False)
    degree = db.Column(db.String(120))
    field_of_study = db.Column(db.String(120))
    start_year = db.Column(db.Integer)
    end_year = db.Column(db.Integer)

class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    date = db.Column(db.String(50))  # Changed to string to handle various date formats
    image_url = db.Column(db.String(255))  # Optional photo for achievement

class ProfilePhoto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    url = db.Column(db.Text, nullable=False)  # Changed to TEXT to handle large base64 data
    uploaded_at = db.Column(db.DateTime, server_default=db.func.now())
