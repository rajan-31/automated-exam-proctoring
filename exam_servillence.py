import dlib
import cv2
import numpy as np
import math
# import os

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("../datasets/shape_predictor_68_face_landmarks.dat")

saved_data = np.load("saved_data.npy")
# print(saved_data.shape)

# tracking status
moving, talking, okay = 0, 0, 0

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

        # points 1, 29, 17 in landmark reference
        # ---------------------------1
        r1 = dist(landmarks[0], landmarks[28])
        r2 = dist(landmarks[28], landmarks[16])
        if math.floor(abs(r1 - r2)) > 9:
            print("Moving", moving)
            moving += 1
        else:
            # print("okay-0")
            okay += 1
        # mouth open/ close - 63, 67
        # ---------------------------2
        r3 = dist(landmarks[62], landmarks[66])

        # x<3 not talking | x>15 yawning
        if math.ceil(3 < r3 < 15):
            print("talking", talking)
            talking += 1
        else:
            # print("okay-1")
            okay += 1
        # ---------------------------

    if ret:
        cv2.imshow("My Screen", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        print("Moving: ", moving)
        print("talking: ", talking)
        print("okay: ", okay)
        break

cap.release()
cv2.destroyAllWindows()
