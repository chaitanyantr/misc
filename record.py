import numpy as np
import cv2

cap = cv2.VideoCapture(1)
#cap.set(cv2.CAP_PROP_AUTOFOCUS, 1) 

frame_w = 1280
frame_h = 720

cap.set(3,frame_w)
cap.set(4,frame_h)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
out = cv2.VideoWriter('output.avi',fourcc, 30.0, (1280,720))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        #frame = cv2.flip(frame,0)

        # write the flipped frame
        #cv2.putText(frame, "Hello World!!!", (50, 15), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.putText(frame, "Hello World!!!", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.putText(frame, "Hello World!!!", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.putText(frame, "Hello World!!!", (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.putText(frame, "Hello World!!!", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.putText(frame, "Hello World!!!", (50, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        cv2.putText(frame, "Hello World!!!", (50, 600), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        
        cv2.line(frame,(frame_w/2,0),(frame_w/2,frame_h),(255,0,0),1)
        cv2.line(frame,(0,frame_h/2),(frame_w,frame_h/2),(255,0,0),1)


        cv2.circle(frame, (frame_w/2,frame_h/2),5, (0,255,0), 4)
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
