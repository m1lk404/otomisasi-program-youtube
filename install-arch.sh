#!/bin/bash
# YouTube Downloader Installer for Arch Linux
# This script installs all dependencies and sets up the application

set -e

echo "╔═══════════════════════════════════════════════════════╗"
echo "║  YouTube Video Downloader - Arch Linux Installation   ║"
echo "╚═══════════════════════════════════════════════════════╝"

# Check if running on Arch Linux
if ! [ -f /etc/arch-release ]; then
    echo "❌ This script is designed for Arch Linux"
    exit 1
fi

INSTALL_DIR="$HOME/.local/share/youtube-downloader"
BIN_DIR="$HOME/.local/bin"

echo ""
echo "📦 Updating system packages..."
sudo pacman -Syu --noconfirm

echo ""
echo "📥 Installing dependencies..."
# Install Python and required packages
sudo pacman -S --noconfirm \
    python \
    python-pip \
    ffmpeg \
    tk  # Required for tkinter (Tcl/Tk)

echo ""
echo "📂 Creating installation directory..."
mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"

echo ""
echo "📋 Installing Python dependencies..."
pip install --user -r requirements.txt

echo ""
echo "📋 Creating launcher script..."
cat > "$BIN_DIR/youtube-downloader" << 'LAUNCHER'
#!/bin/bash
# YouTube Downloader Launcher

SCRIPT_DIR="$HOME/.local/share/youtube-downloader"
cd "$SCRIPT_DIR" || exit 1

python3 src/main.py "$@"
LAUNCHER

chmod +x "$BIN_DIR/youtube-downloader"

echo ""
echo "📋 Creating desktop entry..."
mkdir -p "$HOME/.local/share/applications"
cat > "$HOME/.local/share/applications/youtube-downloader.desktop" << 'DESKTOP'
[Desktop Entry]
Version=1.0
Type=Application
Name=YouTube Downloader
Comment=Download YouTube videos with custom quality and clip cutting
Exec=$HOME/.local/bin/youtube-downloader
Icon=preferences-system-network-proxy
Categories=Utility;
Terminal=false
DESKTOP

echo ""
echo "📋 Copying application files..."
cp -r src/ "$INSTALL_DIR/"
cp requirements.txt "$INSTALL_DIR/"

echo ""
echo "✅ Installation complete!"
echo ""
echo "📍 Application installed at: $INSTALL_DIR"
echo ""
echo "🚀 To run the application:"
echo "   youtube-downloader"
echo ""
echo "   Or if the command doesn't work, run:"
echo "   python3 $INSTALL_DIR/src/main.py"
echo ""
echo "💡 Make sure ~/.local/bin is in your PATH:"
echo "   export PATH=\$PATH:\$HOME/.local/bin"
echo ""
echo "To remove the installation later:"
echo "   rm -rf $INSTALL_DIR"
echo "   rm $BIN_DIR/youtube-downloader"
echo "   rm $HOME/.local/share/applications/youtube-downloader.desktop"
echo "   pip uninstall yt-dlp -y"
