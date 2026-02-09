# YouTube Video Downloader

A feature-rich YouTube video downloader with GUI, clip cutting, and best quality selection.

## Features

✨ **Core Features:**

- Download YouTube videos in best available quality
- Combine best video and audio tracks automatically
- Simple and intuitive GUI
- Auto-cookie extraction from Chrome/Firefox
- Bot blocking protection with retry mechanisms
- Multiple quality options (Best, 1080p, 720p, Audio Only)

🎬 **Clip Cutting:**

- Cut videos from minute to minute
- Specify start and end times in minutes
- Automatic FFmpeg processing

🔒 **Security & Reliability:**

- Bot blocking protection
- Automatic cookie extraction from browsers
- Retry logic with exponential backoff
- Socket timeout handling
- Fragment retry mechanisms

## System Requirements

### Windows

- Windows 7 or later
- FFmpeg (automatically handled by yt-dlp)
- 500 MB free disk space

### Arch Linux

- Python 3.8+
- FFmpeg
- Tcl/Tk (for GUI)
- 500 MB free disk space

## Installation

### Windows (Standalone Executable)

**Option 1: Using Pre-built Executable**

1. Download `YouTube Downloader.exe` from releases
2. Run the executable directly
3. No installation required!

**Option 2: Building from Source**

1. Install Python from https://www.python.org/ (check "Add to PATH")
2. Install FFmpeg from https://ffmpeg.org/download.html
3. Clone/download this repository
4. Open Command Prompt in the project directory
5. Run: `build-windows.bat`
6. The executable will be in `dist\YouTube Downloader.exe`

### Arch Linux

**Option 1: Automated Installation**

```bash
chmod +x install-arch.sh
./install-arch.sh
```

**Option 2: Manual Installation**

```bash
# Install dependencies
sudo pacman -S python python-pip ffmpeg tk

# Install Python dependencies
pip install --user -r requirements.txt

# Run the application
python3 src/main.py
```

**Option 3: Build Standalone Script**

```bash
chmod +x build-windows.sh
./build-windows.sh  # Creates standalone executable
```

## Usage

### Starting the Application

**Windows:**

- Double-click `YouTube Downloader.exe`

**Arch Linux (after installation):**

```bash
youtube-downloader
# Or:
python3 /path/to/src/main.py
```

### Using the GUI

1. **Enter YouTube Link**: Paste a YouTube URL in the "YouTube Link" field
   - Examples: `https://www.youtube.com/watch?v=...`

2. **Select Download Folder**:
   - Click "Browse" to choose where to save videos
   - Default location: `~/Downloads/YouTube`

3. **Optional: Enable Clip Cutting**
   - Check "Enable Clip Cutting (Cut video from minute to minute)"
   - Enter start time (in minutes)
   - Enter end time (optional, leaves blank for to end)
   - Example: Start=5, End=10 cuts from 5 minutes to 10 minutes

4. **Configure Browser Cookies** (optional):
   - Select "None" for no cookie extraction
   - Select "Chrome" if logged into Chrome
   - Select "Firefox" if logged into Firefox
   - Helps bypass some blocking mechanisms

5. **Choose Quality**:
   - **Best**: Highest available quality (recommended)
   - **1080p**: Maximum 1080p video
   - **720p**: Maximum 720p video
   - **Audio Only**: Download audio track only

6. **Click "Start Download"**
   - Progress will be shown in the log window
   - Can click "Cancel" to stop at any time

## Features in Detail

### Bot Blocking Protection

The application includes several anti-bot measures:

- Custom User-Agent spoofing
- Automatic retry with exponential backoff
- Socket timeout handling
- Fragment retry mechanisms
- Cookie extraction from browsers
- Fallback methods for blocked videos

### Clip Cutting

Uses FFmpeg internally to cut videos:

- Specify start time in minutes (e.g., 2.5 for 2 minutes 30 seconds)
- Specify end time in minutes (optional)
- Automatically processes and saves the clipped video

### Quality Selection

- **Best**: Combines the best video and audio tracks automatically
- **1080p**: Highest 1080p available (may have lower audio quality)
- **720p**: Good balance of quality and file size
- **Audio Only**: MP3/M4A format for music

## Troubleshooting

### "yt-dlp not found"

- **Windows**: Reinstall using the installer
- **Linux**: Run `pip install --user yt-dlp`

### Download fails with bot detection

1. Try selecting a browser in "Browser Cookie Handling"
2. Close the browser window you selected (temporarily)
3. Use a VPN if location-blocked
4. Wait a few minutes before retrying

### FFmpeg errors

- **Windows**: Download from https://ffmpeg.org/download.html
- **Arch Linux**: `sudo pacman -S ffmpeg`

### GUI doesn't appear (Linux)

- Ensure Tcl/Tk is installed: `sudo pacman -S tk`
- Try running: `python3 src/main.py`

### Video won't cut properly

- Ensure start time < end time
- Times must be in decimal numbers (e.g., 2.5 not 2:30)
- FFmpeg must be installed and in PATH

## Configuration

Settings are automatically saved to:

- **Windows**: `C:\Users\YourUsername\.youtube_downloader_config.json`
- **Linux**: `~/.youtube_downloader_config.json`

Saved settings:

- Last used download folder
- Preferred quality
- Browser choice for cookies

## Advanced Usage

### Command Line (Linux/Mac)

For development or automation:

```bash
# Direct Python execution
python3 src/main.py

# If installed via install-arch.sh
youtube-downloader
```

### FFmpeg Post-Processing

The application automatically:

1. Downloads the best video track
2. Downloads the best audio track
3. Merges them into MP4 format
4. Applies clip cutting if enabled

## Building for Distribution

### Create Windows Installer

```bash
pip install pyinstaller
pyinstaller --onefile --windowed src/main.py
```

### Create Linux Package

For distribution on Arch Linux:

```bash
# Run the install script which creates:
# - ~/.local/share/youtube-downloader/ (application files)
# - ~/.local/bin/youtube-downloader (launcher script)
# - Desktop entry for application menu
```

## Dependencies

### Core

- **yt-dlp**: YouTube downloader and extractor
- **Python 3.8+**: Application runtime
- **FFmpeg**: Video processing and merging
- **tkinter**: GUI framework (included with Python)

### Build (Windows)

- **PyInstaller**: Creates standalone executables

### Optional

- Chrome/Firefox: For cookie extraction

## Known Limitations

1. Very restricted/private videos may not download
2. Some region-restricted content may not work without proper VPN/cookies
3. Very large videos (4K) may take considerable time
4. Live streams are not supported

## File Formats

Downloaded videos are saved as:

- **Video**: `.mp4` (recommended, most compatible)
- **Alternative**: `.mkv`, `.webm` depending on availability

## Performance

Typical download times:

- 1080p video (~500MB): 5-15 minutes
- 720p video (~300MB): 3-8 minutes
- Audio only (~50MB): 1-3 minutes

Speed depends on:

- Your internet connection
- YouTube server load
- Video availability
- Video resolution

## Updates

To update to the latest version:

**Windows:**

- Download the latest `YouTube Downloader.exe`

**Arch Linux:**

```bash
pip install --user --upgrade yt-dlp
```

## License

This is an educational tool for personal use.

## Disclaimer

This tool is for downloading videos you have the right to download. Respect copyright laws in your jurisdiction. The authors are not responsible for misuse.

## Support

For issues or feature requests:

1. Check the Troubleshooting section
2. Ensure FFmpeg is installed
3. Try running: `pip install --upgrade yt-dlp`

## Technical Details

### Windows Build Process

1. PyInstaller bundles Python, tkinter, and dependencies
2. Creates a single `.exe` file (~100-150MB)
3. No Python installation required on target system
4. FFmpeg is downloaded automatically by yt-dlp

### Arch Linux Installation Process

1. Installs system packages via pacman
2. Installs Python dependencies via pip
3. Creates launcher script in `~/.local/bin/`
4. Registers desktop application
5. Can be uninstalled by removing installed files

## Version

- **Current Version**: 1.0.0
- **Based on**: yt-dlp (latest stable)
- **Python Compatibility**: 3.8+
- **Last Updated**: 2024

---

**Enjoy downloading YouTube videos safely and easily!** 🎥
