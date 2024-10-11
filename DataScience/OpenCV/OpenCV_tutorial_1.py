import numpy as np
import cv2 as cv
#   CHAPTER 1
# Import (i) image, (ii) video from local directory, (iii) capture video from webcam

##1. IMPORT a IMAGE from a local directory as "img" vairable
#img = cv.imread("C:/Users/HP 840 G1/Desktop/My Doc/mpic.jpg");

##showing the IMAGE
#cv.imshow("output",img)
#cv.waitKey(0) # waiting for unlimited time: cv.waitKey(miliseconds) ; here "0" means infinite time 

##2. IMPORT a VIDEO from a local directory as "ved" vairable
#ved = cv.VideoCapture("C:/Users/HP 840 G1/Downloads/Video/Kapwing - Where Content Creation Happens.mp4");

#while True:
#   success, img2 = ved.read()
#    cv.imshow("Video",img2)
#    if cv.waitKey(25) & 0xFF == ord('q') :
#        break

##3. Capture a VIDEO from a WEBCAM as "cap" vairable
#cap = cv.VideoCapture(0); #VideoCapture(0): here "0" means default WEBCAM
#cap.set(3,640) # id 3 as width 640
#cap.set(4,480) # id 3 as height 480
#cap.set(10,1000) # id 10 as brightness
#while True:
#    success, img3 = cap.read()
#    cv.imshow("Video",img3)
#    if cv.waitKey(1) & 0xFF == ord('q') :
#        break

##   CHAPTER 2 : Basic functions
# (i)Imgage Gray - cvtColor(img,cv.COLOR_BGR2GRAY)
img = cv.imread("C:/Users/HP 840 G1/Desktop/My Doc/mpic.jpg")

imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("Gray Image",imgGray)
#cv.waitKey(0)

#(ii)Imgage Blur - GaussianBlur(img,(7,7),0)
#imgBlur = cv.GaussianBlur(img,(7,7),0)
#cv.imshow("Blur Image",imgBlur)
#cv.waitKey(0)

#(iii)Imgage Canny(Edges) - Canny(img,100,100) 
#imgCanny = cv.Canny(img,100,100) # higher edges
#cv.imshow("Canny Image",imgCanny)
#imgCanny1 = cv.Canny(img,150,200) # lower edges
#cv.imshow("Canny1 Image",imgCanny1)
#cv.waitKey(0)

#(vi)Imgage Dialation(Increase the Edges) - dilate(imgCanny,kernel,iterations = 2)
#kernel = np.ones((5,5),np.uint8) # this is used for increasing the thickness of the edges
#imgDialation = cv.dilate(imgCanny,kernel,iterations = 2) # more "iteration" value more Image Dialiation
#cv.imshow("Dialation Image",imgDialation )
#cv.waitKey(0)

#(v)Imgage Eroded(Decrease the Edges of the Dialiation) - erode(imgDialation,kernel,iterations = 2)
#kernel = np.ones((5,5),np.uint8) # this is used for increasing the thickness of the edges
#imgEroded = cv.erode(imgDialation,kernel,iterations = 2) # more "iteration" value more Image Dialiation
#cv.imshow("Eroded Image",imgEroded)
#cv.waitKey(0)

##   CHAPTER 3 : Croping and Resizing
#    0 _____________ X
#       |        _______
#       |        |               |
#       |        |               |
#       |        |______|
#      Y
# Axis Format of Python OpenCV

#(i)Image Resizing : for resizing we have to know the current size after that we can resize it
img = cv.imread("C:/Users/HP 840 G1/Desktop/My Doc/mpic.jpg")

#Current size of the image
currentSizeOfimage = img.shape
print(currentSizeOfimage) #(656, 480, 3) = (height,width,RGB Scale)
cv.imshow("Current Image",img)
#Imaged resized as (300 by 300)
resizedImage = cv.resize(img,(300,300))
cv.imshow("Resized Image",resizedImage)

cv.waitKey(0)
