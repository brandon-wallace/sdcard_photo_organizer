#!/usr/bin/env python3
"""
Move photos and videos from the SD card into
folders organized by date on a Linux OS.
Requirements:
    Python3.6+
"""

import os
import sys
import shutil
import datetime
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS


# Create the directory according to the date formatted YYYY-MM-DD.
main_directory = datetime.datetime.today().strftime("%Y-%m-%d")
# Get the name of the user logged in.
current_user = os.getlogin()
menu = []

# Scan for media mounted on the computer. Display a menu of storage devices.
storage = Path(f'/media/{current_user}').iterdir()
if not storage:
    print('No storage media mounted.')
    sys.exit(1)
else:
    for item, path in enumerate(storage, start=1):
        menu.append(path)
        print(f'{item}. {path}')

# Select the device containing the media.
try:
    selection = int(input("Select a number of the SD card: "))
    sdcard = str(menu[selection-1])
except (ValueError, IndexError):
    sys.exit(1)

source = sdcard
destination = Path(f'/home/{current_user}/Pictures/photos_{main_directory}')


def create_directory(directory):
    '''Make directory to store picture files'''

    if not directory.is_dir():
        print(f'Creating directory: {directory}!')
        directory.mkdir(mode=0o777, parents=False, exist_ok=False)
    else:
        return


def get_img_date(path_to_image):
    '''Retrieve the date of the photo from the metadata'''

    exif = {}
    image_file = Image.open(path_to_image)
    for tag, value in image_file.getexif().items():
        if tag in TAGS:
            exif[TAGS[tag]] = value
    return exif


def file_search(path):
    '''Recursively search for image files'''

    count = 0
    print('Searching for images. Please wait...')
    source_dir = Path(path)
    for ele in source_dir.rglob('*.JPG'):
        count += 1
        img = get_img_date(ele)
        creation_date = str(img['DateTime']).replace(':', '-').split(' ')[0]
        new_directory = destination / creation_date
        if not new_directory.exists():
            new_directory.mkdir()
        shutil.move(str(ele), new_directory)
    print('Done.')
    print(f'{count} number of pictures moved off SD card.')


def main():
    '''Main function to run program'''

    create_directory(destination)
    file_search(source)


if __name__ == '__main__':
    main()
