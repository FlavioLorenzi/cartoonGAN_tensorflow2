#!/usr/bin/python

# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
cam = cv2.VideoCapture("./Samsara.2011.1080p.BRRip.x264.AAC-Ozlem.mp4")
framerate=(int)(cam.get(5))
print(framerate)

try:
    # creating a folder named data
    if not os.path.exists('imgs_ambient_full'):
        os.makedirs('imgs_ambient_full')

# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')

# frame
currentframe = 0
i=0

while(True):
    ret,frame = cam.read()
    if ret:
        if (currentframe % framerate == 0):
            name = 'frame_' + str(i) + '.jpg'
            i += 1
            writeStatus = cv2.imwrite(os.path.join('imgs_ambient_full', name), frame)
            if writeStatus is True:
                print ('Creating...', name)
            else:
                print("problem with image", name) # or raise exception, handle problem, etc.
                pass
        currentframe += 1
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
