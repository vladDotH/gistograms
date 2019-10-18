import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('image.jpg')
hsv = np.array(cv2.cvtColor(img, cv2.COLOR_BGR2HSV))

h, w, d = img.shape

vec = hsv.cumsum(0)[-1]

plt.plot(np.arange(w), vec)

plt.show()
