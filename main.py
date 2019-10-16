import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('image.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

gst = np.ones((480, 640, 3)) * 255

cv2.imshow('img', img)

h, w, d = img.shape

vec = []

for i in range(w):
    s = 0
    for j in range(h):
        s += hsv[j][i][1]
    vec.append(s)

plt.plot(list(range(w)), vec)

plt.show()

cv2.waitKey(0)