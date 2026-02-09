# COMMAND REFERENCE GUIDE

## Quick Command Reference

### 🚀 Running the Application

```bash
# Run GUI directly (requires Python + tkinter)
python3 src/main.py

# Using entry point
python3 run.py

# On Arch Linux (after installation)
youtube-downloader
```

### 🔨 Building Executables

#### Windows

```bash
# Automated build (cross-platform bash)
chmod +x build-windows.sh
./build-windows.sh
# Output: build/windows/dist/YouTube Downloader.exe

# Or Windows native
build-windows.bat
# Run from Command Prompt directly
```

#### Linux

```bash
# Build standalone Linux executable
chmod +x build-linux.sh
./build-linux.sh
# Output: build/linux/dist/youtube-downloader

# Make it executable
chmod +x build/linux/dist/youtube-downloader

# Run standalone
./build/linux/dist/youtube-downloader
```

### 💾 Installing on Arch Linux

```bash
# Automated installation (recommended)
chmod +x install-arch.sh
./install-arch.sh
# Installs to ~/.local/share/youtube-downloader/
# Creates command: youtube-downloader

# Uninstall
rm -rf ~/.local/share/youtube-downloader
rm ~/.local/bin/youtube-downloader
pip uninstall yt-dlp -y
```

### 📦 Development Commands

```bash
# Setup for development
chmod +x setup.sh
./setup.sh

# With virtual environment
./setup.sh --venv

# Install dependencies
pip install -r requirements.txt

# Install with dev tools
pip install -r requirements-dev.txt

# Using Makefile
make install                # Install production deps
make install-dev            # Install with dev tools
make run                    # Run application
make clean                  # Clean build artifacts
make test                   # Run tests
```

### ✅ Verification Commands

```bash
# Check Python syntax
python3 -m py_compile src/*.py

# Test imports
python3 -c "from src.downloader import YouTubeDownloader; print('✅ OK')"

# Check file structure
ls -lah
cd src && ls -lah

# Count lines of code
wc -l src/*.py

# View all Python files
find . -name "*.py" -type f
```

### 📋 Make Commands (if make installed)

```bash
# Show all available commands
make help

# Development setup
make install                # Production dependencies
make install-dev            # Development dependencies
make test                   # Run tests
make clean                  # Clean artifacts

# Running
make run                    # Run the application

# Building
make build-windows          # Build Windows executable
make build-linux            # Build Linux executable
make build-arch             # Install on Arch
make dist                   # Create distribution
```

### 🔍 Troubleshooting Commands

```bash
# Check Python version
python3 --version

# List installed packages
pip list | grep yt-dlp

# Reinstall yt-dlp
pip install --upgrade yt-dlp

# Check FFmpeg
ffmpeg -version

# Test tkinter (GUI)
python3 -m tkinter

# Find yt-dlp location
which yt-dlp
pip show yt-dlp
```

### 📂 File Management Commands

```bash
# Navigate to project
cd /home/m1lk/Project/otomisasi-program-youtube

# View directory structure
tree -a -L 2

# List all files
ls -lah

# View file contents
cat README.md
cat QUICKSTART.md

# Search in files
grep -r "def download" src/

# Count total lines
find src -name "*.py" -exec wc -l {} + | tail -1
```

### 🐍 Python Commands

```bash
# Interactive Python shell
python3

# Run a Python file
python3 main.py

# Execute Python code
python3 -c "import src.downloader; print('Works!')"

# List Python paths
python3 -c "import sys; print(sys.path)"

# Check Python features
python3 -c "import tkinter; print('tkinter available')"
```

### 🔄 Version Management

```bash
# Check yt-dlp version
yt-dlp --version

# Install specific version
pip install yt-dlp==2024.1.0

# Update to latest
pip install --upgrade yt-dlp

# PyInstaller version
pyinstaller --version
```

### 📋 Documentation Commands

```bash
# View main README
cat README.md | less

# View quick start
cat QUICKSTART.md

# View Windows install guide
cat INSTALL_WINDOWS.md | less

# View Arch install guide
cat INSTALL_ARCH.md | less

# View technical docs
cat PROJECT.md | less

# View deployment guide
cat DEPLOYMENT.md | less
```

## Platform-Specific Commands

### Windows (Command Prompt)

```cmd
# Navigate directory
cd C:\path\to\project

# Run Python
python src/main.py

# Run build script
build-windows.bat

# Check files
dir
dir src\

# Delete files
del build-windows.bat
rmdir /s build\

# Set permissions (if needed)
takeown /f file.exe
icacls file.exe /grant Users:F
```

### Arch Linux (Bash)

```bash
# Navigate directory
cd ~/projects/youtube-downloader

# Make files executable
chmod +x *.sh
chmod +x src/*.py

# Install system dependencies
sudo pacman -S python python-pip ffmpeg tk

# Install Python packages
pip install --user yt-dlp

# Run application
python3 src/main.py

# Remove directory
rm -rf ~/projects/youtube-downloader
```

## Installation Commands by Method

### Method 1: From Arch Script

```bash
cd /home/m1lk/Project/otomisasi-program-youtube
chmod +x install-arch.sh
./install-arch.sh
# Now: youtube-downloader
```

### Method 2: Manual Installation

```bash
# Install system packages
sudo pacman -Syu
sudo pacman -S python python-pip ffmpeg tk

# Install Python packages
pip install --user -r requirements.txt

# Run directly
python3 src/main.py
```

### Method 3: System-wide Installation

```bash
sudo pip install .
youtube-downloader
```

### Method 4: Virtual Environment (Dev)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 src/main.py
deactivate
```

## Deployment Commands

### Create Windows Distribution

```bash
# Build executable
./build-windows.sh

# Test executable
./dist/YouTube\ Downloader.exe

# Create installer (optional - requires NSIS/InnoSetup)
makensis installer.nsi
```

### Create Linux Distribution

```bash
# Build standalone executable
./build-linux.sh

# Test executable
./build/linux/dist/youtube-downloader

# Create distribution tarball
tar -czf youtube-downloader-linux.tar.gz build/linux/dist/
```

### Create GitHub Release

```bash
# Tag version
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push tag
git push origin v1.0.0

# Create release on GitHub
# Upload dist files:
# - YouTube_Downloader.exe
# - youtube-downloader-linux
# - Source code
```

## Environment Setup

### Virtual Environment (Optional)

```bash
# Create virtual environment
python3 -m venv venv

# Activate
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Deactivate
deactivate
```

### Environment Variables

```bash
# Set Python path
export PYTHONPATH="${PYTHONPATH}:/home/m1lk/Project/otomisasi-program-youtube"

# Add to PATH
export PATH="$PATH:~/.local/bin"

# Verify
echo $PYTHONPATH
echo $PATH
```

## Debugging Commands

```bash
# Run with verbose output
python3 -v src/main.py

# Run with debugging
python3 -m pdb src/main.py

# Check import errors
python3 -c "import src.main" 2>&1

# View error log
tail -f /tmp/app.log

# Check running processes
ps aux | grep python

# Kill process
kill -9 <PID>
```

## Performance Monitoring

```bash
# Monitor memory usage
python3 -X importtime src/main.py

# Profile execution
python3 -m cProfile src/main.py

# Check file sizes
du -sh *
du -sh src/

# Monitor disk space
df -h

# Check network
ping -c 1 youtube.com
```

## Cleanup Commands

```bash
# Clean Python cache
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type f -name "*.pyc" -delete

# Clean build artifacts
rm -rf build/
rm -rf dist/
rm -rf *.egg-info

# Clean temporary files
rm -f *.tmp *.log *.swp *~

# Full cleanup (careful!)
make clean
```

---

**All commands organized by category for easy reference!** 📚
