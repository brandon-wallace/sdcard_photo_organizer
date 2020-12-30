#!/usr/bin/env python3
"""
Move photos and videos from the SD card into
folders organized by date on a Linux OS.

Requirements:
    Python3.6+
"""


import sys
import datetime
from pathlib import Path
# import shutil
import os
from PIL import Image
from PIL.ExifTags import TAGS


# Create the directory according to the date formatted YYYY-MM-DD.
main_directory = datetime.datetime.today().strftime("%Y-%m-%d")
# Get the name of the user logged in.
current_user = os.getlogin()
count = 0
menu = []

# Scan for media mounted on the computer. Display a menu of storage devices.
storage = Path(f'/media/{current_user}').iterdir()
if not storage:
    print('No storage media mounted.')
    sys.exit(1)
else:
    for item, path in enumerate(storage, start=1):
        menu.append(path)
        print(f'{item}. {str(path)}')

# Select the device containing the media.
try:
    selection = int(input("Select a number of the SD card: "))
    sdcard = str(menu[selection-1])
except (ValueError, IndexError) as e:
    print(e)
    sys.exit(1)

source = sdcard
destination = Path(f'/home/{current_user}/Pictures/photos_{main_directory}')


def create_directory(directory):
    '''Make directory to store picture files'''

    # target_dir = Path(directory)
    if not directory.is_dir():
        print(f'Creating {directory}!')
        directory.mkdir(mode=0o777, parents=False, exist_ok=False)
    else:
        print(f'Directory {directory} exists.')
        return


create_directory(destination)


def get_img_date(path_to_image):
    '''Retrieve the date of the photo from the metadata.'''

    exif = {}
    image_file = Image.open(path_to_image)
    for tag, value in image_file.getexif().items():
        if tag in TAGS:
            exif[TAGS[tag]] = value
    return exif
    # exifdata = image_file.getexif()
    # for tag_id in exifdata:
    #     tag = TAGS.get(tag_id, tag_id)
    #     data = exifdata.get(tag_id)
    #     if isinstance(data, bytes):
    #         data = data.decode()
    #     print(f'{tag:25} => {data}')
    # img_date = Image.open(path)._getexif()[36867].split()[0]
    # img_date = img_date.replace(':', '-')
    # return img_date


def file_search(path):

    print('SEARCHING...')
    source_dir = Path(path)
    for ele in source_dir.rglob('*.JPG'):
        print(ele)
        img = get_img_date(ele)
        print(img['DateTime'])


file_search(source)
