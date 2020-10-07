import dlib
import cv2
import numpy as np
import math
import requests
import time
# import os

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("../datasets/shape_predictor_68_face_landmarks.dat")

# saved_data = np.load("saved_data.npy")
# print(saved_data.shape)

# Name of candidate
name = input("Enter Your Name: ")
startt = time.time() / 60

# tracking status
moving, talking, okay = 0, 0, 0
# initialize record
url = 'http://127.0.0.1:5000/servillence'
infoo = {"name": name, "moved": moving, "talked": talking}
foo = requests.post(url, json=infoo)


# distance between two points
def dist(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face).parts()
        for point in landmarks:
            cv2.circle(frame, (point.x, point.y), 2, (255, 0, 0), 2)

        # nose = landmarks[27:36]
        # lBro = landmarks[17:22]
        # rBro = landmarks[42:48]
        # lEye = landmarks[36:42]
        # rEye = landmarks[42:48]
        # mouthOut = landmarks[48:60]
        # mouthIn = landmarks[60:68]
        # border = landmarks[0:17]

        # points 1, 29, 17 in landmarks reference
        # ---------------------------1
        r1 = dist(landmarks[0], landmarks[28])
        r2 = dist(landmarks[28], landmarks[16])
        if math.floor(abs(r1 - r2)) > 9:
            # print("Moving", moving)
            moving += 1
        else:
            # print("okay-0")
            okay += 1

        # mouth open/ close - 63, 67
        # ---------------------------2
        r3 = dist(landmarks[62], landmarks[66])

        # x<3 not talking | x>15 yawning
        if math.ceil(3 < r3 < 15):
            # print("talking", talking)
            talking += 1
        else:
            # print("okay-1")
            okay += 1
        # ---------------------------

    if ret:
        cv2.imshow("My Screen", frame)

    key = cv2.waitKey(1)

    # -_-_-_-_-
    infoo = {"name": name, "moved": moving, "talked": talking}

    current = time.time() / 60
    time_passed = current - startt # minutes
    print(time_passed)
    if time_passed >= 0.5:
        startt = current
        foo = requests.put(url, json=infoo)
        # print("Moving: ",moving)
        foo = requests.put(url, json=infoo)
        # print("Talking: ",talking)
    # -_-_-_-_-

    if key == ord('q'):
        print("Moving: ", moving)
        print("talking: ", talking)
        print("okay: ", okay)
        break

cap.release()
cv2.destroyAllWindows()
