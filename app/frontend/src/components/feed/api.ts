const API_URL = import.meta.env.PROD 
  ? 'https://peer-backend-yfr4.onrender.com'
  : 'http://localhost:5000';

export const feedApi = {
  getFeed: async () => {
    const response = await fetch(`${API_URL}/feed`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      mode: 'cors',
      credentials: 'omit',
    });
    
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || 'Failed to get feed');
    }
    
    return response.json();
  },

  getFeedByUser: async (userId: number) => {
    const response = await fetch(`${API_URL}/feed/user/${userId}`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      mode: 'cors',
      credentials: 'omit',
    });
    
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || 'Failed to get user feed');
    }
    
    return response.json();
  },
}; 