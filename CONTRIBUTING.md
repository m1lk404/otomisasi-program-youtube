# Contributing to YouTube Video Downloader

Thank you for your interest in contributing to this project!

## How to Contribute

### Reporting Issues

- Check if the issue already exists
- Provide a clear description
- Include your OS and Python version
- Describe the steps to reproduce

### Making Code Changes

1. **Setup Development Environment**

   ```bash
   pip install -r requirements-dev.txt
   ```

2. **Make Your Changes**
   - Follow PEP 8 style guidelines
   - Add comments for complex logic
   - Keep functions focused and small

3. **Test Your Changes**

   ```bash
   python3 -m pytest tests/ -v
   ```

4. **Submit a Pull Request**
   - Write a clear PR description
   - Reference any related issues
   - Include before/after screenshots if UI changes

## Code Style

- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use meaningful variable names
- Add docstrings to functions

## Feature Ideas

- [ ] Batch downloading multiple videos
- [ ] Downloading entire playlists
- [ ] Audio format selection (MP3, WAV, etc.)
- [ ] Custom metadata tagging
- [ ] Download scheduling
- [ ] Speed limit controls

## Testing

Run tests with:

```bash
pytest
```

Run specific test:

```bash
pytest tests/test_downloader.py -v
```

## Questions?

Open an issue on GitHub or check the README for FAQs.

Thank you for contributing! 🙌
