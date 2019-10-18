import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)

while cv2.waitKey(1) == -1:
    _, img = cap.read()
    img = cv2.resize(img, (640 // 2, 480 // 2))
    img = cv2.blur(img, (3, 3))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.imshow('img', img)
    cv2.imshow('hsv', hsv)

    h, w, d = img.shape
    vec = hsv.cumsum(0)[-1].T[2]
    plt.plot(np.arange(w), vec)

    plt.pause(0.0001)
    plt.clf()
    plt.show(False)

