#!/usr/bin/env python3
"""
Setup script for YouTube Downloader
Allows package installation and distribution building
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="youtube-video-downloader",
    version="1.0.0",
    author="YouTube Downloader Project",
    description="YouTube video downloader with clip cutting and best quality selection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/youtube-video-downloader",
    project_urls={
        "Bug Tracker": "https://github.com/yourusername/youtube-video-downloader/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Topic :: Multimedia :: Video",
        "Topic :: System :: Archiving :: Downloading",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "yt-dlp>=2024.1.0",
    ],
    extras_require={
        "dev": [
            "pyinstaller>=5.13.2",
            "pytest>=7.4.0",
            "pillow>=10.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "youtube-downloader=src.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.py", "*.md"],
    },
)
