import cv2
import numpy as np

image = cv2.imread('../images/renkler.png')

print("image dimensions: {}".format(image.shape))

# BGR'dan HSV'ye çevir
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Görsel 3 kanallı olduğu için 3'er değer

# önceden BGR için aralık vermiştik, artık
# Hue, Saturation, Value
alt_degerler = (30, 127, 90)
ust_degerler = (60, 255, 180)


result = cv2.inRange(hsv_image, alt_degerler, ust_degerler)
print("result dimensions: {}".format(result.shape))

cv2.namedWindow("result", cv2.WINDOW_FREERATIO)
cv2.namedWindow("ORIGINAL", cv2.WINDOW_FREERATIO)
cv2.imshow("result", result)
cv2.imshow('ORIGINAL', image)

cv2.waitKey()
cv2.destroyAllWindows()
