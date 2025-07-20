const API_URL = 'http://localhost:5000/api';

export const postsApi = {
  getAllPosts: async () => {
    const response = await fetch(`${API_URL}/posts`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.json();
  },

  createPost: async (postData: { content?: string; image_url?: string }) => {
    const response = await fetch(`${API_URL}/posts`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify(postData),
    });
    return response.json();
  },

  createPhotoPost: async (postData: { content?: string; image_url: string }) => {
    const response = await fetch(`${API_URL}/posts/photo`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify(postData),
    });
    return response.json();
  },

  updatePost: async (postId: number, postData: { content?: string; image_url?: string }) => {
    const response = await fetch(`${API_URL}/posts/${postId}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify(postData),
    });
    return response.json();
  },

  deletePost: async (postId: number) => {
    const response = await fetch(`${API_URL}/posts/${postId}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.json();
  },

  getUserPosts: async (userId: number) => {
    const response = await fetch(`${API_URL}/posts/user/${userId}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.json();
  },
}; 