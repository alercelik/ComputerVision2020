import cv2
import numpy as np
#import mouse

image = cv2.imread('../images/renkler.png')
print(image.shape)
	
#                 Blue, Green, Red
en_alt_degerler = (0,   100,   0)
en_ust_degerler = (100, 255,   255)

result = cv2.inRange(image, en_alt_degerler, en_ust_degerler)

cv2.namedWindow("result", cv2.WINDOW_FREERATIO)
cv2.imshow("result", result)


cv2.namedWindow("ORIGINAL", cv2.WINDOW_FREERATIO)
cv2.imshow('ORIGINAL', image)
cv2.waitKey()


_, contours, hierarchy = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))


def contourCenter(contour):
	# compute the center of the contour
	M = cv2.moments(contour)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])

	return cX, cY  # centerX, centerY


for c in contours:
	if cv2.contourArea(c) > 100:
		cX, cY = contourCenter(c)
		#print(c)

		#cv2.circle()

		print("kontorun merkezi = {}".format((cX, cY)))

		dikdortgen = cv2.boundingRect(c)
		cember     = cv2.minEnclosingCircle(c)

		cv2.rectangle(image, (int(dikdortgen[0]), int(dikdortgen[1])), (int(dikdortgen[0]+dikdortgen[2]), int(dikdortgen[1]+dikdortgen[3])), (255, 0, 255), 9)
		cv2.circle(image, (cX, cY), int(cember[1]), (0, 255, 255), 9)
	

		print(dikdortgen)
		print(cember)

		#mouse.move(ekran_sol + cX, ekran_ust + cY)
		#mouse.click()

		cv2.circle(image, (cX, cY), 15, (255, 255, 255), -1)
		cv2.imshow('ORIGINAL', image)
		cv2.waitKey()
	else:
		print("Alan 100'den düşük, işlem yapma")
		#cv2.circle(image, (cX, cY), 7, (0, 0, 0), -1)
		#cv2.waitKey()

cv2.imshow('ORIGINAL', image)
cv2.waitKey()


