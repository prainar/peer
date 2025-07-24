import React from 'react';
import { Link, useLocation } from 'react-router-dom';

const RouteTest: React.FC = () => {
  const location = useLocation();

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="max-w-md w-full space-y-8 p-8 bg-white rounded-lg shadow">
        <h1 className="text-2xl font-bold text-center text-gray-900 mb-6">
          🎉 Route Test Successful!
        </h1>
        
        <div className="text-center mb-6">
          <p className="text-gray-600 mb-2">
            <strong>Current Path:</strong> {location.pathname}
          </p>
          <p className="text-green-600 font-semibold">
            ✅ Client-side routing is working!
          </p>
        </div>

        <div className="space-y-4">
          <h3 className="text-lg font-semibold text-gray-800">Test Navigation:</h3>
          
          <Link 
            to="/login" 
            className="block w-full text-center py-2 px-4 border border-transparent rounded-md shadow-sm font-semibold text-lg bg-blue-600 text-white hover:bg-blue-700"
          >
            Go to Login
          </Link>
          
          <Link 
            to="/signup" 
            className="block w-full text-center py-2 px-4 border border-transparent rounded-md shadow-sm font-semibold text-lg bg-green-600 text-white hover:bg-green-700"
          >
            Go to Signup
          </Link>
          
          <Link 
            to="/dashboard" 
            className="block w-full text-center py-2 px-4 border border-transparent rounded-md shadow-sm font-semibold text-lg bg-purple-600 text-white hover:bg-purple-700"
          >
            Go to Dashboard
          </Link>
          
          <Link 
            to="/" 
            className="block w-full text-center py-2 px-4 border border-gray-300 rounded-md shadow-sm font-semibold text-lg bg-white text-gray-700 hover:bg-gray-50"
          >
            Go to Home
          </Link>
        </div>

        <div className="mt-8 p-4 bg-gray-100 rounded-lg">
          <h4 className="font-semibold text-gray-800 mb-2">Debug Info:</h4>
          <p className="text-sm text-gray-600">
            <strong>Pathname:</strong> {location.pathname}<br/>
            <strong>Search:</strong> {location.search}<br/>
            <strong>Hash:</strong> {location.hash}<br/>
            <strong>Timestamp:</strong> {new Date().toLocaleString()}
          </p>
        </div>
      </div>
    </div>
  );
};

export default RouteTest; 