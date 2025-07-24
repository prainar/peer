const API_URL = import.meta.env.PROD 
  ? 'https://peer-backend-yfr4.onrender.com'
  : 'http://localhost:5000';

const getAuthHeaders = () => {
  const token = localStorage.getItem('token');
  return {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`
  };
};

const handleResponse = async (response: Response, defaultMessage: string) => {
  if (!response.ok) {
    let errorMessage = defaultMessage;
    try {
      const errorData = await response.json();
      errorMessage = errorData.message || errorMessage;
    } catch (e) {
      console.error('Error parsing error response:', e);
    }
    throw new Error(errorMessage);
  }
  return response.json();
};

export const dashboardApi = {
  // Get user profile
  getProfile: async () => {
    const response = await fetch(`${API_URL}/api/profile`, {
      method: 'GET',
      headers: getAuthHeaders(),
      mode: 'cors',
      credentials: 'omit',
    });
    return handleResponse(response, 'Failed to get profile');
  },

  // Update profile basic info
  updateProfile: async (data: { bio?: string; location?: string }) => {
    const response = await fetch(`${API_URL}/api/profile`, {
      method: 'PUT',
      headers: getAuthHeaders(),
      body: JSON.stringify(data),
      mode: 'cors',
      credentials: 'omit',
    });
    return handleResponse(response, 'Failed to update profile');
  },

  // Add skill
  addSkill: async (name: string) => {
    const response = await fetch(`${API_URL}/api/profile/skills`, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: JSON.stringify({ name }),
      mode: 'cors',
      credentials: 'omit',
    });
    return handleResponse(response, 'Failed to add skill');
  },

  // Remove skill
  removeSkill: async (skillId: number) => {
    const response = await fetch(`${API_URL}/api/profile/skills/${skillId}`, {
      method: 'DELETE',
      headers: getAuthHeaders(),
      mode: 'cors',
      credentials: 'omit',
    });
    return handleResponse(response, 'Failed to remove skill');
  },

  // Add experience
  addExperience: async (data: {
    title: string;
    company: string;
    start_date: string;
    end_date?: string;
    description?: string;
  }) => {
    const response = await fetch(`${API_URL}/api/profile/experience`, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: JSON.stringify(data),
      mode: 'cors',
      credentials: 'omit',
    });
    return handleResponse(response, 'Failed to add experience');
  },

  // Remove experience
  removeExperience: async (expId: number) => {
    const response = await fetch(`${API_URL}/api/profile/experience/${expId}`, {
      method: 'DELETE',
      headers: getAuthHeaders(),
      mode: 'cors',
      credentials: 'omit',
    });
    return handleResponse(response, 'Failed to remove experience');
  },

  // Add achievement
  addAchievement: async (data: {
    title: string;
    description?: string;
    date?: string;
    image_url?: string;
  }) => {
    const response = await fetch(`${API_URL}/api/profile/achievements`, {
      method: 'POST',
      headers: getAuthHeaders(),
      body: JSON.stringify(data),
      mode: 'cors',
      credentials: 'omit',
    });
    return handleResponse(response, 'Failed to add achievement');
  },

  // Remove achievement
  removeAchievement: async (achievementId: number) => {
    const response = await fetch(`${API_URL}/api/profile/achievements/${achievementId}`, {
      method: 'DELETE',
      headers: getAuthHeaders(),
      mode: 'cors',
      credentials: 'omit',
    });
    return handleResponse(response, 'Failed to remove achievement');
  },
};