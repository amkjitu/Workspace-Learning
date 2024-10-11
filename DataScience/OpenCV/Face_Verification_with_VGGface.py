import cv2
import numpy as np
from torch import tensor
from mtcnn.mtcnn import MTCNN
from keras_vggface.utils import preprocess_input
from keras_vggface.vggface import VGGFace
from scipy.spatial.distance import cosine
import matplotlib.pyplot as plt
import warnings

#to ignore future warnings
#warnings.filterwarnings("ignore",category=FutureWarning())

####1. Face Detector##### 
face_detector=MTCNN(min_face_size=26)

#creates a box around the face only
def create_box(image):
    #image=cv2.resize(image,(300,300))
    faces = face_detector.detect_faces(image)
    no_of_faces = len(faces)
    print("Number of faces = {}".format(no_of_faces))
    if no_of_faces>0:
        for i in range(no_of_faces):
            bounding_box = faces[i]['box']
            keypoints = faces[i]['keypoints']
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
#marked_image=create_box(cv2.imread("./DataScience/OpenCV/Images/Mybd.jpg"))

#cv2.imshow('marked', marked_image)
#cv2.waitKey(0)

####2. Face Extract : that is cropping the face only with the help of create box. VGGface used (224x224) dimension.
def extract_faces(image,resize=(224,224)):
    ##one
    faces = face_detector.detect_faces(image)
    no_of_faces = len(faces)
    print("Number of faces = {}".format(no_of_faces))

    x1,y1,width,height = faces[0]['box']
    x2,y2 = x1+width, y1+height
    face_boundary = image[y1:y2, x1:x2]
    face_image=cv2.resize(face_boundary,resize)
    return face_image

    ##many
    # faces = face_detector.detect_faces(image)
    # no_of_faces = len(faces)
    # print("Number of faces = {}".format(no_of_faces))

    # if no_of_faces>0:
    #     cropped_image=[]
    #     for i in range(no_of_faces):
    #         x1,y1,width,height = faces[i]['box']
    #         x2,y2 = x1+width, y1+height
    #         face_boundary = image[y1:y2, x1:x2]
    #         face_image=cv2.resize(face_boundary,resize)
    #         cropped_image.append(face_image)
    #     return cropped_image
    # else:
    #     print("Face can't be extracted")

#cropped_faces=extract_faces(cv2.imread("./DataScience/OpenCV/Images/Mybd.jpg"))

####DISPLAYING Images##########
##1. Displaying the croped images one by one
# for cropped_face in cropped_faces:
#     cv2.imshow('marked', cropped_faces)
#     cv2.waitKey(0)

###2. Displaying the croped images in a horizontal grid
#image_grid_hori = np.concatenate(cropped_faces,axis=(0,1))
#cv2.imshow('Horizontal', image_grid_hori)
#cv2.waitKey(0)

###3. Displaying the croped images in a grid(4x4) using Matplotlib
#plt.figure(figsize=(16, 16))
# for i, k in enumerate(cropped_faces):
#     #image = Image.open(k)
#     plt.subplot(4, 4, i+1 )
#     plt.imshow(k)
#     plt.title("Image "+str(i+1))
# plt.show()

###4. Displaying the croped images in a grid(4x4) using torch
# ## import required library
# # import torch
# import torchvision
# #from torchvision.io import read_image
# from torchvision.utils import make_grid
# import torchvision.transforms as transforms
  
# # read images from computer
# # a = read_image('a.png')
# # b = read_image('b.png')
# # c = read_image('c.png')
# # d = read_image('d.png')
# # e = read_image('e.png')
# # f = read_image('f.png')
  
# # make grid from the input images
# # set nrow=3, and padding=25
# #Grid = make_grid([a, b, c, d, e, f], nrow=3, padding=25)

# # Define a transform to convert the image to torch tensor
# transform = transforms.Compose([transforms.ToTensor()])
  
# # Convert the image to Torch tensor
# img_tensor = []
# for cimage in cropped_faces:
#     img_tensor.append(transform(cimage))
# Grid = make_grid(img_tensor, nrow=3, padding=25)
  
# # display result
# img = torchvision.transforms.ToPILImage()(Grid)
# img.show()

#####Feature extration from the croped faces
####VGGface model: a pretrained model using 3.3 Mi faces of celebraties
####Embedding is the final layer vector of a model
def get_embeddings(cropped_faces):
    face = np.asarray(cropped_faces,'float32')
    ##'version=2' means resnet50 (version=1 means vgg60)
    face = preprocess_input(face,version=2)
    ##in this model 'include_top = false' means 'dont include the classification'
    ##'pooling = avg' means average the filter and give the output
    model = VGGFace(model='resnet50',include_top=False, input_shape=(224,224,3), pooling='avg')
    return model.predict(face)

####Compare similarities between faces. 
####Passing two images and get their embedding(features)
####Compare the cosine distance of the two embedding vestors. if score <=0.5 : matched, else not matched
def get_dissimilarity(cropped_faces):
    embeddings = get_embeddings(cropped_faces)
    score = cosine(embeddings[0],embeddings[1])
    #Embedding contains 244 values of a vector
    print("Embedding0 = {}, Embedding1 = {}".format(embeddings[0],embeddings[1]))
    #print("Cosine distance, score = {}".format(score))
    if score <= 0.5:
        return "Face Matched",score
    else:
        return "Face not Matched",score

#####Data Input of the model
faces = [extract_faces(image) for image in [cv2.imread('./DataScience/OpenCV/Images/images.jpeg'),cv2.imread('./DataScience/OpenCV/Images/hafiz_sir.jpg')] ]
result=get_dissimilarity(faces)
print(result) #####Data Input of the model

faces = [extract_faces(image) for image in [cv2.imread('./DataScience/OpenCV/Images/images.jpeg'),cv2.imread('./DataScience/OpenCV/Images/images.jpeg')] ]
result=get_dissimilarity(faces)
print(result) 





