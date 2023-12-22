import serial
import cv2
import torch
usbport = '/dev/tty.usbmodem1411' #usb from arduino


arduino = serial.Serial(usbport, 9600, timeout=0)

vid = cv2.VideoCapture(0)
distances = []
def imgans():
    ret,img = vid.read()
    if ret:
        cv2.imwrite('x1.png',img)
        model = torch.load('f.pt')
        return len(model.predict('x1.png',confidence=70).predictions)
    else:
        return 0
while (True):
    if (arduino.inWaiting()>0):
        myData = arduino.readline().decode('ascii')
        if myData<10:
            command = imgans()
            if command==0:
                arduino.write(180)
            else:
                arduino.write(-1)
            #arduino.write(command)                          # write position to serial port
            #reachedPos = str(arduino.readline())            # read serial port for arduino echo
            #distances.append(myData)
            print(myData)
        #print(distances)
