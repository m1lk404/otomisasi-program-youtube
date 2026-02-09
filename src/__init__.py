"""
YouTube Video Downloader Package
"""

__version__ = "1.0.0"
__author__ = "YouTube Downloader Team"

from .downloader import YouTubeDownloader

# GUI import is optional (requires tkinter)
try:
    from .main import YouTubeDownloaderGUI
    __all__ = ['YouTubeDownloader', 'YouTubeDownloaderGUI']
except ImportError:
    # If tkinter is not available, still allow downloader to be imported
    __all__ = ['YouTubeDownloader']
