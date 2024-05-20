# importing the required  libraries
import cv2,imutils,time
from funcs import is_empty

# importing the haarcascade algorithm
alg="haarcascade_frontalface_default.xml"

# initializing an object for haar cascade algorithm using cascade classifier class
haar_cascade=cv2.CascadeClassifier(alg)

# initializing camera object
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

# using while loop reading the camera frame by frame
while True:
    # reading the  frame from camera
    _,img=cam.read()
    # changing the image obtained into a gray scale image
    grayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # feeding the above gray scale image to the haar cascade algorithm it returns the x,y,w,h to draw rectangle
    face_cordinates=haar_cascade.detectMultiScale(grayImage,1.3,4)
    if len(face_cordinates)==0:
        color = (255, 0, 0)
        text="No face detected"

    else:
        color = (0, 255, 0)

        text=" Face Detected !"
    # drawing the rectangle around the detected face using the tuple returned by haar cascade algorithm
    for(x,y,w,h) in face_cordinates:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    # displating the alert in the window
    cv2.putText(img, text, (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, )
    cv2.putText(img,"Press q to exit ", (500, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (95, 25, 240), )
    # displaying the frame in a window
    cv2.imshow("Face Detector",img)

    # initializng the key
    key=cv2.waitKey(1)&0xFF
    if key==ord("q"):
        break
# releasing the camera
cam.release()
# destroying all windows
cv2.destroyAllWindows()
