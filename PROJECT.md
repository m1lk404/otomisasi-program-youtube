# PROJECT STRUCTURE & DOCUMENTATION

## Overview

YouTube Video Downloader is a feature-rich application for downloading YouTube videos with support for best quality selection, clip cutting, and browser cookie integration for bypassing some restrictions.

## Technology Stack

- **Language**: Python 3.8+
- **GUI Framework**: Tkinter (cross-platform, built-in with Python)
- **Downloader**: yt-dlp (maintained fork of youtube-dl)
- **Video Processing**: FFmpeg (audio/video merging and cutting)
- **Package Management**: pip, PyInstaller (for .exe building)

## Project Structure

```
otomisasi-program-youtube/
├── src/                          # Source code directory
│   ├── __init__.py               # Package initialization
│   ├── main.py                   # GUI application (tkinter)
│   └── downloader.py             # Core download logic (yt-dlp)
├── build/                        # Build output directory (created during build)
│   ├── windows/                  # Windows build artifacts
│   └── linux/                    # Linux build artifacts
├── dist/                         # Distributions (created by dist target)
├── requirements.txt              # Production dependencies
├── requirements-dev.txt          # Development dependencies
├── setup.py                      # Python package setup
├── setup.cfg                     # Package configuration
├── Makefile                      # Build and development commands
├── run.py                        # Entry point script
├── setup.sh                      # General setup script
├── build-windows.bat             # Windows build script (batch)
├── build-windows.sh              # Windows build script (bash)
├── build-linux.sh                # Linux build script
├── install-arch.sh               # Arch Linux installation script
├── README.md                     # Main documentation
├── QUICKSTART.md                 # Quick start guide
├── INSTALL_WINDOWS.md            # Windows installation guide
├── INSTALL_ARCH.md               # Arch Linux installation guide
├── CONTRIBUTING.md               # Contribution guidelines
├── .gitignore                    # Git ignore rules
└── .youtube_downloader_config.json # User configuration (created at runtime)
```

## Module Descriptions

### src/main.py

**YouTube Downloader GUI Application**

- Main tkinter GUI window
- Input fields: YouTube link, folder selection, clip times
- Options: quality selection, cookie browser choice
- Features: progress tracking, logging, configuration saving
- Classes: `YouTubeDownloaderGUI`
- Dependencies: tkinter, pathlib, threading

### src/downloader.py

**Core Download Functionality**

- yt-dlp wrapper with bot protection
- Handles video quality selection
- Implements clip cutting using FFmpeg
- Browser cookie integration
- Fallback mechanisms for blocked videos
- Classes: `YouTubeDownloader`
- Methods:
  - `download()`: Main method to download videos
  - `_get_format_string()`: Quality format selection
  - `_download_with_fallback()`: Anti-bot fallback
  - `_find_downloaded_file()`: Locate output files

### src/**init**.py

**Package Initialization**

- Exports public classes
- Handles optional imports (GUI requires tkinter)
- Version information

### run.py

**Entry Point Script**

- Cross-platform way to run the application
- Adds src to Python path
- Can be used directly: `python3 run.py`

## Build Setup Files

### Windows

- **build-windows.bat**: Batch script for Windows users
- **build-windows.sh**: Bash script for cross-platform builders
- Uses PyInstaller to create standalone .exe
- Creates ~100-150MB executable with all dependencies

### Arch Linux

- **install-arch.sh**: Automated installation script
  - Installs system packages via pacman
  - Installs Python dependencies via pip
  - Creates launcher scripts and desktop entry
  - User-level installation (no sudo for app)
- **build-linux.sh**: Creates standalone Linux executable
  - Builds portable executable
  - No Python required on target system

### General

- **setup.sh**: General setup for development
- **Makefile**: Convenient commands for development

## Configuration

### User Configuration File

Location: `~/.youtube_downloader_config.json`

```json
{
  "download_path": "/path/to/downloads",
  "quality": "best|1080|720|audio",
  "cookies_browser": "none|chrome|firefox"
}
```

### Build Configuration

- **setup.py**: Python package metadata
- **setup.cfg**: Additional package settings
- **requirements\*.txt**: Dependency specifications

## Key Features

### 1. Video Quality Selection

- **Best**: Combines best video + best audio
- **1080p**: Max 1080p video resolution
- **720p**: Max 720p video resolution
- **Audio Only**: Audio tracks only

### 2. Bot Protection

- User-Agent spoofing
- Automatic retry with backoff
- Socket timeout handling
- Fragment retry mechanisms
- Browser cookie extraction (Chrome/Firefox)
- Fallback download methods

### 3. Clip Cutting

- Specify start and end times (in minutes)
- Uses FFmpeg internally
- Automatic processing
- Decimal support (e.g., 2.5 = 2:30)

### 4. Browser Integration

- Chrome cookie extraction
- Firefox cookie extraction
- Auto-login support
- Helps bypass some restrictions

### 5. Cross-Platform

- Windows (.exe standalone)
- Arch Linux (.sh installer)
- Command-line interface available
- GUI via tkinter

## Dependencies

### Core

- **yt-dlp**: YouTube video downloader
  - Actively maintained fork of youtube-dl
  - Handles bot blocking
  - Supports cookie extraction
- **FFmpeg**: Video processing
  - Merge audio/video streams
  - Clip cutting functionality
  - Format conversion

### GUI

- **tkinter**: Built-in with Python
  - Cross-platform GUI
  - No external dependencies for GUI
  - File dialogs and message boxes

### Build Tools

- **PyInstaller**: Creates standalone executables
- **setuptools/wheel**: Python packaging

## Installation Variants

### Windows

1. **Pre-built .exe** (easiest)
   - Download and run directly
   - No installation needed
2. **Build from source**
   - Install Python + FFmpeg
   - Run build-windows.bat
   - Creates executable

### Arch Linux

1. **Automated script**
   - Run install-arch.sh
   - User-level installation
   - Creates launcher and desktop entry
2. **Manual installation**
   - pacman for system packages
   - pip for Python packages
3. **System-wide installation**
   - `pip install .` as root
   - Installs as system package

## Usage Examples

### GUI Mode

```bash
# Windows
YouTube_Downloader.exe

# Linux
youtube-downloader
# or
python3 src/main.py
```

### Python Module

```python
from src.downloader import YouTubeDownloader

downloader = YouTubeDownloader()
result = downloader.download(
    "https://youtube.com/watch?v=dQw4w9WgXcQ",
    {
        'quality': 'best',
        'output_path': '/home/user/Downloads',
        'cookies_browser': 'firefox',
        'start_time': 2.5,
        'end_time': 7.5
    }
)

if result['success']:
    print(f"Downloaded: {result['filepath']}")
else:
    print(f"Error: {result['error']}")
```

## Development

### Setup

```bash
./setup.sh              # Install dependencies
# or
pip install -r requirements-dev.txt
```

### Building

```bash
make all                # Build everything
make build-windows      # Windows .exe
make build-linux        # Linux executable
make build-arch         # Arch Linux installer
make test              # Run tests (if available)
make clean             # Clean build artifacts
```

### Syntax Check

```bash
python3 -m py_compile src/*.py
```

### File Distribution

```bash
make dist              # Create dist/ folder with all files
```

## Error Handling

### Common Issues & Fixes

| Error                | Cause                 | Solution                 |
| -------------------- | --------------------- | ------------------------ |
| "yt-dlp not found"   | Not installed         | `pip install yt-dlp`     |
| "FFmpeg not found"   | Not installed         | Install from ffmpeg.org  |
| Bot blocking         | YouTube restriction   | Enable cookies, use VPN  |
| Tkinter import error | GUI library missing   | Install tk package       |
| Permission denied    | Download folder issue | Check folder permissions |

## Performance Notes

- Typical download times:
  - 1080p 500MB: 5-15 minutes
  - 720p 300MB: 3-8 minutes
  - Audio 50MB: 1-3 minutes
- Speed varies based on:
  - Internet connection quality
  - YouTube server load
  - Selected quality/resolution

## Security & Privacy

- Local processing only
- No data transmission to external servers
- Configuration stored locally
- Respects YouTube's ToS (for allowed content)
- Cookie extraction from local browser storage only

## Future Enhancements

Potential features:

- [ ] Batch downloading
- [ ] Playlist support
- [ ] Custom audio formats (MP3, WAV, etc.)
- [ ] Metadata tagging
- [ ] Download scheduling
- [ ] Speed limiting
- [ ] Dark mode GUI
- [ ] Multiple language support
- [ ] Automatic updates

## Support & Issues

For problems:

1. Check README.md troubleshooting
2. Review QUICKSTART.md
3. Ensure FFmpeg installed
4. Check yt-dlp version: `yt-dlp --version`
5. Update: `pip install --upgrade yt-dlp`

## License & Disclaimer

- Educational and personal use only
- Respect copyright laws in your jurisdiction
- Not responsible for misuse
- Always check local regulations

## Version Information

- **Version**: 1.0.0
- **Python**: 3.8+
- **yt-dlp**: 2024.1.0+
- **Last Updated**: February 2024

---

**Project Completion Checklist:**

- ✅ Core download functionality
- ✅ GUI with all required features
- ✅ Clip cutting support
- ✅ Cookie automation
- ✅ Quality selection
- ✅ Windows packaging (.exe)
- ✅ Arch Linux packaging (.sh)
- ✅ Bot protection mechanisms
- ✅ Comprehensive documentation
- ✅ Cross-platform support

**Ready for deployment! 🚀**
