from PIL import Image
from os import listdir,path,remove
import argparse

# Change according to what you want the new filetype to be
newFileType = ".png"

def getTerminalArgs() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument(help='The directory to search for files to convert' , dest='dir' , type=str)
    args = parser.parse_args()
    return args.dir

# Go through the files
#   If .bmp -> convert to .jpeg
#   If file -> Loop to iterate through the file to check for .bmp files

def convert_file(full_path, new_file_path):
    try:
        with Image.open(full_path) as im:
            new_file_with_ext = new_file_path + newFileType
            im.save(new_file_with_ext)
            print(f'Converted {full_path} to {new_file_with_ext}')
            # After conversion, delete the original .bmp file
            remove(full_path)
            print(f'Deleted original file: {full_path}')
    except (IOError, OSError) as e:
        print(f'Error converting {full_path}: {e}')

def get_files_to_convert(dir_path, old_file_types):
    print(f'Checking directory: {dir_path}')
    for file in listdir(dir_path):
        full_path = path.join(dir_path, file)
        if path.isdir(full_path):
            get_files_to_convert(full_path, old_file_types)
        else:
            print(f'Found file: {file}')
            file_name, file_extension = path.splitext(file)
            if file_extension.lower() in old_file_types:
                new_file_path = path.join(dir_path, file_name)
                convert_file(full_path, new_file_path)
            else:
                print(f'Skipped file (not in {old_file_types}): {file}')


if __name__ == '__main__':
    directory = getTerminalArgs()
    get_files_to_convert(directory, ('.jpg',))
