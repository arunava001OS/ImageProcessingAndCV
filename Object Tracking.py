import cv2

cam = cv2.VideoCapture(0)

available_trackers = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
tracker_type = available_trackers[1]

if tracker_type == 'BOOSTING':
    tracker= cv2.TrackerBoosting_create()
if tracker_type == 'MIL':
    tracker= cv2.TrackerMIL_create()
if tracker_type == 'KCF':
    #tracker= cv2.TrackerKCF_create()
    pass
if tracker_type == 'TLD':
    tracker= cv2.TrackerTLD_create()
if tracker_type == 'MEDIANFLOW':
    tracker= cv2.TrackerMedianFlow_create()
if tracker_type == 'GOTURN':
    tracker= cv2.TrackerGOTURN_create()
if tracker_type == 'MOSSE':
    tracker= cv2.TrackerMOSSE_create()
if tracker_type == 'CSRT':
    tracker= cv2.TrackerCSRT_create()

ret,frame = cam.read()
    
bbox = cv2.selectROI('Tracker',frame,False)

tracker.init(frame, bbox)

while True:
    ret,frame = cam.read()
    ret, bbox = tracker.update(frame)
    
    if ret:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    else:
        cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
    cv2.imshow('Tracker',frame)
    
    if cv2.waitKey(1) == 27:
        break
        
cam.release()
cv2.destroyAllWindows()
