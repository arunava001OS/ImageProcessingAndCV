
import numpy as np
import cv2

# ## Canny Edge Detector

cap = cv2.VideoCapture(0)

if cap.isOpened():
    ret,frame = cap.read()
else:
    ret = False

while ret:
    ret,frame = cap.read()
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    output = cv2.Canny(rgb,100,200)  ##(img,minval,maxval) for hysteresis equalization
    cv2.imshow('Edge',output) ## here Edge is the window name
    cv2.imshow("Live Video Feed",frame)
    
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()



