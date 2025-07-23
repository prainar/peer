import React from 'react';
import { Link } from 'react-router-dom';

const TestRoute: React.FC = () => {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="max-w-md w-full space-y-8 p-8 bg-white rounded-lg shadow">
        <h1 className="text-2xl font-bold text-center text-gray-900 mb-6">
          🎉 Routing Test Successful!
        </h1>
        <p className="text-center text-gray-600 mb-6">
          If you can see this page, client-side routing is working correctly.
        </p>
        <div className="space-y-4">
          <Link 
            to="/login" 
            className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm font-semibold text-lg bg-blue-600 text-white hover:bg-blue-700"
          >
            Go to Login
          </Link>
          <Link 
            to="/signup" 
            className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm font-semibold text-lg bg-green-600 text-white hover:bg-green-700"
          >
            Go to Signup
          </Link>
          <Link 
            to="/" 
            className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm font-semibold text-lg bg-gray-600 text-white hover:bg-gray-700"
          >
            Go to Home
          </Link>
        </div>
      </div>
    </div>
  );
};

export default TestRoute; 