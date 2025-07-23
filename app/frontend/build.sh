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

# Create a simple index.html fallback
echo "📋 Creating fallback configuration..."
cat > dist/_redirects << EOF
/*    /index.html   200
EOF

echo "✅ Frontend build completed successfully!"
echo "📁 Build output: dist/" 