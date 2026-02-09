#!/bin/bash

# Windows .exe Build Guide for Linux System

# This script generates a detailed guide since true cross-compilation requires Windows

cat > WINDOWS_BUILD_GUIDE.md << 'EOF'

# Building Windows .exe on Windows System

## Option 1: Automated Build (Recommended for Windows Users)

### Prerequisites on Windows

- Python 3.8+ (download from https://www.python.org/downloads/)
  - **IMPORTANT**: Check "Add Python to PATH" during installation
- FFmpeg (optional but recommended)
  - Download from https://ffmpeg.org/download.html
  - Or let yt-dlp auto-download it

### Steps to Build

1. **Extract Project Files**
   - Download the entire project folder
   - Extract to any location (e.g., `C:\Users\YourName\Downloads\youtube-downloader`)

2. **Open Command Prompt**
   - Windows key → type "cmd" → press Enter
   - Navigate to project folder:

   ```cmd
   cd C:\Users\YourName\Downloads\youtube-downloader
   ```

3. **Run Build Script**

   ```cmd
   build-windows.bat
   ```

   This will:
   - Install PyInstaller automatically
   - Build the executable
   - Create folder: `dist\YouTube Downloader.exe`

4. **Find Your .exe**
   ```
   dist\YouTube Downloader.exe
   ```

### Option 2: Manual Step-by-Step Build

```cmd
# Step 1: Install dependencies
pip install --upgrade pip
pip install yt-dlp pyinstaller

# Step 2: Build executable
pyinstaller --onefile --windowed --name "YouTube Downloader" src/main.py

# Step 3: Find the .exe
# Location: dist\YouTube Downloader.exe
```

### Troubleshooting

**Python not found**

- Reinstall Python with "Add Python to PATH" checked
- Restart Command Prompt after installation

**pip command not found**

- Python not in PATH - reinstall with "Add Python to PATH"
- Or use: `python -m pip install ...`

**Build hangs/takes long**

- Normal - first build takes 2-5 minutes
- Don't close the window

**FFmpeg error**

- Download FFmpeg from https://ffmpeg.org/download.html
- Add to Windows PATH or let yt-dlp handle it

## Option 3: Using GitHub Actions to Build Automatically

Create `.github/workflows/build-windows.yml`:

```yaml
name: Build Windows Executable

on: [push]

jobs:
  build:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pyinstaller yt-dlp

      - name: Build executable
        run: |
          pyinstaller --onefile --windowed --name "YouTube Downloader" src/main.py

      - name: Upload artifact
        uses: actions/upload-artifact@v2
        with:
          name: YouTube_Downloader.exe
          path: dist/YouTube Downloader.exe
```

Then push to GitHub and download the .exe from Actions!

## Resulting File

**Location**: `dist/YouTube Downloader.exe`
**Size**: ~100-150 MB (includes Python + all dependencies)
**Requirements**: Windows 7+
**Can run from**: USB drive, network share, anywhere

## Distribution

Share with users:

1. Just the `dist/YouTube Downloader.exe` file
2. Or the entire `dist/` folder
3. Users can run directly - no installation needed!

---

**Note**: This guide is for building ON Windows. If you don't have Windows access, use GitHub Actions above.
EOF

cat WINDOWS_BUILD_GUIDE.md
