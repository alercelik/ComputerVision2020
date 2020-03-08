import cv2
import numpy as np

image_path = '../images/renkler.png'

image = cv2.imread(image_path)

print(image.shape)

# Fotoğraf BGR olduğu için B, G, R diye ayırdık (isimlendirdik).
# Fotoğraf CMY (cyan, magenta, yellow) veya HSV (hue, saturation, value)
# gibi farklı renk uzayına sahip olsaydı o zaman o şekilde isimlendirirdik.

B = image[:, :, 0]
G = image[:, :, 1]
R = image[:, :, 2]

print(B.shape)
print(G.shape)
print(R.shape)

# veya
# B, G, R = cv2.split(image)
# "numpy indexing is faster"



gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('ORIGINAL', cv2.WINDOW_FREERATIO)
cv2.namedWindow('B', cv2.WINDOW_FREERATIO)
cv2.namedWindow('G', cv2.WINDOW_FREERATIO)
cv2.namedWindow('R', cv2.WINDOW_FREERATIO)
cv2.namedWindow('grayscale', cv2.WINDOW_FREERATIO)
cv2.imshow('ORIGINAL', image)
cv2.imshow('grayscale', gray)
cv2.imshow('B', B)
cv2.imshow('G', G)
cv2.imshow('R', R)
cv2.waitKey()
