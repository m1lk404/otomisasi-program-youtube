#!/bin/bash
# YouTube Downloader Standalone Build for Linux
# Creates a portable executable that can run on any Linux system

set -e

echo "╔═══════════════════════════════════════════════════════╗"
echo "║  YouTube Video Downloader - Linux Build               ║"
echo "╚═══════════════════════════════════════════════════════╝"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed"
    exit 1
fi

echo ""
echo "✅ Python3 found: $(python3 --version)"

echo ""
echo "📥 Installing build dependencies..."
pip install --user pyinstaller

echo ""
echo "🔨 Building standalone Linux executable..."

# Create build directory
mkdir -p build/linux

# Build with PyInstaller
pyinstaller \
    --onefile \
    --windowed \
    --name "youtube-downloader" \
    --distpath build/linux/dist \
    --buildpath build/linux/build \
    --specpath build/linux \
    --hidden-import=tkinter \
    src/main.py

# Make executable
chmod +x build/linux/dist/youtube-downloader

echo ""
echo "✅ Build successful!"
echo ""
echo "📍 Executable location: build/linux/dist/youtube-downloader"
echo ""
echo "📦 Files:"
ls -lh build/linux/dist/

echo ""
echo "🚀 To run the executable:"
echo "   ./build/linux/dist/youtube-downloader"
echo ""
echo "📦 To distribute:"
echo "   cp build/linux/dist/youtube-downloader /usr/local/bin/"
echo "   chmod +x /usr/local/bin/youtube-downloader"
echo ""
