import pickle 
import cv2
import numpy as np
import cvzone
import os.path
from cvzone.HandTrackingModule import HandDetector

##camera settings
cam_id = 1 #1 for droidcam
#width,height=1024,768
width,height=768,1024

#dot p file of map and districts
map_file_path = "DataScience/OpenCV/Virtual-Map-Computer-Vission/1_Get-Corner-Points/map.p"
districts_file_path = "DataScience/OpenCV/Virtual-Map-Computer-Vission/2_Get-District-Polygons/districts.p"

#loading map coordinates from map.p file
fileObj = open(map_file_path,"rb")
map_points = pickle.load(fileObj)
fileObj.close()
print(f"Loaded map coordinates \n {map_points}")

if(os.path.isfile(districts_file_path)):
    #loading district coordinates from district.p file
    fileObj = open(districts_file_path,"rb")
    polygons = pickle.load(fileObj)
    fileObj.close()
    print(f"Loaded {len(polygons)} districts")
else:
    polygons = []    

##initializing webcam
cap = cv2.VideoCapture(cam_id)
cap.set(3,width)
cap.set(4,height)

#Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

##warp captured image
def warpImage(img,map_points,size=[width,height-200]):
    pts1=np.float32(map_points) #converts original points to float32
    pts2=np.float32([ [0,0], [size[0],0], [0,size[1]], [size[0],size[1]] ]) #target warping points
    matrix=cv2.getPerspectiveTransform(pts1,pts2) #calculate the perpective
    output_wrapped_image=cv2.warpPerspective(img,matrix, (size[0],size[1])) #warp image
    return output_wrapped_image,matrix

def warp_single_point(point,matrix):
    #convert the point to homogeneous coordinates
    point_homogeneous = np.array([ [point[0], point[1], 1] ],dtype=np.float32)
    #Apply the perspective transformation to the point
    point_homogeneous_transformed = np.dot(matrix,point_homogeneous.T).T
    #convert back to non-homogeneous coordinates
    point_warped = point_homogeneous_transformed[0,:2]/point_homogeneous_transformed[0,2]
    return point_warped

def get_finger_location(img,warped_img):
    #Find the hands in the current frame
    hands, img = detector.findHands(img, draw=False, flipType = True)

    #check if any hands are detected
    if hands:
        #information for the 1st hand detected
        hand1 = hands[0] #get the first hand detected
        #List of 21 landmarks fo the first hand
        indexFinger = hand1["lmList"][8][0:2] 
        cv2.circle(img, indexFinger, 5, (255,0,255), cv2.FILLED)
        warped_point = warp_single_point(indexFinger,matrix)
        warped_point = int(warped_point[0]), int(warped_point[1])
        cv2.circle(warped_img,warped_point,10,(255,0,0),cv2.FILLED)

    else:
        warped_point = None

    return warped_point

def create_overlay_image(polygons, warped_point, imgOverlay):
    
    #loop through all the districts
    for polygon, name in polygons:
        polygon_np = np.array(polygon,np.int32).reshape((-1,1,2))
        #checks if a point is within that polygon
        result = cv2.pointPolygonTest(polygon_np,warped_point,False)
        if result >= 0:
            cv2.polylines(imgOverlay, [np.array(polygon)], isClosed=True, color=(0,255,0), thickness=2)
            cv2.fillPoly(imgOverlay, [np.array(polygon)], (0,255,0))
            cvzone.putTextRect(imgOverlay, name, polygon[0], scale=1, thickness=1)
            cvzone.putTextRect(imgOverlay, name, (0,800), scale=6, thickness=4)

    #cv2.imshow("Overlay",imgOverlay)
    return imgOverlay


##reverse warp
def inverseWarpImage(img,imgOverlay,map_points):
    
    #convert map_points to NumPy array
    map_points = np.array(map_points, dtype=np.float32)
    #Define the destination points for the overlay image
    destination_points = np.array([ [0,0], [imgOverlay.shape[1]-1, 0], [0, imgOverlay.shape[0]-1], [imgOverlay.shape[1]-1, imgOverlay.shape[0]-1] ], dtype=np.float32)

    #Calculate the perspective transform matrix
    M = cv2.getPerspectiveTransform(destination_points,map_points)
    #warp the overlay image to fit the perspective of the original image 
    wraped_overlay=cv2.warpPerspective(imgOverlay,M, (img.shape[1], img.shape[0]))
    #combine the original image with the warped overlay
    result = cv2.addWeighted(img,1,wraped_overlay,0.65,0,wraped_overlay)

    return result
        



###FRAME CAPTURING LOOP
while True:

    #0. initialize cam read to produce image
    success,img = cap.read()

    #1. warp captured image by the map coordinates got from map.py created by the get_map.py
    warped_img, matrix = warpImage(img,map_points)

    #copying original image
    imgOutput = img.copy()

    #Find the hand and its landmarks
    warped_point = get_finger_location(img,warped_img)

    #creating a black image
    h,w,_ = warped_img.shape
    imgOverlay = np.zeros((h,w,3), dtype=np.uint8)


    #if there is a warped point 
    if warped_point:
        imgOverlay = create_overlay_image(polygons, warped_point, imgOverlay)
        imgOutput = inverseWarpImage(img,imgOverlay,map_points)

    # #stack the images in a single Window
    # stacked_image = cvzone.stackImages([img,warped_img,imgOutput,imgOverlay],2,0.3)
    # cv2.imshow("Stacked Images",stacked_image)

    #final image
    cv2.imshow("Output Image",imgOutput)


    #Stop Capture
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#release resources
cap.release()
cv2.destroyAllWindows()