#### https://github.com/ageitgey/face_recognition/tree/master
#### https://pypi.org/project/face-recognition/
#### https://viso.ai/computer-vision/deepface/
#### https://pyimagesearch.com/2021/04/19/face-detection-with-dlib-hog-and-cnn/
import face_recognition
import cv2
import numpy as np
import os

# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

###Load sample images and train(recognize) them one by one
## Load a sample picture and learn how to recognize it.
# jitu_image = face_recognition.load_image_file("./DataScience/OpenCV/CSE-15-Final/1702028_Jitu.png")
# jitu_face_encoding = face_recognition.face_encodings(jitu_image)[0]

# ## Load a second sample picture and learn how to recognize it.
# najmul_image = face_recognition.load_image_file("./DataScience/OpenCV/CSE-15-Final/1702069_Najmul.png")
# najmul_face_encoding = face_recognition.face_encodings(najmul_image)[0]

# ## Load a second sample picture and learn how to recognize it.
# akash_image = face_recognition.load_image_file("./DataScience/OpenCV/CSE-15-Final/1702013_Akash.jpg")
# akash_face_encoding = face_recognition.face_encodings(akash_image)[0]

# ## Load a second sample picture and learn how to recognize it.
# shaikat_image = face_recognition.load_image_file("./DataScience/OpenCV/CSE-15-Final/1702030_Shaikat.jpg")
# shaikat_face_encoding = face_recognition.face_encodings(shaikat_image)[0]


# ## Create arrays of known face encodings and their names
# known_face_encodings = [
#     najmul_face_encoding,
#     jitu_face_encoding,
#     akash_face_encoding,
#     shaikat_face_encoding
# ]
# known_face_names = [
#     "Najmul",
#     "Jitu",
#     "Akash",
#     "Shaikat"
# ]

###Load sample images and train(recognize) them by a folder
## Load a sample picture and learn how to recognize it.

def load_images_from_folder_and_recognize(folder):
    "this function loads images from a folder and train with their name"
    known_face_names=[]
    known_face_encodings=[]
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        img_path = os.path.join(folder,filename)
        if img_path is not None:
            #filename with extension
            #print(filename)
            #filename without extension
            indexoflastdot = filename.rfind(".")
            onlyfilename=filename[:indexoflastdot]

            # Load a sample picture and learn how to recognize it.
            image = face_recognition.load_image_file(img_path)
            image_encoding = face_recognition.face_encodings(image)[0]
            known_face_names.append(onlyfilename)
            known_face_encodings.append(image_encoding)
            print(filename+" recognizing complete")
            images.append(img)
    return known_face_names,known_face_encodings

known_face_names,known_face_encodings=load_images_from_folder_and_recognize('./DataScience/OpenCV/CSE-15-Final/')

## Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

## Get a reference to webcam #0 or ipcam (the default one)
video_capture = cv2.VideoCapture(0)
#video_capture = cv2.VideoCapture('rtsp://foscamr2:foscamr2@192.168.1.2:88/videoMain')
#video_capture = cv2.VideoCapture('rtsp://visitor1:visitor1@192.168.1.2:88/videoMain')

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        #rgb_small_frame = small_frame[:, :, ::-1] #not works
        #rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 115, 115), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (255, 0, 0), cv2.FILLED)
        #font = cv2.FONT_HERSHEY_DUPLEX
        #font = cv2.FONT_HERSHEY_TRIPLEX
        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.53, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()

#########Using Multi-processing############
# import face_recognition
# import cv2
# from multiprocessing import Process, Manager, cpu_count, set_start_method
# import time
# import numpy as np
# import threading
# import platform


# # This is a little bit complicated (but fast) example of running face recognition on live video from your webcam.
# # This example is using multiprocess.

# # PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# # OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# # specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.


# # Get next worker's id
# def next_id(current_id, worker_num):
#     if current_id == worker_num:
#         return 1
#     else:
#         return current_id + 1


# # Get previous worker's id
# def prev_id(current_id, worker_num):
#     if current_id == 1:
#         return worker_num
#     else:
#         return current_id - 1


# # A subprocess use to capture frames.
# def capture(read_frame_list, Global, worker_num):
#     # Get a reference to webcam #0 (the default one)
#     #video_capture = cv2.VideoCapture(0)
#     video_capture = cv2.VideoCapture('rtsp://foscamr2:foscamr2@192.168.1.2:88/videoMain')
#     # video_capture.set(3, 640)  # Width of the frames in the video stream.
#     # video_capture.set(4, 480)  # Height of the frames in the video stream.
#     # video_capture.set(5, 30) # Frame rate.
#     print("Width: %d, Height: %d, FPS: %d" % (video_capture.get(3), video_capture.get(4), video_capture.get(5)))

#     while not Global.is_exit:
#         # If it's time to read a frame
#         if Global.buff_num != next_id(Global.read_num, worker_num):
#             # Grab a single frame of video
#             ret, frame = video_capture.read()
#             read_frame_list[Global.buff_num] = frame
#             Global.buff_num = next_id(Global.buff_num, worker_num)
#         else:
#             time.sleep(0.01)

#     # Release webcam
#     video_capture.release()


# # Many subprocess use to process frames.
# def process(worker_id, read_frame_list, write_frame_list, Global, worker_num):
#     known_face_encodings = Global.known_face_encodings
#     known_face_names = Global.known_face_names
#     while not Global.is_exit:

#         # Wait to read
#         while Global.read_num != worker_id or Global.read_num != prev_id(Global.buff_num, worker_num):
#             # If the user has requested to end the app, then stop waiting for webcam frames
#             if Global.is_exit:
#                 break

#             time.sleep(0.01)

#         # Delay to make the video look smoother
#         time.sleep(Global.frame_delay)

#         # Read a single frame from frame list
#         frame_process = read_frame_list[worker_id]

#         # Expect next worker to read frame
#         Global.read_num = next_id(Global.read_num, worker_num)

#         # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
#         #rgb_frame = frame_process[:, :, ::-1] not works
#         rgb_frame = np.ascontiguousarray(frame_process[:, :, ::-1])

#         # Find all the faces and face encodings in the frame of video, cost most time
#         face_locations = face_recognition.face_locations(rgb_frame)
#         face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#         # Loop through each face in this frame of video
#         for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#             # See if the face is a match for the known face(s)
#             matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

#             name = "Unknown"

#             # If a match was found in known_face_encodings, just use the first one.
#             if True in matches:
#                 first_match_index = matches.index(True)
#                 name = known_face_names[first_match_index]

#             # Draw a box around the face
#             cv2.rectangle(frame_process, (left, top), (right, bottom), (0, 0, 255), 2)

#             # Draw a label with a name below the face
#             cv2.rectangle(frame_process, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
#             font = cv2.FONT_HERSHEY_DUPLEX
#             cv2.putText(frame_process, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

#         # Wait to write
#         while Global.write_num != worker_id:
#             time.sleep(0.01)

#         # Send frame to global
#         write_frame_list[worker_id] = frame_process

#         # Expect next worker to write frame
#         Global.write_num = next_id(Global.write_num, worker_num)


# if __name__ == '__main__':

#     # Fix Bug on MacOS
#     if platform.system() == 'Darwin':
#         set_start_method('forkserver')

#     # Global variables
#     Global = Manager().Namespace()
#     Global.buff_num = 1
#     Global.read_num = 1
#     Global.write_num = 1
#     Global.frame_delay = 0
#     Global.is_exit = False
#     read_frame_list = Manager().dict()
#     write_frame_list = Manager().dict()

#     # Number of workers (subprocess use to process frames)
#     if cpu_count() > 2:
#         worker_num = cpu_count() - 1  # 1 for capturing frames
#     else:
#         worker_num = 2

#     # Subprocess list
#     p = []

#     # Create a thread to capture frames (if uses subprocess, it will crash on Mac)
#     p.append(threading.Thread(target=capture, args=(read_frame_list, Global, worker_num,)))
#     p[0].start()

#     # Load a sample picture and learn how to recognize it.
#     jitu_image = face_recognition.load_image_file("./DataScience/OpenCV/CSE-15-Final/1702028_Jitu.png")
#     jitu_face_encoding = face_recognition.face_encodings(jitu_image)[0]

#     # Load a second sample picture and learn how to recognize it.
#     najmul_image = face_recognition.load_image_file("./DataScience/OpenCV/CSE-15-Final/1702069_Najmul.png")
#     najmul_face_encoding = face_recognition.face_encodings(najmul_image)[0]

#     # Load a second sample picture and learn how to recognize it.
#     akash_image = face_recognition.load_image_file("./DataScience/OpenCV/CSE-15-Final/1702013_Akash.jpg")
#     akash_face_encoding = face_recognition.face_encodings(akash_image)[0]

#     # Load a second sample picture and learn how to recognize it.
#     shaikat_image = face_recognition.load_image_file("./DataScience/OpenCV/CSE-15-Final/1702030_Shaikat.jpg")
#     shaikat_face_encoding = face_recognition.face_encodings(shaikat_image)[0]


#     # Create arrays of known face encodings and their names
#     Global.known_face_encodings = [
#         najmul_face_encoding,
#         jitu_face_encoding,
#         akash_face_encoding,
#         shaikat_face_encoding
#     ]
#     Global.known_face_names = [
#         "Najmul",
#         "Jitu",
#         "Akash",
#         "Shaikat"
#     ]

#     # Create workers
#     for worker_id in range(1, worker_num + 1):
#         p.append(Process(target=process, args=(worker_id, read_frame_list, write_frame_list, Global, worker_num,)))
#         p[worker_id].start()

#     # Start to show video
#     last_num = 1
#     fps_list = []
#     tmp_time = time.time()
#     while not Global.is_exit:
#         while Global.write_num != last_num:
#             last_num = int(Global.write_num)

#             # Calculate fps
#             delay = time.time() - tmp_time
#             tmp_time = time.time()
#             fps_list.append(delay)
#             if len(fps_list) > 5 * worker_num:
#                 fps_list.pop(0)
#             fps = len(fps_list) / np.sum(fps_list)
#             print("fps: %.2f" % fps)

#             # Calculate frame delay, in order to make the video look smoother.
#             # When fps is higher, should use a smaller ratio, or fps will be limited in a lower value.
#             # Larger ratio can make the video look smoother, but fps will hard to become higher.
#             # Smaller ratio can make fps higher, but the video looks not too smoother.
#             # The ratios below are tested many times.
#             if fps < 6:
#                 Global.frame_delay = (1 / fps) * 0.75
#             elif fps < 20:
#                 Global.frame_delay = (1 / fps) * 0.5
#             elif fps < 30:
#                 Global.frame_delay = (1 / fps) * 0.25
#             else:
#                 Global.frame_delay = 0

#             # Display the resulting image
#             cv2.imshow('Video', write_frame_list[prev_id(Global.write_num, worker_num)])

#         # Hit 'q' on the keyboard to quit!
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             Global.is_exit = True
#             break

#         time.sleep(0.01)

#     # Quit
#     cv2.destroyAllWindows()
