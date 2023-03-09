import requests 
import cv2 
import numpy as np 

url = "http://192.168.169.250:8080/shot.jpg"
i = 1

while True: 
    img_req = requests.get(url) 
    img_arr = np.array(bytearray(img_req.content), dtype=np.uint8)
    cv2.namedWindow("img_arr", cv2.WINDOW_NORMAL) 
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR) 
    cv2.imshow("img_arr", img) 
    key = cv2.waitKey(10)
    if key == 27:    #ESC
        break

    elif key == 13:    #Enter
        file_name = ("ScreenShot "+ str(i)+ ".jpeg")
        image = cv2.imwrite(file_name, img)
        print(file_name)
        i += 1

cv2.destroyAllWindows()