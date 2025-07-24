const API_URL = import.meta.env.PROD 
  ? 'https://peer-backend-yfr4.onrender.com'
  : 'http://localhost:5000';

export const profileApi = {
  getProfile: async () => {
    const response = await fetch(`${API_URL}/api/profile`, {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.json();
  },

  updateProfile: async (profileData: { bio?: string; location?: string; full_name?: string }) => {
    const response = await fetch(`${API_URL}/api/profile`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify(profileData),
    });
    return response.json();
  },

  uploadProfilePhoto: async (photoData: string | FormData) => {
    let response: Response;
    
    if (photoData instanceof FormData) {
      // Handle file upload
      response = await fetch(`${API_URL}/api/profile/photo`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('token')}`,
        },
        body: photoData,
      });
    } else {
      // Handle base64 data URL
      response = await fetch(`${API_URL}/api/profile/photo`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('token')}`,
        },
        body: JSON.stringify({ photo_url: photoData }),
      });
    }
    
    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.message || 'Failed to upload photo');
    }
    
    return response.json();
  },

  removeProfilePhoto: async () => {
    const response = await fetch(`${API_URL}/api/profile/photo`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.json();
  },



  addExperience: async (experienceData: { title: string; company: string; start_date: string; end_date?: string; description: string }) => {
    const response = await fetch(`${API_URL}/api/profile/experience`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify(experienceData),
    });
    return response.json();
  },

  removeExperience: async (experienceId: number) => {
    const response = await fetch(`${API_URL}/api/profile/experience/${experienceId}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.json();
  },

  addAchievement: async (achievementData: { title: string; description: string; date: string }) => {
    const response = await fetch(`${API_URL}/api/profile/achievements`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
      body: JSON.stringify(achievementData),
    });
    return response.json();
  },

  removeAchievement: async (achievementId: number) => {
    const response = await fetch(`${API_URL}/api/profile/achievements/${achievementId}`, {
      method: 'DELETE',
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`,
      },
    });
    return response.json();
  },
}; 