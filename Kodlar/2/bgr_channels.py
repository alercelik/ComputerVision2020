import cv2  # opencv
import numpy as np

# JPEG
# Joint Photohraphers Experts Group
# PNG
# Portable network graphics
# bmp

fotograf_adresi = "../images/renkler.png"

# fotografı oku
image = cv2.imread(fotograf_adresi)
print(image.shape)

cv2.namedWindow('ORIGINAL', cv2.WINDOW_FREERATIO)
cv2.namedWindow('mavi', cv2.WINDOW_FREERATIO)
cv2.namedWindow('yesil', cv2.WINDOW_FREERATIO)
cv2.namedWindow('kirmizi', cv2.WINDOW_FREERATIO)

# fotoğrafı göster
cv2.imshow("ORIGINAL", image)
cv2.waitKey()

mavi = image.copy()
mavi[:,:,1] = 0
mavi[:,:,2] = 0

yesil = image.copy()
yesil[:,:,0] = 0
yesil[:,:,2] = 0

kirmizi = image.copy()
kirmizi[:,:,0] = 0
kirmizi[:,:,1] = 0

cv2.imshow("mavi", mavi)
cv2.imshow("yesil", yesil)
cv2.imshow("kirmizi", kirmizi)

cv2.waitKey()
cv2.destroyAllWindows()


# 255 beyaz
# 0 siyah
# 127 gri
# 200 açık gri

# bos_fotograf = np.zeros((100,100), dtype="uint8")

# for i in range(bos_fotograf.shape[0]):
# 	bos_fotograf[i] = 255 - (i*2.55)

# # fotoğrafı göster
# cv2.namedWindow("Simsiyah", cv2.WINDOW_FREERATIO)
# cv2.imshow("Simsiyah", bos_fotograf)
# cv2.waitKey()
# cv2.destroyAllWindows()
