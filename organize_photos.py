#!/usr/bin/env python3
"""
Move photos and videos from the SD card into
folders organized by date on a Linux OS.

Requirements:
    Python3.6+
"""


import datetime
from PIL import Image
from pathlib import Path
import shutil
import os


# Create the directory according to the date formatted YYYY-MM-DD.
main_directory = datetime.datetime.today().strftime("%Y-%m-%d")
# Get the name of the user logged in.
current_user = os.getlogin()
count = 0
menu = []

# Scan for media mounted on the computer. Display a menu of storage devices.
for item, path in enumerate(Path(f'/media/{current_user}').iterdir(), start=1):
    menu.append(path)
    print(f'{item}. {str(path)}')
# for card in os.listdir('/media/' + current_user):
#     menu.append(card)
#     count += 1
#     print("{}. {}".format(count, card))

# Select the device containing the media.
selection = int(input("Select a number of the SD card: "))
sdcard = str(menu[selection-1])
print(sdcard)
print(type(sdcard))
print(f'SOURCE: {sdcard}')
destination = Path(f'/media/{current_user}/Pictures/photos_{main_directory}')
print(f'DESTINATION: {destination}')


def create_directory(directory):
    '''Make directory to store picture files'''

    target_dir = Path(directory)
    if not target_dir.is_dir():
        print(f'Creating {target_dir}!')
        target_dir.mkdir(mode=0o777, parents=False, exist_ok=False)
    else:
        print(f'Directory {target_dir} exists.')
        return


create_directory('test_directory')
# def make_directory(directory):
#     '''Create the directory if not in existance.'''
#     if not os.path.exists(directory):
#         os.mkdir(directory)
# 
# 
# source = '/media/' + current_user + '/' + sdcard
# destination = '/home/' + current_user + '/Pictures/' + 'photos_' + main_directory
# 
# make_directory(destination)
# 
# 
# def get_img_date(path):
#     '''Retrieve the date of the photo from the metadata.'''
#     # Date format YYYY-MM-DD. 
#     img_date = Image.open(path)._getexif()[36867].split()[0]
#     img_date = img_date.replace(':', '-')
#     return img_date
# 
# 
# def get_video_date(path):
#     '''Retrieve the date of the video from the metadata.'''
#     video_date = os.system("ls -l --time-style='+%Y-%m-%d' *.MOV")
#     
# 
# # Recursively scan for the photos and videos contained on the storage media.
# for root, directories, photos in os.walk(source):
#     for p in photos:
#         # Copy photos to destination directory.
#         if p.endswith(".JPG") or p.endswith(".jpg"):
#             files = os.path.join(root, p)
#             make_directory(destination + '/' + get_img_date(files))
#             shutil.move(files, destination + '/' + get_img_date(files))
# 
