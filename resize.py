#!/usr/bin/python3

from PIL import Image
import os
from resizeimage import resizeimage

FOLDER_RESIZED = './testA/'
FOLDER = './testfull/'

try:
    # creating a folder named data
    if not os.path.exists(FOLDER_RESIZED):
        os.makedirs(FOLDER_RESIZED)

except OSError:
    print ('Error: Creating directory of data')


for filename in os.listdir(FOLDER):
    with open(FOLDER + filename, 'r+b') as f:
        #check if f is an image
        if filename.endswith('.jpg'):
            try:
                image= Image.open(f) # open the image file
                print("processing image...", filename)
            except (IOError, SyntaxError) as e:
                print('Bad file:', filename) # print out the names of corrupt files

            try:
                cover = resizeimage.resize_cover(image, [256, 256])
                cover.save(os.path.join(FOLDER_RESIZED,"256_"+filename), image.format)
            except OSError:
                pass # You can always log it to logger
