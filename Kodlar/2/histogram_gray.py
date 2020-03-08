import cv2
import numpy as np
from matplotlib import pyplot as plt

# fotoğrafı grayscale olarak oku, 0
image = cv2.imread("../images/wiki.jpg", 0) 


cv2.namedWindow("image", cv2.WINDOW_FREERATIO)
cv2.imshow("image", image)

plt.hist(image.flatten(), 256, [0,256])
plt.show()
