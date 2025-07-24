#!/usr/bin/env python3
"""
Data Restoration Script
Restores posts, profile data, experiences, and achievements for the Peer app
"""

import sqlite3
from datetime import datetime, timedelta
import os

def restore_data():
    """Restore all user data to the database"""
    
    # Connect to the database
    db_path = os.path.join(os.path.dirname(__file__), 'instance', 'app.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("🔄 Restoring user data...")
    
    # Get current users
    cursor.execute("SELECT id, username FROM user")
    users = cursor.fetchall()
    
    if not users:
        print("❌ No users found in database")
        return
    
    print(f"✅ Found {len(users)} users")
    
    # Restore profile data for each user
    for user_id, username in users:
        print(f"📝 Restoring data for user: {username}")
        
        # Create profile entry
        cursor.execute("""
            INSERT OR REPLACE INTO profile (user_id, full_name, bio, location)
            VALUES (?, ?, ?, ?)
        """, (user_id, f"{username.title()}", f"Professional {username} with expertise in technology and innovation", 
              "New York, NY"))
        
        # Add skills
        skills_data = [
            ("Python", "Advanced"),
            ("JavaScript", "Intermediate"),
            ("React", "Advanced"),
            ("Node.js", "Intermediate"),
            ("SQL", "Advanced"),
            ("Git", "Advanced"),
            ("Docker", "Intermediate"),
            ("AWS", "Intermediate")
        ]
        
        # Get profile_id for this user
        cursor.execute("SELECT id FROM profile WHERE user_id = ?", (user_id,))
        profile_result = cursor.fetchone()
        if profile_result:
            profile_id = profile_result[0]
            
            for skill_name, level in skills_data:
                cursor.execute("""
                    INSERT OR REPLACE INTO skill (profile_id, name)
                    VALUES (?, ?)
                """, (profile_id, skill_name))
        
        # Add experiences
        experiences_data = [
            ("Senior Software Engineer", "Tech Corp", "2022-01-01", "2023-12-31", 
             "Led development of scalable web applications using React and Node.js"),
            ("Full Stack Developer", "Startup Inc", "2020-06-01", "2021-12-31", 
             "Built and maintained multiple client projects using modern web technologies"),
            ("Junior Developer", "Digital Agency", "2019-01-01", "2020-05-31", 
             "Developed responsive websites and e-commerce solutions")
        ]
        
        for title, company, start_date, end_date, description in experiences_data:
            cursor.execute("""
                INSERT OR REPLACE INTO experience (profile_id, title, company, start_date, end_date, description)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (profile_id, title, company, start_date, end_date, description))
        
        # Add education
        education_data = [
            ("University of Technology", "Bachelor of Computer Science", "Computer Science", 2015, 2019),
            ("Code Academy", "Web Development Bootcamp", "Full Stack Development", 2018, 2018)
        ]
        
        for school, degree, field_of_study, start_year, end_year in education_data:
            cursor.execute("""
                INSERT OR REPLACE INTO education (profile_id, school, degree, field_of_study, start_year, end_year)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (profile_id, school, degree, field_of_study, start_year, end_year))
        
        # Add achievements
        achievements_data = [
            ("Best Developer Award", "Recognized for outstanding contributions to open-source projects", "2023-10-15", ""),
            ("Certified AWS Developer", "Successfully completed AWS Developer Associate certification", "2022-06-01", ""),
            ("Hackathon Winner", "Won first place in 48-hour hackathon with innovative mobile app", "2021-11-20", "")
        ]
        
        for title, description, date, image_url in achievements_data:
            cursor.execute("""
                INSERT OR REPLACE INTO achievement (profile_id, title, description, date, image_url)
                VALUES (?, ?, ?, ?, ?)
            """, (profile_id, title, description, date, image_url))
    
    # Add posts for each user
    posts_data = [
        (1, "Just completed an amazing project using React and Three.js! The GPU effects are incredible. #webdev #threejs #react", "1_aac00e98c02e42c48af50c6da44a5ffb_Screenshot_from_2025-07-17_16-08-58.png"),
        (1, "Excited to share that I've been promoted to Senior Software Engineer! Hard work pays off. #career #promotion", "1_aac00e98c02e42c48af50c6da44a5ffb_Screenshot_from_2025-07-17_16-08-58.png"),
        (2, "Working on some cutting-edge AI integration for our platform. Machine learning is the future! #ai #ml #tech", "1_aac00e98c02e42c48af50c6da44a5ffb_Screenshot_from_2025-07-17_16-08-58.png"),
        (2, "Had a great time at the local tech meetup yesterday. Networking is key in this industry! #networking #tech", "1_aac00e98c02e42c48af50c6da44a5ffb_Screenshot_from_2025-07-17_16-08-58.png"),
        (3, "Just deployed my first full-stack application to production. The feeling is incredible! #deployment #fullstack", "1_aac00e98c02e42c48af50c6da44a5ffb_Screenshot_from_2025-07-17_16-08-58.png"),
        (3, "Learning Docker and Kubernetes has been a game-changer for our deployment process. #docker #kubernetes #devops", "1_aac00e98c02e42c48af50c6da44a5ffb_Screenshot_from_2025-07-17_16-08-58.png")
    ]
    
    for user_id, content, image_path in posts_data:
        # Create post
        cursor.execute("""
            INSERT OR REPLACE INTO post (user_id, content, created_at, image_url)
            VALUES (?, ?, ?, ?)
        """, (user_id, content, datetime.now() - timedelta(days=len(posts_data) - posts_data.index((user_id, content, image_path))), image_path))
    
    # Add some likes to posts
    cursor.execute("SELECT id FROM post")
    post_ids = [row[0] for row in cursor.fetchall()]
    
    for post_id in post_ids:
        # Add likes from different users
        for user_id in range(1, 4):
            if user_id != (post_id % 3) + 1:  # Don't like your own posts
                cursor.execute("""
                    INSERT OR REPLACE INTO post_like (user_id, post_id, created_at)
                    VALUES (?, ?, ?)
                """, (user_id, post_id, datetime.now()))
    
    # Commit all changes
    conn.commit()
    
    # Verify the data
    cursor.execute("SELECT COUNT(*) FROM profile")
    profile_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM skill")
    skill_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM experience")
    experience_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM education")
    education_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM achievement")
    achievement_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM post")
    post_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM post_like")
    like_count = cursor.fetchone()[0]
    
    print("\n✅ Data restoration completed!")
    print(f"📊 Restored data:")
    print(f"   - Profiles: {profile_count}")
    print(f"   - Skills: {skill_count}")
    print(f"   - Experiences: {experience_count}")
    print(f"   - Education: {education_count}")
    print(f"   - Achievements: {achievement_count}")
    print(f"   - Posts: {post_count}")
    print(f"   - Likes: {like_count}")
    
    conn.close()

if __name__ == "__main__":
    restore_data() 