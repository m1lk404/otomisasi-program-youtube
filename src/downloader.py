#!/usr/bin/env python3
"""
YouTube Downloader using yt-dlp
Handles video download, clip cutting, and cookie management
"""

import os
import subprocess
import json
from pathlib import Path
import re
from typing import Optional, Dict, Any, Callable


class YouTubeDownloader:
    def __init__(self):
        self.is_cancelled = False
        self.ytdlp_path = self._find_ytdlp()
        
    def _find_ytdlp(self) -> str:
        """Find yt-dlp executable in system"""
        # Try to find yt-dlp in common locations or PATH
        possible_paths = [
            'yt-dlp',
            'yt-dlp.exe',
            os.path.expanduser('~/.local/bin/yt-dlp'),
            'C:\\Program Files\\yt-dlp\\yt-dlp.exe',
        ]
        
        for path in possible_paths:
            if self._command_exists(path):
                return path
                
        return 'yt-dlp'  # Default, will rely on PATH
        
    @staticmethod
    def _command_exists(command: str) -> bool:
        """Check if command exists in system"""
        try:
            if command.endswith('.exe'):
                return os.path.exists(command)
            result = subprocess.run(['which', command], capture_output=True, timeout=2)
            return result.returncode == 0
        except:
            return False
            
    def cancel_download(self):
        """Cancel current download"""
        self.is_cancelled = True
        
    def download(self, url: str, options: Dict[str, Any]) -> Dict[str, Any]:
        """
        Download video from YouTube
        
        Args:
            url: YouTube URL
            options: Download options including:
                - quality: 'best', '1080', '720', 'audio'
                - cookies_browser: 'chrome', 'firefox', or None
                - start_time: Start time in minutes (for clipping)
                - end_time: End time in minutes (for clipping)
                - output_path: Where to save the video
                - log_callback: Function to call for logging
                
        Returns:
            Dict with 'success', 'filepath', and optional 'error'
        """
        self.is_cancelled = False
        
        try:
            quality = options.get('quality', 'best')
            cookies_browser = options.get('cookies_browser')
            start_time = options.get('start_time')
            end_time = options.get('end_time')
            output_path = options.get('output_path', str(Path.home() / 'Downloads'))
            log_callback = options.get('log_callback', lambda x: None)
            
            # Build yt-dlp command
            cmd = [self.ytdlp_path]
            
            # Add bot protection and cookie handling
            log_callback("Configuring yt-dlp options...")
            cmd.extend([
                '--no-warnings',
                '--progress',
                '--socket-timeout', '30',
                '--retries', '3',
                '--http-chunks', '10',
                '-R', 'exponential:10',
                '--quiet',
            ])
            
            # Add browser cookie extraction
            if cookies_browser:
                log_callback(f"Extracting cookies from {cookies_browser.capitalize()}...")
                cmd.extend(['--cookies-from-browser', cookies_browser])
                
            # Add User-Agent to avoid simple blocks
            cmd.extend([
                '-U', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            ])
            
            # Configure quality format
            format_string = self._get_format_string(quality)
            log_callback(f"Using quality: {quality}")
            cmd.extend(['-f', format_string])
            
            # Output template
            output_template = os.path.join(output_path, '%(title)s.%(ext)s')
            cmd.extend(['-o', output_template])
            
            # Add clip cutting if enabled
            clip_info = ""
            if start_time is not None:
                log_callback(f"Clip cutting enabled: {start_time}m to {end_time if end_time else 'end'}m")
                start_seconds = int(start_time * 60)
                cmd.extend(['--postprocessor-args', f'--cut_start {start_seconds}'])
                if end_time:
                    end_seconds = int(end_time * 60)
                    duration = end_seconds - start_seconds
                    cmd.extend(['--postprocessor-args', f'--cut_duration {duration}'])
                clip_info = f" (cut from {start_time}m to {end_time if end_time else 'end'}m)"
                
            # Add FFmpeg post-processor for merging audio/video
            cmd.extend(['--merge-output-format', 'mp4'])
            
            # Add URL
            cmd.append(url)
            
            log_callback(f"Starting download...{clip_info}")
            log_callback(f"Command: {' '.join([cmd[0]] + cmd[1:5])}... (additional options)")
            
            # Execute download
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=3600  # 1 hour timeout
            )
            
            if self.is_cancelled:
                return {
                    'success': False,
                    'error': 'Download cancelled by user'
                }
            
            if result.returncode == 0:
                log_callback("Video download and processing completed!")
                
                # Try to find the output file
                output_file = self._find_downloaded_file(output_path)
                
                return {
                    'success': True,
                    'filepath': output_file if output_file else output_path
                }
            else:
                error_msg = result.stderr if result.stderr else result.stdout
                
                # Check for specific errors
                if 'bot' in error_msg.lower() or '403' in error_msg:
                    log_callback("Bot blocking detected. Trying alternative approach...")
                    return self._download_with_fallback(url, options)
                    
                log_callback(f"Error output: {error_msg[:500]}")
                return {
                    'success': False,
                    'error': f'Download failed: {error_msg[:200]}'
                }
                
        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'error': 'Download timeout (exceeded 1 hour)'
            }
        except FileNotFoundError:
            return {
                'success': False,
                'error': 'yt-dlp not found. Please install it:\npip install yt-dlp'
            }
        except Exception as e:
            return {
                'success': False,
                'error': f'Unexpected error: {str(e)}'
            }
                
    def _download_with_fallback(self, url: str, options: Dict[str, Any]) -> Dict[str, Any]:
        """Fallback download method with additional anti-bot measures"""
        try:
            output_path = options.get('output_path', str(Path.home() / 'Downloads'))
            log_callback = options.get('log_callback', lambda x: None)
            
            log_callback("Using fallback with additional anti-bot measures...")
            
            cmd = [
                self.ytdlp_path,
                '--no-warnings',
                '-f', 'best',
                '--extractor-args', 'youtube:lang=en',
                '--socket-timeout', '60',
                '-U', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
                '--http-chunks', '10',
                '--fragment-retries', '5',
                '--skip-unavailable-fragments',
                '-o', os.path.join(output_path, '%(title)s.%(ext)s'),
                '--merge-output-format', 'mp4',
                url
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)
            
            if result.returncode == 0:
                log_callback("Fallback download successful!")
                output_file = self._find_downloaded_file(output_path)
                return {
                    'success': True,
                    'filepath': output_file if output_file else output_path
                }
            else:
                return {
                    'success': False,
                    'error': 'Download failed even with fallback method'
                }
                
        except Exception as e:
            return {
                'success': False,
                'error': f'Fallback failed: {str(e)}'
            }
            
    @staticmethod
    def _get_format_string(quality: str) -> str:
        """Generate yt-dlp format string based on quality preference"""
        quality_formats = {
            'best': 'bv*+ba/b',  # Best video + best audio or best overall
            '1080': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            '720': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
            'audio': 'bestaudio[ext=m4a]/bestaudio',
        }
        return quality_formats.get(quality, 'bv*+ba/b')
        
    @staticmethod
    def _find_downloaded_file(output_path: str) -> Optional[str]:
        """Find the most recently downloaded file"""
        try:
            files = []
            for ext in ['*.mp4', '*.mkv', '*.webm', '*.m4a', '*.mp3']:
                files.extend(Path(output_path).glob(ext))
                
            if files:
                # Return most recently modified file
                latest_file = max(files, key=lambda p: p.stat().st_mtime)
                return str(latest_file)
        except Exception:
            pass
            
        return None
