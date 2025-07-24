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

# Copy netlify.toml to dist folder
echo "📋 Setting up netlify configuration..."
cp netlify.toml dist/

# Create a comprehensive _redirects file in dist
echo "📋 Creating comprehensive redirects..."
cat > dist/_redirects << 'EOF'
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

# Handle assets with proper caching
/assets/*  /assets/:splat  200

# Handle API routes (should not be redirected)
/api/*     /api/:splat    200

# Handle static files
*.js       /index.html    200
*.css      /index.html    200
*.png      /index.html    200
*.jpg      /index.html    200
*.jpeg     /index.html    200
*.gif      /index.html    200
*.svg      /index.html    200
*.ico      /index.html    200

# Fallback for everything else
/*         /index.html    200
EOF

# Create a simple index.html fallback for testing
echo "📋 Creating test index.html..."
cat > dist/test.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>Test Page</title>
</head>
<body>
    <h1>Test Page Works!</h1>
    <p>If you can see this, the static hosting is working.</p>
    <a href="/">Go to main app</a>
</body>
</html>
EOF

# Verify all files are present
echo "📋 Verifying build output..."
ls -la dist/

echo "✅ Frontend build completed successfully!"
echo "📁 Build output: dist/" 