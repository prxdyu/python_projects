# importing required libraries
import numpy as np
import cv2,os

# importing haar cascade algorithm to detect the face
haar_cascade_algorithm="haarcascade_frontalface_default.xml"
# loading the haar cascade classfier algorithm
haar_cascade=cv2.CascadeClassifier(haar_cascade_algorithm)
# initializing our dataset folder
dataset="Datasets"
text=""
color=()

# labels array contains the label of the persons in our dataset
labels=[]
# images array contains the images in our dataset
images=[]
# names set will contain the names of the persons in our datset
names={}
# intializing the id
id=0

# OS operations os walk returns 3 values a) current folder b) subfolders in the folder c) files in the folder it goes into each folder and returns the same values
for (dirs,subdirs,files) in os.walk(dataset):
    # for each subdirectory
    for subdir in subdirs:
        # assigning names using id (id is incrementing variable) (subdir contains the name of the person)
        names[id]=subdir
        # generating the pathway for the subdirectory
        subDirpath=os.path.join(dataset,subdir)
        # accessing the files(images) in each subdirectory
        for filename in os.listdir(subDirpath):
            # generating path for each image
            imagePath=subDirpath+'/'+filename
            # appending each image to the images list
            images.append(cv2.imread(imagePath,0))
            label=id
            labels.append(int(label))
        id+=1

# converting the images and labels list into numpy array for better handling
(images,labels)=[np.array(i) for i in (images,labels)]
# defining the width and size
(width,height)=(130,100)

# loading the classifier model to classify the image
model=cv2.face.LBPHFaceRecognizer_create()
# training the model with our dataset using images and its corresponding labels
model.train(images,labels)

# accessing the camera
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
count=0
# showing each frame using infinite while loop
while True:
    # reading the frame from the camera
    _,img=cam.read()
    # converting into gray scale
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # detecting the face using haar cascade algorithm it returns the x,y,w,h for the rectangle to draw around the face
    face=haar_cascade.detectMultiScale(grayImg,1.3,5)
    if len(face)==0:
        color = (255, 0, 0)
        text="No face detected"
    else:
        color = (0, 255, 0)
        text=" Face Detected !"

    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        # cropping only our face in gray scale image to give it as an input to our model
        faceImg=grayImg[y:y+h,x:x+h]
        # resizing
        faceImg=cv2.resize(faceImg,(width,height))
        # feeding the image to our model to classify it,it returns list
        prediction=model.predict(faceImg)
        person=str(names[prediction[0]])
        person_label=round(prediction[1],2)

        if prediction[1]<100:
            cv2.putText(img,f"{person}:{person_label}",(x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,color)
        else:
            cv2.putText(img,"Unknown person",(x-10,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,color)
    # displaying the alert in the window
    cv2.putText(img, text, (10, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, )
    cv2.putText(img, "Press q to exit ", (500, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (95, 25, 240), )
    cv2.imshow("Face Recognizer",img)
    # initializing the key
    key=cv2.waitKey(1)&0xFF
    if key==ord("q"):
        break
# releasing the camera
cam.release()
# destroying all windows
cv2.destroyAllWindows()







