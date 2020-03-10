import cv2
import numpy as np

image = cv2.imread('../images/birds2.jpg')

print("image dimensions: {}".format(image.shape))

sol = 150
sag = 750
ust = 100
alt = 300

cropped = image[ust:alt+1, sol:sag+1]

cropped_h, cropped_w = cropped.shape[:2]

print("cropped dimensions: {}".format(cropped.shape))

cv2.namedWindow("cropped", cv2.WINDOW_FREERATIO)
cv2.namedWindow("ORIGINAL", cv2.WINDOW_FREERATIO)
cv2.imshow("cropped", cropped)
cv2.imshow('ORIGINAL', image)

cv2.waitKey()


match_result = cv2.matchTemplate(image, cropped, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(match_result)

top_left = max_loc
bottom_right = (top_left[0] + cropped_w, top_left[1] + cropped_h)

cv2.rectangle(image, top_left, bottom_right, (0,255,255), 4)
cv2.imshow('ORIGINAL', image)

cv2.waitKey()
cv2.destroyAllWindows()
