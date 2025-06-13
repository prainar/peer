/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/frontend/src/**/*.{js,jsx,ts,tsx}",
    "./app/frontend/public/index.html"
  ],
  theme: {
    extend: {
      colors: {
        primary: '#0070f3',
        secondary: '#1a1a1a',
        accent: '#0070f3',
      },
    },
  },
  plugins: [],
} 