# importing the required  libraries
import cv2,imutils,time,os

# importing the haarcascade algorithm
alg="haarcascade_frontalface_default.xml"

# creating the Dataset directory if its not present
dataset="Datasets"
if not os.path.isdir(dataset):
    os.mkdir(dataset)

person=input("Enter the name of the person:")

# joining the variables to make the path for the dataset
path=os.path.join(dataset,person)
# creating the directory if it doesn't exist
if not os.path.isdir(path):
    os.mkdir(path)
else:
    print("Path already exists try giving an another name")

# determining the height and width of the image to be saved in the dataset
(width,height)=130,100

# initializing an object for haar cascade algorithm using cascade classifier class
haar_cascade=cv2.CascadeClassifier(alg)

# initializing camera object
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

# using while loop reading the camera frame by frame for 30 times to take 30 images
count=1
while count<31:
    print(count)
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
        # cropping the face only to save it in gray scale image into the dataset
        faceOnly=grayImage[y:y+h,x:x+w]
        # resizing the image
        faceOnly=cv2.resize(faceOnly,(width,height))
        # saving the cropped image containing only face into our dataset
        cv2.imwrite(f"{path}/{count}.jpg",faceOnly)
    # displaying the alert in the window
    cv2.putText(img, text, (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, )
    cv2.putText(img,"Press q to exit ", (500, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (95, 25, 240), )
    count = count + 1
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
print('Succesfully saved')
