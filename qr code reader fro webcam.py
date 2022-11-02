import cv2                          #These are the libraries being used and that need to added to the interpreter
import numpy as np                  #The needed libraries are opencv-python numpy and pyzbar
from pyzbar.pyzbar import decode    #notice that pyzbar is a more than just import this is what is reading the
                                    # qr and bar codes and decode is the important part of this

cap = cv2.VideoCapture(0)           #calling the camera, the zero might need to be changed depending on what camer is being used

def getQRdata(input):               #function for reading qr codes and bar code
    try:
        return decode(input)
    except:
        return[]

def drawpoly(framein,qrobj):        #function for intupretinf the qr code and bar codes
    if len(qrobj) == 0:             # list where the aqr and bar code data will be stored, could also be another storage method
        return framein              # once the data is colected it will
    else:
        for obj in qrobj:
            text = obj.data.decode('utf-8')     #this is what takes the data from the qr or bar code and turns it into a string
            pts = obj.polygon
            pts = np.array([pts],np.int64)
            print("Before reshaping", pts.shape)
            pts = pts.reshape((4,1,2))
            print("after reshaping", pts.reshape)
            cv2.polylines(framein [pts], True,(255,0,0),2)                              #makes outlines for witch qr is being read
            cv2.putText(framein, text,(50.50), cv2.FONT_HERSHEY_PLAIN,1.0,(200,255,5),2)    #displays text on camera with the outline
            return framein


while True:                                     #while loopp that displays the qr code and outline
    _, frame = cap.read()

    qr_obj = getQRdata(frame)
    frame = drawpoly(frame,qr_obj)

    cv2.imshow("Camera",frame)
    cv2.waitKey(1)

########## note ##########

# currently it will only have the camera pop up if there is a qr code to read

########## challenge ##########

# try to make the program always display the camra even if ther is no qr or bar code being ditected