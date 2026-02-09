# Installation Guide for Windows

## System Requirements

- Windows 7 or later (Windows 10+ recommended)
- 4GB RAM minimum
- 500MB free disk space
- Internet connection

## Option 1: Using Pre-built Executable (Recommended)

### Step 1: Download

1. Go to [Releases Page](https://github.com/yourusername/youtube-video-downloader/releases)
2. Download `YouTube_Downloader_v1.0_Windows.zip`
3. Extract the ZIP file to a desired location

### Step 2: Run

Double-click `YouTube Downloader.exe`

That's it! No installation needed.

### Step 3: (Optional) Create Desktop Shortcut

1. Right-click on `YouTube Downloader.exe`
2. Select "Send to" > "Desktop (create shortcut)"

## Option 2: Building from Source

### Step 1: Install Requirements

1. Download Python 3.8+ from https://www.python.org/downloads/windows/
2. During installation, **CHECK "Add Python to PATH"**
3. Verify: Open Command Prompt and type `python --version`

### Step 2: Install FFmpeg

1. Download from https://ffmpeg.org/download.html#build-windows
2. Choose "Windows builds"
3. Download the static build (full version recommended)
4. Extract to a folder, then add to system PATH:
   - Open Settings > Environment Variables
   - Add FFmpeg\bin folder to PATH

### Step 3: Clone/Download Project

- Download this repository as ZIP and extract
- Or clone: `git clone <repository-url>`

### Step 4: Build Executable

1. Open Command Prompt
2. Navigate to the project folder: `cd path\to\project`
3. Run: `build-windows.bat`
4. Wait for build to complete (~2-5 minutes)
5. Executable will be in `dist\YouTube Downloader.exe`

## Troubleshooting

### Python not found

- Reinstall Python with "Add Python to PATH" checked
- Restart Command Prompt after installation

### build-windows.bat fails

```bash
# Run manually:
pip install --upgrade pip
pip install yt-dlp pyinstaller
pyinstaller --onefile --windowed src/main.py
```

### "FFmpeg not found"

1. Download FFmpeg from https://ffmpeg.org/download.html
2. Add to PATH as described above
3. Test: Open Command Prompt and type `ffmpeg -version`

### GUI doesn't appear

- Ensure Python tkinter is installed
- Reinstall Python and select "tcl/tk" during installation

### Download fails with "unauthorized"

1. Try enabling cookies: Select "Chrome" or "Firefox"
2. Make sure you're logged in to that browser
3. Close the browser and try again

## Updating

To get the latest version:

1. Download the latest release
2. Extract to the same folder (or new folder)
3. Old configuration will be preserved in `%USERPROFILE%\.youtube_downloader_config.json`

## Uninstalling

Simply delete the folder containing `YouTube Downloader.exe` and the executable.

Configuration files can be deleted from:

- `%USERPROFILE%\.youtube_downloader_config.json`

## Advanced: Using Command Line

Instead of GUI, you can use Python directly:

```bash
python3 -m src.main
```

## System Integration

### Add to Start Menu (Optional)

1. Create a shortcut to `YouTube Downloader.exe`
2. Right-click > Properties
3. Change icon if desired
4. Move shortcut to: `%APPDATA%\Microsoft\Windows\Start Menu\Programs`

### Scheduled Downloads

You can schedule downloads using Windows Task Scheduler:

1. Open Task Scheduler
2. Create Basic Task
3. Set to run: `python path\to\project\src\main.py`

## Getting Help

If you encounter issues:

1. Check the Troubleshooting section above
2. Read the [README.md](README.md)
3. Check video format support on https://yt-dlp.org/

## Next Steps

See [QUICKSTART.md](QUICKSTART.md) to start downloading!
