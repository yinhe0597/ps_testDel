# Image Metadata Cleaner

A simple tool to remove Adobe metadata from image files.

## Features
- Removes all metadata including Adobe-specific information
- Preserves original image quality
- Batch processing support
- Automatic output folder creation

## Supported Formats
- JPG/JPEG
- PNG
- TIFF

## Usage

1. Place your images in the `images` folder
2. Run the script:
```bash
python remove_adobe_info.py
```
3. Cleaned images will be saved in `images/ycl` folder

## Requirements
- Python 3.x
- Pillow library (`pip install pillow`)

## Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create a new branch for your feature/bugfix
3. Make your changes
4. Submit a pull request

Please follow these guidelines:
- Write clear commit messages
- Include tests for new features
- Update documentation when needed

## License
MIT License - Feel free to use and modify this tool
