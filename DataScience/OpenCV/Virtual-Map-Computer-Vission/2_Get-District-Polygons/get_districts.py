import pickle 
import cv2
import numpy as np
import os.path

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

##variables 
counter = 0 #counter to keep track of how many polygons have been created
current_polygon = [] #temporary list to store the four points of th current polygon being marked
polygons = [] # list of coordinates, district

if(os.path.isfile(districts_file_path)):
    #loading district coordinates from district.p file
    fileObj = open(districts_file_path,"rb")
    polygons = pickle.load(fileObj)
    fileObj.close()
    print(f"Loaded {len(polygons)} districts")    

##initializing webcam
cap = cv2.VideoCapture(cam_id)
#cap.set(3,width)
#cap.set(4,height)

##warp captured image
def warpImage(img,points,size=[width,height-200]):
    pts1=np.float32(points) #converts original points to float32
    pts2=np.float32([ [0,0], [size[0],0], [0,size[1]], [size[0],size[1]] ]) #target warping points
    matrix=cv2.getPerspectiveTransform(pts1,pts2) #calculate the perpective
    output_wrapped_image=cv2.warpPerspective(img,matrix, (size[0],size[1])) #warp image
    return output_wrapped_image,matrix

##mouse points
def mousePoints(event,x,y,flags,params):
    global counter, current_polygon
    #if the left button of the mouse clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        current_polygon.append((x,y))
        

###FRAME CAPTURING LOOP
while True:

    #0. initialize cam read to produce image
    success,img = cap.read()

    #1. warp captured image by the map coordinates got from map.py created by the get_map.py
    warped_img , _ = warpImage(img,map_points)
    
    #print(current_polygon) #coordinates of the current polygon

    #storing key in a variable for further to check a specific key
    key = cv2.waitKey(1)

    #3. to save a district polygone
    if key == ord("s") and len(current_polygon) > 2:
        district_name = input("Enter the name of the district: ")
        polygons.append([current_polygon,district_name]) #add the coordinates and name of the current district
        current_polygon = [] # reseting the current polygon for next use
        counter += 1 #increment the counter
        print(f"Numbers of districts saved = {len(polygons)}")
    
    #4. Quit from drawing polygon and store the coordinates to file
    if key == ord("q"):
        fileObj = open(districts_file_path,"wb")
        pickle.dump(polygons,fileObj) #storing the coordinates
        fileObj.close()
        print(f"Saved {len(polygons)} districts")

    #5. Delete a polygon 
    if key == ord("d"):
        print(f"{len(polygons)} Districts are in the list: ")
        for pair in polygons:
            print(pair[1])
        distodel = input("Enter the name of the district to be deleted: ")
        polygons = [polygon for polygon in polygons if polygon[1] != distodel]


    #2. draw polygon according to the map
    if current_polygon:
        cv2.polylines(warped_img, [np.array(current_polygon)], isClosed=True, color=(0,0,255), thickness=2)

    overlay = warped_img.copy() # a copy of the image warped

    ## Draw all the previously drawn polygons loaded from districts.p
    for polygon,names in polygons:
        cv2.polylines(warped_img, [np.array(polygon)], isClosed=True, color=(0,255,0), thickness=2)
        cv2.fillPoly(overlay,[np.array(polygon)], color=(0,255,0))

    cv2.addWeighted(overlay, 0.35, warped_img, 0.65, 0, warped_img) #Blend polylines with fill 



    cv2.imshow("Warped Image",warped_img)


    cv2.setMouseCallback("Warped Image",mousePoints)

    if key & 0xFF == ord('q'):
         break

#release resources
cap.release()
cv2.destroyAllWindows()

