###1. Face Detection Code: Basically MTCNN(Multi-task cascaded CNN) detects face and keypoint detection
from mtcnn.mtcnn import MTCNN
import cv2

#image read from local disk
#image = cv2.imread("./DataScience/OpenCV/Images/images.jpeg")
#image = cv2.imread("./DataScience/OpenCV/Images/hafiz_sir.jpg")
#show image
#cv2.imshow("Image",image)
#cv2.waitKey(0)

detector = MTCNN(min_face_size=26)
#faces = detector.detect_faces(image)
#for face in faces:
#    print(face)

def create_box(image):
    image=cv2.resize(image,(300,300))
    faces = detector.detect_faces(image)
    if len(faces)>0:
        print("Number of faces = {}".format(len(faces)))
        bounding_box = faces[0]['box']
        keypoints = faces[0]['keypoints']
        cv2.rectangle(image,(bounding_box[0],bounding_box[1]),(bounding_box[0]+bounding_box[2],bounding_box[1]+bounding_box[3]),(0,155,255),2 )
        #,(0,155,255),2 
        cv2.circle(image,(keypoints['left_eye']),2,(0,155,255),2)
        cv2.circle(image,(keypoints['right_eye']),2,(0,155,255),2)
        cv2.circle(image,(keypoints['nose']),2,(0,155,255),2)
        cv2.circle(image,(keypoints['mouth_left']),2,(0,155,255),2)
        cv2.circle(image,(keypoints['mouth_right']),2,(0,155,255),2)
    else:
        print("No face Detected")
    return image

#marked_image=create_box(cv2.imread("./DataScience/OpenCV/Images/images.jpeg"))
#marked_image=create_box(cv2.imread("./DataScience/OpenCV/Images/hafiz_sir.jpg"))
marked_image=create_box(cv2.imread("./DataScience/OpenCV/Images/Mybd.jpg"))

cv2.imshow('marked',marked_image)
cv2.waitKey(0)