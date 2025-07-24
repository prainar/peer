// API Configuration for different environments
const API_CONFIG = {
  development: {
    baseUrl: 'http://localhost:5000/api',
    description: 'Local development backend'
  },
  production: {
    baseUrl: 'https://peer-backend-yfr4.onrender.com/api',
    description: 'Production backend on Render'
  }
};

// Check for environment variable first, then fall back to environment-based config
const envApiUrl = import.meta.env.VITE_API_URL;
const isProduction = import.meta.env.PROD;
const currentConfig = isProduction ? API_CONFIG.production : API_CONFIG.development;

// Use environment variable if available, otherwise use environment-based config
export const API_URL = envApiUrl || (isProduction ? API_CONFIG.production.baseUrl : API_CONFIG.development.baseUrl);

console.log(`🔧 API Configuration: ${currentConfig.description} (${API_URL})`); 