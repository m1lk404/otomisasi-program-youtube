#!/bin/bash
# YouTube Downloader - Complete Setup Script
# This script sets up everything needed for development or deployment

set -e

echo "╔═══════════════════════════════════════════════════════╗"
echo "║  YouTube Video Downloader - Setup Script              ║"
echo "╚═══════════════════════════════════════════════════════╝"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found"
    echo "Please install: sudo pacman -S python"
    exit 1
fi

echo ""
echo "✅ Python3: $(python3 --version)"

# Setup virtual environment (optional)
if [ "$1" == "--venv" ]; then
    echo ""
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "✅ Virtual environment activated"
fi

# Install dependencies
echo ""
echo "📥 Installing dependencies..."
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "To run the application:"
echo "  python3 run.py"
echo "  # or"
echo "  python3 -m src.main"
echo ""
echo "To build Windows executable:"
echo "  ./build-windows.sh"
echo ""
echo "To build Linux executable:"
echo "  ./build-linux.sh"
echo ""
echo "To install on Arch Linux:"
echo "  ./install-arch.sh"
echo ""
