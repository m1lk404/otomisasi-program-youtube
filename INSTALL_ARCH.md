# Installation Guide for Arch Linux

## System Requirements

- Arch Linux (rolling release)
- Python 3.8 or later
- 4GB RAM minimum
- 500MB free disk space
- Internet connection

## Prerequisites Installation

### Update System

```bash
sudo pacman -Syu
```

### Install Required Packages

```bash
sudo pacman -S \
    python \
    python-pip \
    ffmpeg \
    tk \
    base-devel
```

## Installation Option 1: Automated (Recommended)

### Step 1: Navigate to Project

```bash
cd path/to/otomisasi-program-youtube
```

### Step 2: Run Installation Script

```bash
chmod +x install-arch.sh
./install-arch.sh
```

The script will:

- Update system packages
- Install Python dependencies
- Create launcher in `~/.local/bin/`
- Register desktop application
- Save configuration

### Step 3: Add to PATH (if needed)

If you get "command not found", add this to `~/.bashrc` or `~/.zshrc`:

```bash
export PATH="$PATH:$HOME/.local/bin"
```

Then reload shell:

```bash
source ~/.bashrc  # For bash
# or
source ~/.zshrc   # For zsh
```

### Step 4: Run Application

```bash
youtube-downloader
```

## Installation Option 2: Manual

### Step 1: Clone/Download Project

```bash
cd ~/projects
git clone <repository-url> youtube-downloader
cd youtube-downloader
```

Or if you have a ZIP:

```bash
unzip otomisasi-program-youtube.zip
cd otomisasi-program-youtube
```

### Step 2: Install Dependencies

```bash
pip install --user -r requirements.txt
```

### Step 3: Create Launcher (Optional)

```bash
mkdir -p ~/.local/bin
cat > ~/.local/bin/youtube-downloader << 'EOF'
#!/bin/bash
cd "$HOME/path/to/project"
python3 src/main.py "$@"
EOF

chmod +x ~/.local/bin/youtube-downloader
```

### Step 4: Run

```bash
python3 src/main.py
# or if launcher created:
youtube-downloader
```

## Installation Option 3: System-wide (Advanced)

For installing as a system package:

```bash
cd path/to/project
sudo pip install .
```

Then run as:

```bash
youtube-downloader
```

## Troubleshooting

### "Command not found: python3"

```bash
sudo pacman -S python
python3 --version  # Verify
```

### "ModuleNotFoundError: tkinter"

```bash
sudo pacman -S tk
```

### "yt-dlp not found"

```bash
pip install --user --upgrade yt-dlp
```

### "FFmpeg not found"

```bash
sudo pacman -S ffmpeg
ffmpeg -version  # Verify
```

### GUI doesn't appear

- Ensure Tcl/Tk is installed: `sudo pacman -S tk`
- Try running in terminal to see error: `python3 src/main.py`

### Download authorization errors

```bash
# Try with browser cookies:
# In GUI, select "Chrome" or "Firefox"
# Make sure you're logged in to the browser

# Or manually use yt-dlp:
yt-dlp --cookies-from-browser firefox https://youtube.com/...
```

### Permission denied errors

```bash
# Make sure you have write permission to Downloads
mkdir -p ~/Downloads/YouTube
chmod 755 ~/Downloads/YouTube
```

## Uninstalling

### If installed via install-arch.sh

```bash
rm -rf ~/.local/share/youtube-downloader
rm ~/.local/bin/youtube-downloader
rm ~/.local/share/applications/youtube-downloader.desktop
pip uninstall yt-dlp -y
```

### If installed via pip

```bash
pip uninstall youtube-video-downloader -y
pip uninstall yt-dlp -y
```

### Remove configuration

```bash
rm ~/.youtube_downloader_config.json
```

## Building Standalone Executable

To create a standalone executable:

### Install Build Dependencies

```bash
pip install --user pyinstaller
```

### Build

```bash
cd path/to/project
./build-windows.sh
```

Output will be in `build/linux/dist/`

### Run Standalone

```bash
./build/linux/dist/youtube-downloader
```

## Configuration File

Settings are saved to:

```bash
~/.youtube_downloader_config.json
```

Example content:

```json
{
  "download_path": "/home/user/Downloads/YouTube",
  "quality": "best",
  "cookies_browser": "firefox"
}
```

You can edit this manually if needed.

## Advanced Usage

### Using from Command Line

```bash
python3 src/main.py
```

### Using as Python Module

```python
from src.downloader import YouTubeDownloader

downloader = YouTubeDownloader()
result = downloader.download(
    "https://youtube.com/...",
    {
        'quality': 'best',
        'output_path': '/home/user/Downloads',
        'cookies_browser': 'firefox'
    }
)
```

### Custom Download Directory

Edit `~/.youtube_downloader_config.json`:

```json
{
  "download_path": "/custom/path/to/videos"
}
```

## Updating

To get the latest version:

```bash
cd path/to/project
git pull origin main
# or download latest ZIP and extract

# Update dependencies
pip install --user --upgrade yt-dlp
```

## System Integration

### Desktop Entry (if not auto-created)

Create `~/.local/share/applications/youtube-downloader.desktop`:

```ini
[Desktop Entry]
Version=1.0
Type=Application
Name=YouTube Downloader
Comment=Download YouTube videos with custom quality
Exec=$HOME/.local/bin/youtube-downloader
Icon=media-playback-start
Categories=Utility;
Terminal=false
```

### Add to Application Menu

File above is automatically detected by desktop environments like KDE, GNOME, etc.

## Performance Tips

### For Faster Downloads

1. Use a stable internet connection
2. Close other bandwidth-intensive applications
3. Download during off-peak hours
4. Select appropriate quality (720p is good balance)

### For Large Videos

- 4K videos may take 30+ minutes
- Ensure sufficient disk space
- Don't interrupt the download

## Getting Help

If issues persist:

1. Check the [README.md](README.md)
2. Read the [QUICKSTART.md](QUICKSTART.md)
3. Check yt-dlp documentation: https://yt-dlp.org/
4. Search GitHub issues for similar problems

## Next Steps

Now you're ready! See [QUICKSTART.md](QUICKSTART.md) for your first download!

### Quick Test

```bash
youtube-downloader
```

Download a short video to verify everything works.

---

**Enjoy downloading YouTube videos on Arch Linux!** 🎥
