# ImageFormatConverter.py

## Description
ImageFormatConverter.py is a Python script that automates the conversion of image files to `.png` format. It recursively searches through a specified directory and its subdirectories, converting all `.jpg` files to `.png`. This tool is ideal for standardizing image file formats in large directories.

## Features
- Recursively converts `.jpg` files to `.png` in a specified directory, or any other image extension format.
- Automatically deletes the original `.jpg` files post-conversion
- Easy to use with command line arguments

## Usage
1. Clone the repository.
2. Install dependencies: `pip install Pillow`
3. Navigate to the script directory.
4. Run the script with the target directory: `python ImageFormatConverter.py [target-directory]`

Example:
  `python ImageFormatConverter.py /path/to/directory`

## Requirements
- Python 3.x
- Pillow library

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests for enhancements or bug fixes.

## Contact
For any questions or feedback, please contact jhaenel@siue.edu.
