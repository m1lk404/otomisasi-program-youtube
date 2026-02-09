#!/bin/bash
# YouTube Downloader - Linux Build Strategy
# Multiple build options for different distributions and use cases

set -e

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  YouTube Downloader - Linux Build Strategy                    ║"
echo "╚════════════════════════════════════════════════════════════════╝"

# Detect format requested
BUILD_FORMAT="${1:-standalone}"  # standalone|sh|appimage|all

echo ""
echo "Available build formats:"
echo "  1. standalone - Single ELF binary (current)"
echo "  2. sh - Shell script wrapper with dependencies auto-install"
echo "  3. appimage - AppImage format (works on most Linux distros)"
echo "  4. all - Build all formats"
echo ""

if [ "$BUILD_FORMAT" = "all" ]; then
    BUILD_FORMAT="standalone sh"
fi

build_standalone() {
    echo "📦 Building STANDALONE executable..."
    mkdir -p build/linux/dist
    
    # Use PyInstaller for standalone
    python3 -m PyInstaller \
        --onefile \
        --windowed \
        --name "youtube-downloader" \
        --distpath build/linux/dist/standalone \
        --workpath build/linux/build/standalone \
        --specpath build/linux/spec/standalone \
        --hidden-import=tkinter \
        src/main.py 2>&1 | grep -E "(Bootloader|completed|Build complete)"
    
    chmod +x build/linux/dist/standalone/youtube-downloader
    
    echo "✅ Standalone executable:"
    echo "   Location: build/linux/dist/standalone/youtube-downloader"
    echo "   Size: $(ls -lh build/linux/dist/standalone/youtube-downloader | awk '{print $5}')"
    echo "   Usage: ./build/linux/dist/standalone/youtube-downloader"
}

build_sh_wrapper() {
    echo ""
    echo "📦 Building SH wrapper script..."
    mkdir -p build/linux/dist/sh
    
    cat > build/linux/dist/sh/youtube-downloader.sh << 'SHSCRIPT'
#!/bin/bash
# YouTube Downloader - Linux Wrapper
# Auto-installs dependencies if needed

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found"
    echo "Installing Python3..."
    if command -v pacman &> /dev/null; then
        sudo pacman -S --noconfirm python
    elif command -v apt &> /dev/null; then
        sudo apt update && sudo apt install -y python3
    else
        echo "Please install Python3 manually"
        exit 1
    fi
fi

# Check tkinter
python3 -c "import tkinter" 2>/dev/null || {
    echo "Installing Tkinter..."
    if command -v pacman &> /dev/null; then
        sudo pacman -S --noconfirm tk
    elif command -v apt &> /dev/null; then
        sudo apt install -y python3-tk
    fi
}

# Check FFmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "Installing FFmpeg..."
    if command -v pacman &> /dev/null; then
        sudo pacman -S --noconfirm ffmpeg
    elif command -v apt &> /dev/null; then
        sudo apt install -y ffmpeg
    fi
fi

# Install Python dependencies
pip3 install --user yt-dlp 2>/dev/null || true

# Run application
cd "$PROJECT_DIR"
python3 src/main.py "$@"
SHSCRIPT
    
    chmod +x build/linux/dist/sh/youtube-downloader.sh
    
    echo "✅ Shell wrapper script:"
    echo "   Location: build/linux/dist/sh/youtube-downloader.sh"
    echo "   Auto-installs: Python3, Tkinter, FFmpeg, yt-dlp"
    echo "   Usage: ./build/linux/dist/sh/youtube-downloader.sh"
}

build_appimage() {
    echo ""
    echo "📦 Building AppImage..."
    mkdir -p build/linux/dist/appimage
    
    # Check if linuxdeploy is available
    if ! command -v linuxdeploy &> /dev/null; then
        echo "⚠️  linuxdeploy not found, building simple AppImage..."
        
        # Create AppDir structure
        APPDIR="build/linux/dist/appimage/YouTube_Downloader.AppDir"
        mkdir -p "$APPDIR/usr/bin"
        mkdir -p "$APPDIR/usr/lib"
        mkdir -p "$APPDIR/usr/share/applications"
        
        # Copy executable
        cp build/linux/dist/standalone/youtube-downloader "$APPDIR/usr/bin/"
        
        # Create AppRun script
        cat > "$APPDIR/AppRun" << 'APPRUN'
#!/bin/bash
APPDIR="$(cd "$(dirname "$0")" && pwd)"
export LD_LIBRARY_PATH="$APPDIR/usr/lib:$LD_LIBRARY_PATH"
exec "$APPDIR/usr/bin/youtube-downloader" "$@"
APPRUN
        chmod +x "$APPDIR/AppRun"
        
        # Create desktop entry
        cat > "$APPDIR/youtube-downloader.desktop" << 'DESKTOP'
[Desktop Entry]
Version=1.0
Type=Application
Name=YouTube Downloader
Comment=Download YouTube videos with quality and clip cutting
Exec=youtube-downloader
Icon=media-playback-start
Categories=Utility;
DESKTOP
        
        echo "✅ AppDir structure created:"
        echo "   Location: $APPDIR"
        echo "   To create AppImage, install: appimage-builder"
    else
        echo "Using linuxdeploy to build AppImage..."
        # Advanced AppImage building with linuxdeploy
        echo "⚠️  Advanced AppImage building not yet implemented"
        echo "Please use: appimage-builder (separate tool)"
    fi
}

build_arch_package() {
    echo ""
    echo "📦 Creating Arch Linux PKGBUILD..."
    mkdir -p build/linux/dist/arch
    
    cat > build/linux/dist/arch/PKGBUILD << 'PKGBUILD'
pkgname=youtube-video-downloader
pkgver=1.0.0
pkgrel=1
pkgdesc="YouTube video downloader with clip cutting and best quality selection"
arch=('x86_64')
url="https://github.com/yourusername/youtube-video-downloader"
license=('MIT')
depends=('python' 'python-pip' 'ffmpeg' 'tk')
makedepends=('python-build' 'python-installer' 'python-wheel')
provides=('youtube-video-downloader')

package() {
    cd "$srcdir"
    
    # Install Python dependencies
    pip install --root="$pkgdir" --no-deps yt-dlp
    
    # Install application
    mkdir -p "$pkgdir/opt/youtube-downloader"
    cp -r src/ "$pkgdir/opt/youtube-downloader/"
    cp requirements.txt "$pkgdir/opt/youtube-downloader/"
    
    # Create launcher
    mkdir -p "$pkgdir/usr/bin"
    cat > "$pkgdir/usr/bin/youtube-downloader" << 'EOF'
#!/bin/bash
cd /opt/youtube-downloader
python3 src/main.py "$@"
EOF
    chmod +x "$pkgdir/usr/bin/youtube-downloader"
    
    # Create desktop entry
    mkdir -p "$pkgdir/usr/share/applications"
    cat > "$pkgdir/usr/share/applications/youtube-downloader.desktop" << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=YouTube Downloader
Comment=Download YouTube videos with quality and clip cutting
Exec=youtube-downloader
Icon=media-playback-start
Categories=Utility;
EOF
}
PKGBUILD
    
    echo "✅ PKGBUILD created:"
    echo "   Location: build/linux/dist/arch/PKGBUILD"
    echo ""
    echo "To install on Arch Linux:"
    echo "  cd build/linux/dist/arch"
    echo "  makepkg -si"
}

build_deb_package() {
    echo ""
    echo "📦 Creating Debian/Ubuntu package structure..."
    mkdir -p build/linux/dist/deb
    
    echo "⚠️  Full DEB package creation requires additional tools"
    echo "   Use: fpm or debmake for actual package creation"
}

# Run build based on format
case "$BUILD_FORMAT" in
    standalone)
        build_standalone
        ;;
    sh)
        build_sh_wrapper
        ;;
    appimage)
        build_appimage
        ;;
    "standalone sh")
        build_standalone
        build_sh_wrapper
        ;;
    *)
        echo "Building all formats..."
        build_standalone
        build_sh_wrapper
        echo ""
        echo "Other formats:"
        build_arch_package
        build_deb_package
        ;;
esac

echo ""
echo "════════════════════════════════════════════════════════════════"
echo "📦 BUILD SUMMARY"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "Available outputs:"
[ -d "build/linux/dist/standalone" ] && echo "✅ Standalone: build/linux/dist/standalone/youtube-downloader"
[ -f "build/linux/dist/sh/youtube-downloader.sh" ] && echo "✅ Shell wrapper: build/linux/dist/sh/youtube-downloader.sh"
[ -d "build/linux/dist/appimage" ] && echo "⏳ AppImage: build/linux/dist/appimage/ (partial)"
[ -f "build/linux/dist/arch/PKGBUILD" ] && echo "✅ Arch PKGBUILD: build/linux/dist/arch/PKGBUILD"
echo ""
echo "════════════════════════════════════════════════════════════════"
