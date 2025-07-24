// API Configuration for different environments
const API_CONFIG = {
  development: {
    baseUrl: 'http://localhost:5000/api',
    description: 'Local development backend'
  },
  production: {
    baseUrl: 'https://peer-backend.onrender.com/api',
    description: 'Production backend on Render'
  }
};

// Determine which environment to use
const isProduction = import.meta.env.PROD;
const currentConfig = isProduction ? API_CONFIG.production : API_CONFIG.development;

// For now, always use development backend until production is properly deployed
export const API_URL = API_CONFIG.development.baseUrl;

console.log(`🔧 API Configuration: ${currentConfig.description} (${API_URL})`); 