import cv2

vid = cv2.VideoCapture(0)
body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')
cap = cv2.VideoCapture('walking.avi')
while True: 
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bodies = body_classifier.detectMultiScale(gray,1.2,3)
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Walking", frame)
    if cv2.waitKey(1) == 32: 
        break

cap.release()
cv2.destroyAllWindows()
