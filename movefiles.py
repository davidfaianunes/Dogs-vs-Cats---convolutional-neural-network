# script to separate training data into two folders
# accordingly to its category
# just for organization purposes

import os
import shutil

# Define the source and destination directories
dir_A = r'/home/davidfaianunes/compsci/datasci/dogsvscats/train'
dir_B = r'/home/davidfaianunes/compsci/datasci/dogsvscats/train/caes'
dir_C = r'/home/davidfaianunes/compsci/datasci/dogsvscats/train/gatos'

# Loop through each file in the source directory
for filename in os.listdir(dir_A):
    # Check if the filename starts with 'dog'
    if filename.startswith('dog'):
        # Move the file to dog directory
        shutil.move(os.path.join(dir_A, filename), os.path.join(dir_B, filename))
    # Check if the filename starts with 'cat'
    elif filename.startswith('cat'):
        # Move the file to cat directory
        shutil.move(os.path.join(dir_A, filename), os.path.join(dir_C, filename))