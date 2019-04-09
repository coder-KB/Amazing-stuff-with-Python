"""
    To delete all the files with any specific extenstion
"""
# this code is to remove subtitle files

import os

path = "Path of the folder in which files are there to delete"

files = os.listdir(path)  # to list all files

for file in files:
    full_path = os.path.join(path, file)  # folders inside the main file
    for file1 in os.listdir(full_path):
        if file1.endswith(".srt"):                   # if the file ends with .srt then
            os.remove(os.path.join(full_path, file1)) # remove it
