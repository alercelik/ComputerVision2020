import cv2
import numpy as np

img = cv2.imread('../images/renkler.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

B, G, R = cv2.split(img)

edges   = cv2.Canny(gray, 100, 200)
B_edges = cv2.Canny(B, 100, 200)
G_edges = cv2.Canny(G, 100, 200)
R_edges = cv2.Canny(R, 100, 200)

cv2.namedWindow("img", cv2.WINDOW_FREERATIO)
cv2.namedWindow("gray", cv2.WINDOW_FREERATIO)
cv2.namedWindow("edges", cv2.WINDOW_FREERATIO)
cv2.namedWindow("B_edges", cv2.WINDOW_FREERATIO)
cv2.namedWindow("G_edges", cv2.WINDOW_FREERATIO)
cv2.namedWindow("R_edges", cv2.WINDOW_FREERATIO)
cv2.imshow("img"    , img)
cv2.imshow("gray"   , gray)
cv2.imshow("edges"  , edges)
cv2.imshow("B_edges", B_edges)
cv2.imshow("G_edges", G_edges)
cv2.imshow("R_edges", R_edges)


cv2.waitKey()
cv2.destroyAllWindows()
