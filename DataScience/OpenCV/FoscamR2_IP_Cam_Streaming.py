###opencv guide: https://docs.opencv.org/4.x/
##WORKED with rtsp and videoMain
####How to make it 
##step-1: determine the ip and port
##step-2: connect the cam with ethernet cable
##step-3: login with credientials
##step-4: quick setup the cam and connect it wirelessly and it can remember one wifi at a time.
##step-5: turn off dhcp, set a static ip and ports
###Note: when ip cam is connected to the internet properly only than it can operate

import cv2

print("Before URL")
#cap = cv2.VideoCapture('rtsp://foscamr2:foscamr2@192.168.1.2:88/H264?ch=1&subtype=0')
#cap = cv2.VideoCapture('rtsp://foscamr2:foscamr2@192.168.1.2:88/1')
cap = cv2.VideoCapture('rtsp://foscamr2:foscamr2@192.168.1.2:88/videoMain')
print("After URL")

while True:

    #print('About to start the Read command')
    ret, frame = cap.read()
    #print('About to show frame of Video.')
    cv2.imshow("Capturing",frame)
    #print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

#----------------------------
##NOT WORKED: using http
# import cv2

# cap = cv2.VideoCapture('http://192.168.1.2:88//video')

# while(True):
#     ret, frame = cap.read()
#     cv2.imshow('frame',frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         cv2.destroyAllWindows()
#         break
#-------------------

##WORKED
# import cv2
# import queue
# import time
# import threading
# q=queue.Queue()

# def Receive():
#     print("start Reveive")
#     cap = cv2.VideoCapture("rtsp://foscamr2:foscamr2@192.168.1.2:88/videoMain")
#     ret, frame = cap.read()
#     q.put(frame)
#     while ret:
#         ret, frame = cap.read()
#         q.put(frame)


# def Display():
#      print("Start Displaying")
#      while True:
#          if q.empty() !=True:
#             frame=q.get()
#             cv2.imshow("frame1", frame)
#          if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break
            
# if __name__=='__main__':
#     p1=threading.Thread(target=Receive)
#     p2 = threading.Thread(target=Display)
#     p1.start()
#     p2.start()
##-------------------------
#WORKED
# import cv2
# import time
# vs = cv2.VideoCapture("rtsp://foscamr2:foscamr2@192.168.1.2:88/videoMain")
# while True:
#     ret,frame = vs.read()
#     if not(ret):
#         st = time.time()
#         vs = cv2.VideoCapture("rtsp://foscamr2:foscamr2@192.168.1.2:88/videoMain")
#         print("tot time lost due to reinitialization : ",time.time()-st)
#         continue

#     cv2.imshow("Current frame", frame)
#     cv2.waitKey(0)
#--------------------------

#WORKED
# import cv2

# def main(args):

#     #cap = cv2.VideoCapture(0) #default camera
#     cap = cv2.VideoCapture('rtsp://foscamr2:foscamr2@192.168.1.2:88/videoMain') #IP Camera
    
#     while(True):
#         ret, frame = cap.read()
#         frame=cv2.resize(frame, (960, 540)) 
#         cv2.imshow('Capturing',frame)
        
#         if cv2.waitKey(1) & 0xFF == ord('q'): #click q to stop capturing
#             break

#     cap.release()
#     cv2.destroyAllWindows()
#     return 0

# if __name__ == '__main__':
#     import sys
#     sys.exit(main(sys.argv))