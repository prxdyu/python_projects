# importing library
import cv2,imutils

# asking the hsv values of the object to be detected
h1=int(input("Enter the Hue value for low 0-255: "))
s1=int(input("Enter the Saturation value for low 0-255: "))
v1=int(input("Enter the Value for low 0-255: "))
h2=int(input("Enter the Hue value for high 0-255: "))
s2=int(input("Enter the Saturation value for high 0-255: "))
v2=int(input("Enter the Value for high 0-255: "))
hsvLower=(h1,s1,v1)
hsvUpper=(h2,s2,v2)

# opening the camera to capture video
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

text=None
color=None

# continuously obtaining the image using while loop
while True:
    # obtaining the camera image
    _, img = cam.read()
    # image preprocessing
    img=imutils.resize(img,width=600)
    # applying gaussian blur
    blurred=cv2.GaussianBlur(img,(11,11),0)
    # converting the BGR to HSV
    hsv_img=cv2.cvtColor(blurred,cv2.COLOR_BGR2HSV)
    # finding the mask ie the object to be detected by passing its HSV values
    mask=cv2.inRange(hsv_img, hsvLower, hsvUpper)
    # applying erosion and dilation
    mask=cv2.erode(mask,None,iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    # finding the contours for the object
    (contours,dummy)=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    # checking if we got any object in the screen means the length of the contour list is not zero
    if len(contours)>0:
        # find the the contours with the largest contour area in the contours list
        c=max(contours,key=cv2.contourArea)
        # finding the minimum enclosing circle for the largest contour area this function returns the center of the circle and the radius of the minimum enclosing circle
        ((x,y),radius)=cv2.minEnclosingCircle(c)
        # finding the moments of the object which is used to find the center of the object not the circle
        M=cv2.moments(c)
        # finding the center of the object using  moments
        center= (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # specifying the minimum radius required to draw the circle around the object
        if radius>10:
            # drawing the outer circle
            cv2.circle(img,(int(x),int(y)),int(radius),(0,255,255),2)
            # drawing the inner dot like circle
            cv2.circle(img,center,5,(0,0,255),-1)
            text="Object detected !"
            color=(0,255,0)
        else:
            text="No object detected "
            # blue color
            color=(95, 25, 240)

    cv2.putText(img, text, (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5,color )
    cv2.putText(img, "Press q to exit ", (450,20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), )
    cv2.imshow("Detector",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()


