// Utility function to convert relative image URLs to full URLs
const API_BASE_URL = import.meta.env.PROD 
  ? 'https://peer-backend-yfr4.onrender.com'
  : 'http://localhost:5000';

export const getFullImageUrl = (relativeUrl: string): string => {
  if (!relativeUrl) return '';
  
  // If it's already a full URL, return as is
  if (relativeUrl.startsWith('http://') || relativeUrl.startsWith('https://')) {
    return relativeUrl;
  }
  
  // If it's a data URL, return as is
  if (relativeUrl.startsWith('data:')) {
    return relativeUrl;
  }
  
  // Convert relative URL to full URL
  if (relativeUrl.startsWith('/')) {
    return `${API_BASE_URL}${relativeUrl}`;
  }
  
  // If it doesn't start with /, add it
  return `${API_BASE_URL}/${relativeUrl}`;
};

export const getImageUrl = (imageUrl: string | null | undefined): string => {
  if (!imageUrl) return '';
  return getFullImageUrl(imageUrl);
}; 