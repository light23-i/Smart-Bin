import torch
import cv2 
import os 

#img = cv2.imread('pp4.jpeg')

cap = cv2.VideoCapture('x.mp4')
model = torch.load('f.pt')
model.predict('images/M.jpeg',confidence=70).save('x.jpeg')
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
       print(model.predict(frame,confidence=70).json())
       cv2.imshow('Frame',frame) 
    else:
   	    break
 
# # When everything done, release the video capture object
cap.release()
 
# # Closes all the frames
cv2.destroyAllWindows()
