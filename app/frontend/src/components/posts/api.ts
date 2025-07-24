const API_URL = import.meta.env.PROD 
  ? 'https://peer-backend-yfr4.onrender.com'
  : 'http://localhost:5000';

export const postsApi = {
  createPost: async (content: string, imageUrl?: string) => {
    const response = await fetch(`${API_URL}/api/posts`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify({ content, image_url: imageUrl }),
    });
    return response.json();
  },

  getPosts: async () => {
    const response = await fetch(`${API_URL}/api/posts`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.json();
  },

  getUserPosts: async (userId: number) => {
    const response = await fetch(`${API_URL}/api/posts/user/${userId}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.json();
  },

  likePost: async (postId: number) => {
    const response = await fetch(`${API_URL}/api/posts/${postId}/like`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.json();
  },

  deletePost: async (postId: number) => {
    const response = await fetch(`${API_URL}/api/posts/${postId}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.json();
  },

  uploadPhoto: async (formData: FormData) => {
    console.log('🔍 Uploading post photo: FormData');
    console.log('🔍 Token:', localStorage.getItem('token') ? 'Present' : 'Missing');
    
    const response = await fetch(`${API_URL}/api/posts/photo`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      body: formData,
      mode: 'cors',
      credentials: 'omit',
    });
    
    console.log('🔍 Post photo upload response status:', response.status);
    
    if (!response.ok) {
      let errorMessage = 'Failed to upload photo';
      try {
        const errorData = await response.json();
        errorMessage = errorData.message || errorMessage;
        console.log('🔍 Post photo upload error data:', errorData);
      } catch (e) {
        console.error('Error parsing error response:', e);
      }
      throw new Error(errorMessage);
    }
    
    const result = await response.json();
    console.log('🔍 Post photo upload success:', result);
    return result;
  },
}; 