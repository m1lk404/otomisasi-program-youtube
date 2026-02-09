# Makefile for YouTube Downloader
# Convenience commands for development and deployment

.PHONY: help install install-dev install-arch build-windows clean test run

help:
	@echo "YouTube Video Downloader - Available Commands"
	@echo ""
	@echo "Development:"
	@echo "  make install          Install for development"
	@echo "  make install-dev      Install with dev dependencies"
	@echo "  make test             Run tests"
	@echo "  make clean            Remove build artifacts"
	@echo ""
	@echo "Running:"
	@echo "  make run              Run the GUI application"
	@echo ""
	@echo "Building:"
	@echo "  make build-windows    Build Windows executable"
	@echo "  make build-linux      Build Linux executable"
	@echo "  make build-arch       Install on Arch Linux"
	@echo ""
	@echo "Deployment:"
	@echo "  make dist             Create distributions"
	@echo ""

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:
	python3 -m pytest tests/ -v

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf __pycache__/
	rm -rf src/__pycache__/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

run:
	python3 run.py

build-windows:
	@echo "Building Windows executable..."
	chmod +x build-windows.sh
	./build-windows.sh

build-linux:
	@echo "Building Linux executable..."
	chmod +x build-linux.sh
	./build-linux.sh 2>/dev/null || echo "build-linux.sh not found"

build-arch:
	@echo "Installing on Arch Linux..."
	chmod +x install-arch.sh
	./install-arch.sh

check-syntax:
	python3 -m py_compile src/*.py *.py
	@echo "✅ All Python files have valid syntax"

check-imports:
	python3 -c "from src.downloader import YouTubeDownloader; print('✅ Imports OK')"

install-deps:
	sudo pacman -S python python-pip ffmpeg tk 2>/dev/null || \
	pip install -r requirements.txt

dist: clean
	mkdir -p dist
	cp -r src dist/
	cp requirements.txt dist/
	cp README.md dist/
	cp QUICKSTART.md dist/
	@echo "Distribution ready in dist/"

all: clean install test
	@echo "✅ Build complete"

.DEFAULT_GOAL := help
