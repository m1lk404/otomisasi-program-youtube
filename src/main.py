#!/usr/bin/env python3
"""
YouTube Video Downloader with Clip Cutting Feature
Supports best quality video+audio and automatic cookie handling
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
import sys
from pathlib import Path
import json
from datetime import datetime

from downloader import YouTubeDownloader


class YouTubeDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("900x700")
        self.root.resizable(True, True)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.downloader = YouTubeDownloader()
        self.is_downloading = False
        self.download_thread = None
        
        self.setup_ui()
        self.load_config()
        
    def setup_ui(self):
        """Setup the user interface"""
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights for responsiveness
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="YouTube Video Downloader", 
                                font=("Helvetica", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # YouTube Link
        ttk.Label(main_frame, text="YouTube Link:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.link_entry = ttk.Entry(main_frame, width=80)
        self.link_entry.grid(row=1, column=1, columnspan=2, sticky=(tk.W, tk.E), padx=5)
        
        # Download Folder
        ttk.Label(main_frame, text="Download Folder:").grid(row=2, column=0, sticky=tk.W, pady=5)
        folder_frame = ttk.Frame(main_frame)
        folder_frame.grid(row=2, column=1, columnspan=2, sticky=(tk.W, tk.E), padx=5)
        folder_frame.columnconfigure(0, weight=1)
        
        self.folder_entry = ttk.Entry(folder_frame)
        self.folder_entry.grid(row=0, column=0, sticky=(tk.W, tk.E))
        self.folder_entry.insert(0, str(Path.home() / "Downloads" / "YouTube"))
        
        folder_btn = ttk.Button(folder_frame, text="Browse", command=self.browse_folder)
        folder_btn.grid(row=0, column=1, padx=5)
        
        # Enable Clip Cutting Checkbox
        self.clip_var = tk.BooleanVar(value=False)
        clip_check = ttk.Checkbutton(main_frame, text="Enable Clip Cutting (Cut video from minute to minute)", 
                                     variable=self.clip_var, command=self.toggle_clip_options)
        clip_check.grid(row=3, column=0, columnspan=3, sticky=tk.W, pady=10)
        
        # Clip Cutting Options (initially disabled)
        self.clip_frame = ttk.LabelFrame(main_frame, text="Clip Cutting Options", padding="10")
        self.clip_frame.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5, padx=5)
        self.clip_frame.columnconfigure(1, weight=1)
        
        ttk.Label(self.clip_frame, text="Start Time (minutes):").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.start_time_entry = ttk.Entry(self.clip_frame, width=20)
        self.start_time_entry.grid(row=0, column=1, sticky=tk.W, padx=5)
        self.start_time_entry.insert(0, "0")
        
        ttk.Label(self.clip_frame, text="End Time (minutes):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.end_time_entry = ttk.Entry(self.clip_frame, width=20)
        self.end_time_entry.grid(row=1, column=1, sticky=tk.W, padx=5)
        
        # Browser Cookie Automation
        ttk.Label(main_frame, text="Browser Cookie Handling:").grid(row=5, column=0, sticky=tk.W, pady=5)
        
        self.cookie_var = tk.StringVar(value="none")
        cookie_frame = ttk.Frame(main_frame)
        cookie_frame.grid(row=5, column=1, columnspan=2, sticky=(tk.W, tk.E), padx=5)
        
        ttk.Radiobutton(cookie_frame, text="None", variable=self.cookie_var, 
                       value="none").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(cookie_frame, text="Chrome", variable=self.cookie_var, 
                       value="chrome").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(cookie_frame, text="Firefox", variable=self.cookie_var, 
                       value="firefox").pack(side=tk.LEFT, padx=5)
        
        # Download Quality Options
        ttk.Label(main_frame, text="Quality:").grid(row=6, column=0, sticky=tk.W, pady=5)
        self.quality_var = tk.StringVar(value="best")
        quality_frame = ttk.Frame(main_frame)
        quality_frame.grid(row=6, column=1, columnspan=2, sticky=(tk.W, tk.E), padx=5)
        
        ttk.Radiobutton(quality_frame, text="Best", variable=self.quality_var, 
                       value="best").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(quality_frame, text="1080p", variable=self.quality_var, 
                       value="1080").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(quality_frame, text="720p", variable=self.quality_var, 
                       value="720").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(quality_frame, text="Audio Only", variable=self.quality_var, 
                       value="audio").pack(side=tk.LEFT, padx=5)
        
        # Download Button
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=20)
        button_frame.columnconfigure(0, weight=1)
        
        self.download_btn = ttk.Button(button_frame, text="Start Download", command=self.start_download)
        self.download_btn.pack(side=tk.LEFT, padx=5)
        
        self.cancel_btn = ttk.Button(button_frame, text="Cancel", command=self.cancel_download, state=tk.DISABLED)
        self.cancel_btn.pack(side=tk.LEFT, padx=5)
        
        # Progress Bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=8, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        # Status Label
        self.status_label = ttk.Label(main_frame, text="Ready", relief=tk.SUNKEN)
        self.status_label.grid(row=9, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        # Log Output
        ttk.Label(main_frame, text="Download Log:").grid(row=10, column=0, sticky=tk.W, pady=(10, 5))
        self.log_text = scrolledtext.ScrolledText(main_frame, height=12, width=100)
        self.log_text.grid(row=11, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        main_frame.rowconfigure(11, weight=1)
        
        # Disable clip options initially
        self.toggle_clip_options()
        
    def toggle_clip_options(self):
        """Toggle clip cutting options visibility"""
        if self.clip_var.get():
            self.clip_frame.grid()
        else:
            self.clip_frame.grid_remove()
            
    def browse_folder(self):
        """Open folder browser dialog"""
        folder = filedialog.askdirectory(title="Select Download Folder")
        if folder:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder)
            
    def log_message(self, message):
        """Add message to log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        self.root.update()
        
    def start_download(self):
        """Start download in a separate thread"""
        url = self.link_entry.get().strip()
        
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube link")
            return
            
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
            
        download_path = self.folder_entry.get().strip()
        if not download_path:
            messagebox.showerror("Error", "Please select a download folder")
            return
            
        # Validate clip times if enabled
        start_time = None
        end_time = None
        if self.clip_var.get():
            try:
                start_time = float(self.start_time_entry.get())
                end_time_str = self.end_time_entry.get().strip()
                end_time = float(end_time_str) if end_time_str else None
                
                if end_time and start_time >= end_time:
                    messagebox.showerror("Error", "Start time must be less than end time")
                    return
            except ValueError:
                messagebox.showerror("Error", "Invalid time values. Please enter numbers.")
                return
                
        # Disable UI during download
        self.is_downloading = True
        self.download_btn.config(state=tk.DISABLED)
        self.cancel_btn.config(state=tk.NORMAL)
        self.progress.start()
        self.log_text.delete(1.0, tk.END)
        
        # Start download in thread
        self.download_thread = threading.Thread(
            target=self._download_worker,
            args=(url, download_path, start_time, end_time),
            daemon=True
        )
        self.download_thread.start()
        
    def _download_worker(self, url, download_path, start_time, end_time):
        """Worker thread for downloading"""
        try:
            self.log_message(f"Starting download from: {url}")
            self.log_message(f"Download folder: {download_path}")
            
            # Create download folder if it doesn't exist
            os.makedirs(download_path, exist_ok=True)
            
            # Prepare options
            options = {
                'quality': self.quality_var.get(),
                'cookies_browser': self.cookie_var.get() if self.cookie_var.get() != "none" else None,
                'start_time': start_time,
                'end_time': end_time,
                'output_path': download_path,
                'log_callback': self.log_message
            }
            
            # Download
            result = self.downloader.download(url, options)
            
            if result['success']:
                self.log_message(f"✓ Download completed successfully!")
                self.log_message(f"File saved to: {result.get('filepath', download_path)}")
                self.status_label.config(text="Download completed successfully!")
                messagebox.showinfo("Success", f"Video downloaded successfully!\n\nSaved to: {download_path}")
            else:
                error_msg = result.get('error', 'Unknown error')
                self.log_message(f"✗ Download failed: {error_msg}")
                self.status_label.config(text="Download failed!")
                messagebox.showerror("Download Failed", error_msg)
                
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.log_message(error_msg)
            self.status_label.config(text="Download failed!")
            messagebox.showerror("Error", error_msg)
        finally:
            self.is_downloading = False
            self.download_btn.config(state=tk.NORMAL)
            self.cancel_btn.config(state=tk.DISABLED)
            self.progress.stop()
            
    def cancel_download(self):
        """Cancel current download"""
        self.downloader.cancel_download()
        self.log_message("Download cancelled by user")
        self.is_downloading = False
        
    def load_config(self):
        """Load saved configuration"""
        config_file = Path.home() / ".youtube_downloader_config.json"
        if config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    config = json.load(f)
                    if 'download_path' in config:
                        self.folder_entry.delete(0, tk.END)
                        self.folder_entry.insert(0, config['download_path'])
                    if 'quality' in config:
                        self.quality_var.set(config['quality'])
                    if 'cookies_browser' in config:
                        self.cookie_var.set(config['cookies_browser'])
            except Exception as e:
                print(f"Could not load config: {e}")
                
    def save_config(self):
        """Save current configuration"""
        config = {
            'download_path': self.folder_entry.get(),
            'quality': self.quality_var.get(),
            'cookies_browser': self.cookie_var.get()
        }
        config_file = Path.home() / ".youtube_downloader_config.json"
        try:
            with open(config_file, 'w') as f:
                json.dump(config, f)
        except Exception as e:
            print(f"Could not save config: {e}")
            
    def on_closing(self):
        """Handle window closing"""
        if self.is_downloading:
            if messagebox.askokcancel("Download in Progress", "A download is in progress. Do you want to cancel and exit?"):
                self.cancel_download()
                self.save_config()
                self.root.destroy()
        else:
            self.save_config()
            self.root.destroy()


def main():
    root = tk.Tk()
    app = YouTubeDownloaderGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()
