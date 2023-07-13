import cv2
import numpy as np
# import cupy as cp
import time
import os
import glob

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))  
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cam.get(cv2.CAP_PROP_FPS))
print("{}x{} {}fps".format(width, height, fps))

if not cam.isOpened():
    print("Cannot open camera")
    exit()

# while True:
#     ret, img = cam.read()
#     if not ret:
#         print("Camera not available")
#         break
# 
#     cv2.imshow('FRS', img)   
#     if cv2.waitKey(1) == 27:    #ESC
#         break             