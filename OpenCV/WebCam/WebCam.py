import numpy as np
import cv2
import requests
import time

url = "http://{}/shot.jpg".format(str(input("input IP address: ")))
print(url)

while True: 
    img_req = requests.get(url) 
    WebCam = np.array(bytearray(img_req.content), dtype=np.uint8)
    img = cv2.imdecode(WebCam, cv2.IMREAD_COLOR) 
    cv2.imshow("WebCam", img) 
    key = cv2.waitKey(1)

    if key == 27:    #ESC
        break

    elif key == 13:    #Enter
        file_name = ("ScreenShot "+time.ctime(time.time())+ ".jpeg")
        image = cv2.imwrite(file_name, img)
        
cv2.destroyAllWindows()