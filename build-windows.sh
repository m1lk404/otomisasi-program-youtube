#!/bin/bash
# YouTube Downloader Build Script for Windows Executable
# This script builds a standalone .exe file for Windows

set -e

echo "╔═══════════════════════════════════════════════════════╗"
echo "║  YouTube Video Downloader - Windows Build Script      ║"
echo "╚═══════════════════════════════════════════════════════╝"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed"
    echo "   Please install Python3 first"
    exit 1
fi

echo ""
echo "✅ Python found: $(python3 --version)"

echo ""
echo "📥 Installing build dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller

echo ""
echo "🔨 Building Windows executable..."

# Create build directory
mkdir -p build/windows

# Build with PyInstaller
pyinstaller \
    --onefile \
    --windowed \
    --name "YouTube Downloader" \
    --distpath build/windows/dist \
    --buildpath build/windows/build \
    --specpath build/windows \
    --add-data "src:src" \
    --hidden-import=tkinter \
    src/main.py

# Check if build was successful
if [ -f "build/windows/dist/YouTube Downloader" ] || [ -f "build/windows/dist/YouTube Downloader.exe" ]; then
    echo ""
    echo "✅ Build successful!"
    echo ""
    echo "📍 Executable location: build/windows/dist/"
    echo ""
    echo "📦 Contents:"
    ls -lh build/windows/dist/
else
    echo "❌ Build failed"
    exit 1
fi

echo ""
echo "🚀 Next steps:"
echo "   1. Test the executable on a Windows system"
echo "   2. Create an installer if needed"
echo "   3. Users can run the .exe directly (no installation required)"
echo ""
