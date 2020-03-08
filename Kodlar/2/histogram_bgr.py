import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("../images/image.jpg") 

cv2.namedWindow("image", cv2.WINDOW_FREERATIO)
cv2.imshow("image", image)

# https://docs.opencv.org/master/d1/db7/tutorial_py_histogram_begins.html
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([image], [i], None, [256], [0,256])
    plt.plot(histr, color=col)
    plt.xlim([0,256])
plt.show()

cv2.destroyAllWindows()
