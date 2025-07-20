import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { profileApi } from './api';
import { postsApi } from '../posts/api';

interface Experience {
  id: number;
  title: string;
  company: string;
  start_date: string;
  end_date?: string;
  description: string;
}

interface Achievement {
  id: number;
  title: string;
  description: string;
  date: string;
  image_url?: string;
}

interface Post {
  id: number;
  content: string;
  image_url?: string;
  user_id: number;
  created_at: string;
  user: {
    id: number;
    username: string;
  };
}

interface ProfileData {
  profile: {
    id: number;
    full_name: string;
    bio: string;
    location: string;
    experience: Experience[];
    education: any[];
    achievements: Achievement[];
    photos: any[];
  };
  user: {
    id: number;
    username: string;
    email: string;
  };
}

const ProfileView: React.FC = () => {
  const navigate = useNavigate();
  const [profileData, setProfileData] = useState<ProfileData | null>(null);
  const [loading, setLoading] = useState(true);
  const [expandedSections, setExpandedSections] = useState({
    experience: true,
    achievements: true,
    photos: true,
    posts: true
  });
  const [userPosts, setUserPosts] = useState<Post[]>([]);
  const [newPost, setNewPost] = useState<File | null>(null);
  const [postContent, setPostContent] = useState('');
  const [uploadingPost, setUploadingPost] = useState(false);
  const [showPostForm, setShowPostForm] = useState(false);

  useEffect(() => {
    loadProfile();
    loadUserPosts();
  }, []);

  const loadProfile = async () => {
    try {
      const data = await profileApi.getProfile();
      setProfileData(data);
    } catch (error) {
      console.error('Error loading profile:', error);
    } finally {
      setLoading(false);
    }
  };

  const loadUserPosts = async () => {
    try {
      const data = await profileApi.getProfile();
      const posts = await postsApi.getUserPosts(data.user.id);
      setUserPosts(posts.posts || []);
    } catch (error) {
      console.error('Error loading user posts:', error);
    }
  };

  const handlePostUpload = async () => {
    if (!newPost || !profileData) return;
    
    setUploadingPost(true);
    try {
      // Convert file to base64
      const reader = new FileReader();
      reader.onload = async (e) => {
        const base64 = e.target?.result as string;
        await postsApi.createPhotoPost({
          content: postContent,
          image_url: base64
        });
        setNewPost(null);
        setPostContent('');
        setShowPostForm(false);
        await loadUserPosts();
      };
      reader.readAsDataURL(newPost);
    } catch (error) {
      console.error('Error uploading post:', error);
    } finally {
      setUploadingPost(false);
    }
  };

  const handleTextPost = async () => {
    if (!postContent.trim() || !profileData) return;
    
    setUploadingPost(true);
    try {
      await postsApi.createPost({
        content: postContent
      });
      setPostContent('');
      setShowPostForm(false);
      await loadUserPosts();
    } catch (error) {
      console.error('Error creating text post:', error);
    } finally {
      setUploadingPost(false);
    }
  };

  const handleDeletePost = async (postId: number) => {
    try {
      await postsApi.deletePost(postId);
      await loadUserPosts();
    } catch (error) {
      console.error('Error deleting post:', error);
    }
  };

  const toggleSection = (section: string) => {
    setExpandedSections(prev => ({
      ...prev,
      [section]: !prev[section as keyof typeof prev]
    }));
  };

  const getInitials = (name: string) => {
    return name.split(' ').map(n => n[0]).join('').toUpperCase();
  };

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  if (loading) {
    return (
      <div className="max-w-4xl mx-auto p-4">
        <div className="bg-white rounded-lg shadow p-6">
          <div className="animate-pulse">
            <div className="h-8 bg-gray-200 rounded w-1/3 mb-4"></div>
            <div className="h-4 bg-gray-200 rounded w-1/2 mb-2"></div>
            <div className="h-4 bg-gray-200 rounded w-2/3"></div>
          </div>
        </div>
      </div>
    );
  }

  if (!profileData) {
    return (
      <div className="max-w-4xl mx-auto p-4">
        <div className="bg-white rounded-lg shadow p-6">
          <p className="text-red-500">Failed to load profile data</p>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto p-4">
      {/* Profile Header */}
      <div className="bg-white rounded-lg shadow mb-6">
        <div className="relative">
          {/* Cover Image Placeholder */}
          <div className="h-48 rounded-t-lg" style={{ background: 'linear-gradient(135deg, #8B4513 0%, #6d3410 100%)' }}></div>
          
          {/* Avatar and Basic Info */}
          <div className="relative px-6 pb-6">
            <div className="flex flex-col sm:flex-row sm:items-end sm:justify-between">
              <div className="flex items-end space-x-4 -mt-16">
                {profileData.profile.photos.length > 0 ? (
                  <div className="relative">
                    <img
                      src={profileData.profile.photos[0].url}
                      alt="Profile Picture"
                      className="w-32 h-32 rounded-full object-cover border-4 border-white shadow-lg"
                    />
                  </div>
                ) : (
                  <div className="w-32 h-32 rounded-full flex items-center justify-center border-4 border-white shadow-lg" style={{ backgroundColor: '#8B4513' }}>
                    <span className="text-4xl font-bold text-white">
                      {getInitials(profileData.profile.full_name || profileData.user.username)}
                    </span>
                  </div>
                )}
                <div className="mb-4">
                  <h1 className="text-3xl font-bold text-gray-900">{profileData.profile.full_name || profileData.user.username}</h1>
                  <p className="text-xl text-gray-600">{profileData.user.email}</p>
                  <p className="text-gray-500">📍 {profileData.profile.location || 'Location not set'}</p>
                </div>
              </div>
              
              {/* Edit Profile Button */}
              <div className="flex space-x-3 mt-4 sm:mt-0">
                <button
                  onClick={() => navigate('/profile/edit')}
                  className="px-4 py-2 text-white rounded-md hover:brightness-90 transition-colors"
                  style={{ backgroundColor: '#8B4513' }}
                >
                  Edit Profile
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left Column */}
        <div className="lg:col-span-2 space-y-6">
          {/* About Section */}
          {profileData.profile.bio && (
            <div className="bg-white rounded-lg shadow p-6">
              <h2 className="text-xl font-semibold mb-4" style={{ color: '#8B4513' }}>About</h2>
              <p className="text-gray-700 leading-relaxed">{profileData.profile.bio}</p>
            </div>
          )}

          {/* Posts Section */}
          <div className="bg-white rounded-lg shadow">
            <div className="p-6 border-b">
              <div className="flex items-center justify-between">
                <h2 className="text-xl font-semibold" style={{ color: '#8B4513' }}>📝 My Posts</h2>
                <div className="flex items-center space-x-2">
                  <button
                    onClick={() => setShowPostForm(!showPostForm)}
                    className="px-4 py-2 text-white rounded-md hover:brightness-90 transition-colors"
                    style={{ backgroundColor: '#8B4513' }}
                  >
                    {showPostForm ? 'Cancel' : 'Create Post'}
                  </button>
                  <button
                    onClick={() => toggleSection('posts')}
                    className="text-gray-500 hover:text-gray-700"
                  >
                    {expandedSections.posts ? '▼' : '▶'}
                  </button>
                </div>
              </div>
            </div>
            
            {/* Post Creation Form */}
            {showPostForm && (
              <div className="p-6 border-b bg-gray-50">
                <div className="space-y-4">
                  <div className="space-y-2">
                    <label className="block text-sm font-medium text-gray-700">💬 What's on your mind?</label>
                    <textarea
                      value={postContent}
                      onChange={(e) => setPostContent(e.target.value)}
                      placeholder="Share your thoughts, updates, or experiences..."
                      rows={3}
                      className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2"
                      style={{ '--tw-ring-color': '#8B4513' } as React.CSSProperties}
                    />
                  </div>
                  
                  <div className="space-y-2">
                    <label className="block text-sm font-medium text-gray-700">📸 Add Photo (Optional)</label>
                    <input
                      type="file"
                      accept="image/*"
                      onChange={(e) => setNewPost(e.target.files?.[0] || null)}
                      className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-medium file:text-white file:bg-blue-600 hover:file:bg-blue-700"
                      style={{ border: '2px solid #8B4513', borderRadius: '8px', padding: '8px', backgroundColor: 'white' }}
                    />
                  </div>
                  
                  {newPost && (
                    <div className="p-3 bg-white rounded-lg border">
                      <p className="text-sm font-medium text-gray-700 mb-2">📸 Photo Preview:</p>
                      <img
                        src={URL.createObjectURL(newPost)}
                        alt="Preview"
                        className="w-32 h-32 object-cover border shadow-sm rounded"
                      />
                      <p className="text-xs text-gray-500 mt-1">{newPost.name}</p>
                    </div>
                  )}
                  
                  <div className="flex space-x-3">
                    <button
                      onClick={newPost ? handlePostUpload : handleTextPost}
                      disabled={uploadingPost || (!postContent.trim() && !newPost)}
                      className="px-4 py-2 text-white rounded-md hover:brightness-90 transition-colors disabled:opacity-50"
                      style={{ backgroundColor: '#8B4513' }}
                    >
                      {uploadingPost ? 'Posting...' : 'Post'}
                    </button>
                    <button
                      onClick={() => {
                        setNewPost(null);
                        setPostContent('');
                        setShowPostForm(false);
                      }}
                      className="px-4 py-2 text-gray-600 border border-gray-300 rounded-md hover:bg-gray-50"
                    >
                      Cancel
                    </button>
                  </div>
                </div>
              </div>
            )}
            
            {/* Posts Feed */}
            {expandedSections.posts && (
              <div className="p-6">
                {userPosts.length > 0 ? (
                  <div className="space-y-6">
                    {userPosts.map((post) => (
                      <div key={post.id} className="border border-gray-200 rounded-lg p-4">
                        <div className="flex justify-between items-start mb-3">
                          <div className="flex items-center space-x-3">
                            {profileData.profile.photos.length > 0 ? (
                              <img
                                src={profileData.profile.photos[0].url}
                                alt="Profile"
                                className="w-10 h-10 rounded-full object-cover"
                              />
                            ) : (
                              <div className="w-10 h-10 rounded-full flex items-center justify-center" style={{ backgroundColor: '#8B4513' }}>
                                <span className="text-sm font-bold text-white">
                                  {getInitials(profileData.profile.full_name || profileData.user.username)}
                                </span>
                              </div>
                            )}
                            <div>
                              <p className="font-semibold">{profileData.profile.full_name || profileData.user.username}</p>
                              <p className="text-sm text-gray-500">{formatDate(post.created_at)}</p>
                            </div>
                          </div>
                          <button
                            onClick={() => handleDeletePost(post.id)}
                            className="text-red-600 hover:text-red-800 text-sm"
                          >
                            Delete
                          </button>
                        </div>
                        
                        {post.content && (
                          <p className="text-gray-700 mb-3">{post.content}</p>
                        )}
                        
                        {post.image_url && (
                          <div className="mb-3">
                            <img
                              src={post.image_url}
                              alt="Post image"
                              className="w-full max-w-md rounded-lg shadow-sm"
                            />
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                ) : (
                  <p className="text-gray-500 italic text-center py-8">No posts yet. Create your first post above!</p>
                )}
              </div>
            )}
          </div>

          {/* Experience Section */}
          <div className="bg-white rounded-lg shadow">
            <div className="p-6 border-b">
              <div className="flex items-center justify-between">
                <h2 className="text-xl font-semibold" style={{ color: '#8B4513' }}>Experience</h2>
                <button
                  onClick={() => toggleSection('experience')}
                  className="text-gray-500 hover:text-gray-700"
                >
                  {expandedSections.experience ? '▼' : '▶'}
                </button>
              </div>
            </div>
            
            {expandedSections.experience && (
              <div className="p-6">
                {profileData.profile.experience.length > 0 ? (
                  <div className="space-y-6">
                    {profileData.profile.experience.map((exp) => (
                      <div key={exp.id} className="border-l-4 pl-4" style={{ borderColor: '#8B4513' }}>
                        <h3 className="font-semibold text-lg">{exp.title}</h3>
                        <p className="text-gray-600">{exp.company}</p>
                        <p className="text-sm text-gray-500">
                          {exp.start_date} - {exp.end_date || 'Present'}
                        </p>
                        {exp.description && (
                          <p className="text-gray-700 mt-2">{exp.description}</p>
                        )}
                      </div>
                    ))}
                  </div>
                ) : (
                  <p className="text-gray-500 italic">No experience added yet.</p>
                )}
              </div>
            )}
          </div>

          {/* Achievements Section */}
          <div className="bg-white rounded-lg shadow">
            <div className="p-6 border-b">
              <div className="flex items-center justify-between">
                <h2 className="text-xl font-semibold" style={{ color: '#8B4513' }}>Achievements</h2>
                <button
                  onClick={() => toggleSection('achievements')}
                  className="text-gray-500 hover:text-gray-700"
                >
                  {expandedSections.achievements ? '▼' : '▶'}
                </button>
              </div>
            </div>
            
            {expandedSections.achievements && (
              <div className="p-6">
                {profileData.profile.achievements.length > 0 ? (
                  <div className="space-y-4">
                    {profileData.profile.achievements.map((achievement) => (
                      <div key={achievement.id} className="border border-gray-200 rounded-lg p-4">
                        <h3 className="font-semibold">{achievement.title}</h3>
                        <p className="text-sm text-gray-500">{achievement.date}</p>
                        {achievement.description && (
                          <p className="text-gray-700 mt-2">{achievement.description}</p>
                        )}
                      </div>
                    ))}
                  </div>
                ) : (
                  <p className="text-gray-500 italic">No achievements added yet.</p>
                )}
              </div>
            )}
          </div>

          {/* Photos Section */}
          {profileData.profile.photos.length > 1 && (
            <div className="bg-white rounded-lg shadow">
              <div className="p-6 border-b">
                <div className="flex items-center justify-between">
                  <h2 className="text-xl font-semibold" style={{ color: '#8B4513' }}>Additional Photos</h2>
                  <button
                    onClick={() => toggleSection('photos')}
                    className="text-gray-500 hover:text-gray-700"
                  >
                    {expandedSections.photos ? '▼' : '▶'}
                  </button>
                </div>
              </div>
              
              {expandedSections.photos && (
                <div className="p-6">
                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    {profileData.profile.photos.slice(1).map((photo) => (
                      <div key={photo.id} className="border border-gray-200 rounded-lg overflow-hidden">
                        <img
                          src={photo.url}
                          alt="Profile Photo"
                          className="w-full h-48 object-cover"
                        />
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}
        </div>

        {/* Right Column */}
        <div className="space-y-6">
          {/* Contact Info */}
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-xl font-semibold mb-4" style={{ color: '#8B4513' }}>Contact</h2>
            <div className="space-y-2">
              <p className="text-gray-700">
                <span className="font-medium">Email:</span> {profileData.user.email}
              </p>
              <p className="text-gray-700">
                <span className="font-medium">Username:</span> {profileData.user.username}
              </p>
            </div>
          </div>

          {/* Quick Stats */}
          <div className="bg-white rounded-lg shadow p-6">
            <h2 className="text-xl font-semibold mb-4" style={{ color: '#8B4513' }}>Profile Stats</h2>
            <div className="space-y-3">
              <div className="flex justify-between">
                <span className="text-gray-600">Experience Entries:</span>
                <span className="font-semibold">{profileData.profile.experience.length}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Achievements:</span>
                <span className="font-semibold">{profileData.profile.achievements.length}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Photos:</span>
                <span className="font-semibold">{profileData.profile.photos.length}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-gray-600">Posts:</span>
                <span className="font-semibold">{userPosts.length}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ProfileView;