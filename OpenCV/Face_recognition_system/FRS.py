import cv2
import numpy as np
import cupy as cp
import time
import os
import glob

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, img = cam.read()
    if not ret:
        print("Camera not available")
        break

    cv2.imshow('FRS', img)    
    if cv2.waitKey(1) == 27:    #ESC
        break             