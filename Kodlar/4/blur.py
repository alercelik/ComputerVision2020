import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../images/itu.jpg')
cv2.imshow("img", img)


for kernel_size in [3,5,7,9,11,15]:
	blurred = cv2.blur(img, (kernel_size, kernel_size))

	cv2.imshow("blurred {}".format(kernel_size), blurred)
	cv2.waitKey()

cv2.destroyAllWindows()
