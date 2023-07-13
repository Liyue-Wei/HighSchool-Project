import cv2
import numpy as np
import cupy as cp
import time
import os
import glob

cam = cv2.VideoCapture(0)
# win = cv2.namedWindow("cam", cv2.WINDOW_AUTOSIZE)
# time.sleep(5)
cv2.imshow("cam", cam)
cv2.destroyAllWindows()

if not cam.isOpened():
    print("Cannot open camera")
    exit()