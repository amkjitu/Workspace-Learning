#################Using Webcam###############
import pickle 
import cv2
import numpy as np

##camera settings
cam_id = 1 #1 for droidcam
#width,height=1024,768
width,height=768,1024

##initialize variable
cap = cv2.VideoCapture(cam_id)
#cap.set(3,width)
#cap.set(4,height)

points = np.zeros((4,2),int)
counter = 0

##mouse points
def mousePoints(event,x,y,flags,params):
    global counter

    #if the left button of the mouse clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        points[counter]=x,y #store clicked point
        counter+=1 #increment counter
        print(f"Clicked points: \n {points}")

#warp captured image
def warpImage(img,points,size=[width,height-200]):
    pts1=np.float32(points) #converts original points to float32
    pts2=np.float32([ [0,0], [size[0],0], [0,size[1]], [size[0],size[1]] ]) #target warping points
    matrix=cv2.getPerspectiveTransform(pts1,pts2) #calculate the perpective
    output_wrapped_image=cv2.warpPerspective(img,matrix, (size[0],size[1])) #warp image
    return output_wrapped_image,matrix



###FRAME CAPTURING LOOP
while True:

    #0. initialize cam read to produce image
    success,img = cap.read()

    #3. Save selected 4 points of the map border the to file
    if counter == 4:
        path = "DataScience/OpenCV/Virtual-Map-Computer-Vission/1_Get-Corner-Points/map.p"
        fileObj = open(path,"wb")
        pickle.dump(points,fileObj) #store the coordinates to file
        fileObj.close()

        print("Points saved to file: map.p")
        counter+=1 #to avoid printing 

        #4. wrap the image
        warpedImgOutput,matrix = warpImage(img,points)
        #5. Display the warpped
        cv2.imshow("Output Image",warpedImgOutput)

    

    #2. Draw circle to the clicked points of the image
    for x in range(0,4):
        cv2.circle(img, (points[x][0],points[x][1]), 3 , (0,255,0), cv2.FILLED)

    #1. Show image
    
    #cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
    #cv2.resizeWindow("Original Image", 768, 1024)
    #img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("Original Image",img)
    cv2.setMouseCallback("Original Image",mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break

#release resources
cap.release()
cv2.destroyAllWindows()



# #############Using Local Image############
# import pickle 
# import cv2
# import numpy as np

# #width,height=1024,768
# width,height=768,768

# points = np.zeros((4,2),int)
# counter = 0

# ##mouse points
# def mousePoints(event,x,y,flags,params):
#     global counter
#     if event == cv2.EVENT_LBUTTONDOWN:
#         points[counter]=x,y #store clicked point
#         counter+=1 #increment counter
#         print(f"Clicked points: {points}")

# #warp captured image
# def warpImage(img,points,size=[width,height]):
#     pts1=np.float32(points) #converts original points to float32
#     pts2=np.float32([ [0,0], [size[0],0], [0,size[1]], [size[0],size[1]] ]) #target warping points
#     matrix=cv2.getPerspectiveTransform(pts1,pts2) #calculate the perpective
#     output_wrapped_image=cv2.warpPerspective(img,matrix, (size[0],size[1])) #warp image
#     return output_wrapped_image,matrix

# while True:

#     #3. Save selected points to file
#     if counter == 4:
#         path = "DataScience/OpenCV/Virtual-Map-Computer-Vission/1_Get-Corner-Points/"
#         fileObj = open(path+"map.p","wb")
#         pickle.dump(points,fileObj)
#         fileObj.close()
#         print("Points saved to file: map.p")

#         #4. wrap the image
#         imgOutput,matrix = warpImage(img,points)
#         #5. Display the warpped
#         cv2.imshow("Output Image",imgOutput)


#     img = cv2.imread("DataScience/OpenCV/Virtual-Map-Computer-Vission/Map_BD_64_Dis.png", cv2.IMREAD_COLOR)

#     #2. Draw circle to the clicked points of the image
#     for x in range(0,4):
#         cv2.circle(img, (points[x][0],points[x][1]), 3 , (0,255,0), cv2.FILLED)

#     #1. Show image
#     cv2.imshow("Original Image",img)
#     cv2.setMouseCallback("Original Image",mousePoints)

#     if cv2.waitKey(0) & 0xFF == ord('q'):
#         break

# #release resources
# cv2.destroyAllWindows()








