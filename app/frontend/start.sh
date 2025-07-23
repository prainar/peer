#!/bin/bash

echo "🚀 Starting Frontend Server..."

# Serve the built application
echo "🌐 Serving static files..."
npx serve -s dist -l $PORT

echo "✅ Frontend server started on port $PORT" 