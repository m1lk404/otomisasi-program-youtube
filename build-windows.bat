@echo off
REM YouTube Downloader Installer for Windows
REM This script installs all dependencies and sets up the application

setlocal enabledelayedexpansion

echo.
echo ╔═══════════════════════════════════════════════════════╗
echo ║  YouTube Video Downloader - Windows Installation      ║
echo ╚═══════════════════════════════════════════════════════╝
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo    Please install Python from https://www.python.org/
    echo    Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo ✅ Python found: 
python --version

echo.
echo 📥 Installing Python dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo.
echo 📥 Installing PyInstaller for building executable...
pip install pyinstaller

echo.
echo 🔨 Building Windows executable...
pyinstaller --onefile ^
    --windowed ^
    --name "YouTube Downloader" ^
    --icon=app.ico ^
    --add-data "src:src" ^
    --hidden-import=tkinter ^
    src/main.py

if errorlevel 1 (
    echo ❌ Build failed
    pause
    exit /b 1
)

echo.
echo ✅ Executable created!
echo.
echo 📍 Location: dist\YouTube Downloader.exe
echo.
echo 🚀 To run the application:
echo    dist\YouTube Downloader.exe
echo.
echo 📦 To create a distributable package:
echo    - Copy the dist folder
echo    - Users can run "YouTube Downloader.exe"
echo.

pause
