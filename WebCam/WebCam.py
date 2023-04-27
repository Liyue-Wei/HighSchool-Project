import numpy as np
import cv2
import requests
import time

# url = "http://"+str(input("input url: ")+"/shot.jpg")
url = "http://{}/shot.jpg".format(str(input("input url: ")))
time_output = time.ctime(time.time())
print(url)
print(time_output)

while True: 
    img_req = requests.get(url) 
    WebCam = np.array(bytearray(img_req.content), dtype=np.uint8)
    cv2.namedWindow("WebCam", cv2.WINDOW_NORMAL) 
    img = cv2.imdecode(WebCam, cv2.IMREAD_COLOR) 
    cv2.imshow("WebCam", img) 
    key = cv2.waitKey(10)

    if key == 27:    #ESC
        break

    elif key == 13:    #Enter
        file_name = ("ScreenShot "+time_output+ ".jpeg")
        image = cv2.imwrite(file_name, img)
        
cv2.destroyAllWindows()