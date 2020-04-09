
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

kernel = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

if cap.isOpened():
    ret,frame = cap.read()
else:
    ret = False

while ret:
    ret,frame = cap.read()
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    output = cv2.filter2D(rgb,-1,kernel)
    cv2.imshow('Edge',output) ## here GRAY is the window name
    cv2.imshow("Live Video Feed",frame)
    
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()


