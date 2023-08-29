import numpy as np
import cv2
# import requests
import time

cam = cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

if not cam.isOpened():
    print("Camera is not available")
    exit()

width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))  
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cam.get(cv2.CAP_PROP_FPS))
print("{}x{} {}fps".format(width, height, fps))

while True:
    ret, img = cam.read()
    if not ret:
        print("Camera is not available")
        break

    # img = cv2.resize(img, (0, 0), fx=2.0, fy=2.0)
    cv2.imshow('FRS', img)
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    img = cv2.filter2D(img, -1, kernel)
    cv2.imshow('FRS enhanced', img)   
    
    if cv2.waitKey(1) == 27:    #ESC
        break   

    elif cv2.waitKey(1) == 13:    #Enter
        file_name = ("ScreenShot "+time.ctime(time.time())+ ".jpeg")
        image = cv2.imwrite(file_name, img)  