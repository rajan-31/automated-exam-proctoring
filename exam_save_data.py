import cv2
import dlib
import numpy as np
import os

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("../datasets/shape_predictor_68_face_landmarks.dat")

print('press "c" to capture and then "q" to exit')

cap = cv2.VideoCapture(0)
frames = []
data = np.array([])

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face).parts()

        data = np.array([[point.x - face.left(), point.y - face.top()] for point in landmarks])
        for point in data:
            cv2.circle(frame, (point[0], point[1]), 2, (0, 0, 255), 2)
    if ret:
        cv2.imshow("My Screen", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    if key == ord("c"):
        if data.any():
            frames.append(data)
            print("Captured successfully!!!")
        else: print("Please try again!!")

X = np.array(frames[0])
f_name = "saved_data.npy"
np.save(f_name, X)

cap.release()
cv2.destroyAllWindows()