import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import peerLogo from '../../assets/peer.svg';

const Signup: React.FC = () => {
  const [showPassword, setShowPassword] = useState(false);

  return (
    <div className="min-h-screen flex flex-col md:flex-row font-sans">
      {/* Left Panel */}
      <div className="hidden md:flex flex-col justify-center items-center bg-blue-700 w-1/2 p-12 text-white">
        <div className="bg-white rounded-lg flex items-center justify-center mb-6" style={{ width: 64, height: 64 }}>
          <img src={peerLogo} alt="Peer Logo" className="h-12 w-12" />
        </div>
        <h1 className="text-4xl font-bold mb-2">Join Peer</h1>
        <p className="text-lg font-medium">Create your professional profile and connect with others.</p>
      </div>
      {/* Right Panel (Form) */}
      <div className="flex flex-1 flex-col justify-center items-center bg-gray-50">
        <div className="w-full max-w-md p-8 bg-white rounded-lg shadow-lg">
          <div className="flex flex-col items-center mb-6 md:hidden">
            <div className="bg-white rounded-lg flex items-center justify-center mb-2" style={{ width: 48, height: 48 }}>
              <img src={peerLogo} alt="Peer Logo" className="h-8 w-8" />
            </div>
            <h1 className="text-2xl font-bold text-blue-700">Join Peer</h1>
          </div>
          <h2 className="text-3xl font-bold text-center text-gray-900 mb-2">Sign up for Peer</h2>
          <form className="mt-8 space-y-6">
            <div className="rounded-md shadow-sm -space-y-px">
              <div>
                <label htmlFor="name" className="sr-only">Full Name</label>
                <input
                  id="name"
                  name="name"
                  type="text"
                  autoComplete="name"
                  required
                  className="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-blue-600 focus:border-blue-600 focus:z-10 sm:text-base font-sans"
                  placeholder="Full Name"
                />
              </div>
              <div>
                <label htmlFor="email-address" className="sr-only">Email address</label>
                <input
                  id="email-address"
                  name="email"
                  type="email"
                  autoComplete="email"
                  required
                  className="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-blue-600 focus:border-blue-600 focus:z-10 sm:text-base font-sans"
                  placeholder="Email address"
                />
              </div>
              <div className="relative">
                <label htmlFor="password" className="sr-only">Password</label>
                <input
                  id="password"
                  name="password"
                  type={showPassword ? 'text' : 'password'}
                  autoComplete="new-password"
                  required
                  className="appearance-none rounded-none relative block w-full px-3 py-3 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-blue-600 focus:border-blue-600 focus:z-10 sm:text-base font-sans"
                  placeholder="Password"
                />
                <button
                  type="button"
                  className="absolute inset-y-0 right-0 px-3 flex items-center text-sm text-blue-700 hover:underline focus:outline-none"
                  onClick={() => setShowPassword((prev) => !prev)}
                  tabIndex={-1}
                >
                  {showPassword ? 'Hide' : 'Show'}
                </button>
              </div>
            </div>
            <div>
              <button
                type="submit"
                className="group relative w-full flex justify-center py-3 px-4 border border-transparent text-base font-semibold rounded-md text-white bg-blue-700 hover:bg-blue-800 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-600 transition font-sans"
              >
                Agree & Join
              </button>
            </div>
          </form>
          <div className="text-center mt-6">
            <span className="text-gray-600">Already on Peer? </span>
            <Link to="/login" className="text-blue-700 hover:underline font-medium">Sign in</Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Signup; 