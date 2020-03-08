import cv2
import numpy as np

image = cv2.imread('../images/renkler.png')

print("image dimensions: {}".format(image.shape))

# lower = (0, 150, 0) # b, g ve r değeleri
# upper = (255, 200, 255) # b, g ve r değeleri

# Görsel 3 kanallı olduğu için 3'er değer

# Alttaki değerleri verdiğimiz takdirde normal threshold
# Blue, Green, Red
alt_degerler = (127, 127, 127)
ust_degerler = (255, 255, 255)


result = cv2.inRange(image, alt_degerler, ust_degerler)
print("result dimensions: {}".format(result.shape))

cv2.namedWindow("result", cv2.WINDOW_FREERATIO)
cv2.namedWindow("ORIGINAL", cv2.WINDOW_FREERATIO)
cv2.imshow("result", result)
cv2.imshow('ORIGINAL', image)

cv2.waitKey()

# Blue, Green, Red
alt_degerler2 = (  0,    0,   0)
ust_degerler2 = (255,  100, 100)


result2 = cv2.inRange(image, alt_degerler2, ust_degerler2)
print("result2 dimensions: {}".format(result2.shape))

cv2.namedWindow("result2", cv2.WINDOW_FREERATIO)
cv2.imshow("result2", result2)


cv2.waitKey()
cv2.destroyAllWindows()
