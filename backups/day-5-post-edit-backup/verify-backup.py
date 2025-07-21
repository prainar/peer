#!/usr/bin/env python3
"""
Backup Verification Script
Verifies that all important files are present in the backup
"""

import os
import sys

def check_file_exists(filepath):
    """Check if a file exists and return status"""
    if os.path.exists(filepath):
        return True, f"✅ {filepath}"
    else:
        return False, f"❌ {filepath} - MISSING"

def main():
    print("🔍 Verifying Day 5 Post Edit Backup...")
    print("=" * 50)
    
    # List of critical files to verify
    critical_files = [
        "app/backend/api/posts.py",
        "app/backend/models/post.py",
        "app/backend/main.py",
        "app/backend/models/user.py",
        "app/backend/models/profile.py",
        "app/frontend/src/components/posts/PostCreate.tsx",
        "app/frontend/src/components/posts/PostList.tsx",
        "app/frontend/src/components/posts/api.ts",
        "app/frontend/src/components/dashboard/Dashboard.tsx",
        "app/backend/uploads/post_photos/",
        "db.sql",
        "BACKUP-README.md"
    ]
    
    all_good = True
    
    for filepath in critical_files:
        exists, message = check_file_exists(filepath)
        print(message)
        if not exists:
            all_good = False
    
    print("=" * 50)
    
    if all_good:
        print("🎉 BACKUP VERIFICATION SUCCESSFUL!")
        print("✅ All critical files are present")
        print("✅ Backup is complete and ready")
    else:
        print("⚠️  BACKUP VERIFICATION FAILED!")
        print("❌ Some critical files are missing")
        sys.exit(1)
    
    # Check file sizes for key files
    print("\n📊 Key File Sizes:")
    key_files = [
        "app/backend/api/posts.py",
        "app/frontend/src/components/posts/PostCreate.tsx",
        "app/frontend/src/components/posts/PostList.tsx"
    ]
    
    for filepath in key_files:
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            print(f"📄 {filepath}: {size:,} bytes")
    
    print("\n🏷️  Git Tag: day-5-post-edit-backup-20250720-212246")
    print("🌿 Branch: day-5-post-edit")
    print("📅 Date: July 20, 2025 - 21:22:46")

if __name__ == "__main__":
    main() 