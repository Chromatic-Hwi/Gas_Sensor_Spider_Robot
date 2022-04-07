import cv2
import numpy as np

def tracking():
    cap=cv2.VideoCapture(0)
    cap.set(3,320)
    cap.set(4.240)
    
    while true:
        ret, frame = cap.read()
        cv2.imshow('video', frame)
        
        if cv2.waitkey(1) & 0xff == ord('q'):
            break
        
    cv2.destroyAllwindows()
    
tracking()