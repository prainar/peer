#!/bin/bash

echo "🚀 Building Frontend for Production..."

# Install dependencies
echo "📦 Installing dependencies..."
npm install

# Build the application
echo "🔨 Building application..."
npm run build

# Copy _redirects to dist folder for client-side routing
echo "📋 Setting up client-side routing..."
cp public/_redirects dist/

# Copy static.json to dist folder
echo "📋 Setting up static configuration..."
cp static.json dist/

# Copy vercel.json to dist folder
echo "📋 Setting up Vercel configuration..."
cp vercel.json dist/

# Copy netlify.toml to dist folder
echo "📋 Setting up Netlify configuration..."
cp netlify.toml dist/

# Create a comprehensive _redirects file
echo "📋 Creating comprehensive redirects..."
cat > dist/_redirects << EOF
# Handle client-side routing for React Router
/*    /index.html   200

# Handle specific routes explicitly
/signup    /index.html   200
/login     /index.html   200
/dashboard /index.html   200
/profile   /index.html   200
/profile/* /index.html   200
/posts     /index.html   200
/posts/*   /index.html   200
/jobs      /index.html   200
/messages  /index.html   200
/three-demo /index.html  200
/test-route /index.html  200

# Handle assets
/assets/*  /assets/:splat  200
EOF

# Create a simple index.html test
echo "📋 Creating test file..."
cat > dist/test.html << EOF
<!DOCTYPE html>
<html>
<head>
    <title>Test Page</title>
</head>
<body>
    <h1>Test Page Works!</h1>
    <p>If you can see this, static file serving is working.</p>
    <a href="/">Go to Home</a>
</body>
</html>
EOF

echo "✅ Frontend build completed successfully!"
echo "📁 Build output: dist/" 