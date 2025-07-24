import { API_URL } from '../config/api';

export const api = {
  // Auth endpoints
  login: async (credentials: { email: string; password: string }) => {
    const response = await fetch(`${API_URL}/api/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(credentials),
      mode: 'cors',
      credentials: 'omit',
    });
    
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || 'Login failed');
    }
    
    return response.json();
  },

  signup: async (userData: { email: string; password: string; name: string }) => {
    const response = await fetch(`${API_URL}/api/signup`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData),
      mode: 'cors',
      credentials: 'omit',
    });
    
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || 'Signup failed');
    }
    
    return response.json();
  },

  // Profile endpoints
  getProfile: async () => {
    const response = await fetch(`${API_URL}/api/profile`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      mode: 'cors',
      credentials: 'omit',
    });
    
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || 'Failed to get profile');
    }
    
    return response.json();
  },

  updateProfile: async (profileData: any) => {
    const response = await fetch(`${API_URL}/api/profile`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify(profileData),
      mode: 'cors',
      credentials: 'omit',
    });
    
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || 'Failed to update profile');
    }
    
    return response.json();
  },
}; 