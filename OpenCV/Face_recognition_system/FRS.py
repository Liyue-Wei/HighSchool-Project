import numpy as np
import cv2
import time

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Camera is not available")
    exit()

try:
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

except:
    print("Camera does not support 720p")

width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))  
height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cam.get(cv2.CAP_PROP_FPS))
print("{}x{} {}fps".format(width, height, fps))

upscale = 4.0
downscale = 1/4

while True:
    ret, img = cam.read()
    if not ret:
        print("Camera is not available")
        break

    cv2.imshow('FRS', img)
    
    img = cv2.resize(img, (0, 0), fx=upscale, fy=upscale)
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])  
    img = cv2.filter2D(img, -1, kernel)
    img = cv2.resize(img, (0, 0), fx=downscale, fy=downscale)
    cv2.imshow('FRS enhanced', img) 

    key = cv2.waitKey(1)    
    if key == 27:    #ESC
        break   

    # elif key == 13:    #Enter
    #     file_name = ("ScreenShot "+time.ctime(time.time())+ ".jpeg")
    #     image = cv2.imwrite(file_name, img)  

cv2.destroyAllWindows()