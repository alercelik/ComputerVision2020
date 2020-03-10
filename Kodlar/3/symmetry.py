import cv2
import numpy as np

image = cv2.imread('../images/itu.jpg')

print("image dimensions: {}".format(image.shape))


symmetry_by_x_axis = image[::-1]
symmetry_by_y_axis = image[:, ::-1]
symmetry_by_origin = image[::-1, ::-1]
print("symmetry_by_x_axis dimensions: {}".format(symmetry_by_x_axis.shape))
print("symmetry_by_y_axis dimensions: {}".format(symmetry_by_y_axis.shape))
print("symmetry_by_origin dimensions: {}".format(symmetry_by_origin.shape))

cv2.namedWindow("ORIGINAL", cv2.WINDOW_FREERATIO)
cv2.imshow('ORIGINAL', image)
cv2.waitKey()

cv2.namedWindow("symmetry_by_x_axis", cv2.WINDOW_FREERATIO)
cv2.imshow("symmetry_by_x_axis", symmetry_by_x_axis)
cv2.waitKey()

cv2.namedWindow("symmetry_by_y_axis", cv2.WINDOW_FREERATIO)
cv2.imshow("symmetry_by_y_axis", symmetry_by_y_axis)
cv2.waitKey()

cv2.namedWindow("symmetry_by_origin", cv2.WINDOW_FREERATIO)
cv2.imshow("symmetry_by_origin", symmetry_by_origin)
cv2.waitKey()

cv2.destroyAllWindows()
