import cv2
import numpy as np

# 0 -> default camera (genelde dahili webcam)
# usb kameraları için vs. 1, 2 vs..
# başka video'lar için aşağıdaki 0 parametresi yerine
# video'nun path'ini verin
video_path = 0
# video_path = "../videos/video.mp4"

camera = cv2.VideoCapture(video_path)

# Hue, Saturation, Value
alt_degerler = (0, 127, 127)
ust_degerler = (5, 255, 255)

alt_degerler2 = (175, 127, 127)
ust_degerler2 = (180, 255, 255)


_, frame = camera.read()

# tek kanallı bos frame oluştur
tracking_frame = np.zeros_like(frame[:,:,0])

kernel = np.ones((5,5), dtype=np.uint8)
opencv_major_version = int(cv2.__version__.split(".")[0])

def contourCenter(contour):
	# compute the center of the contour
	M = cv2.moments(contour)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])

	return cX, cY  # centerX, centerY


# döngüden çıkmak için terminal üstündeyken ctrl+c yapın.
while True:
	_, frame = camera.read()

	blurred = cv2.blur(frame, (5,5))
	
	hsv_frame = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

	# görüntü HSV renk uzayında olduğu için alt ve üst değeleri
	# HSV formatında ayarlamamız gerekli.
	result1 = cv2.inRange(hsv_frame, alt_degerler, ust_degerler)
	result2 = cv2.inRange(hsv_frame, alt_degerler2, ust_degerler2)

	result = cv2.bitwise_or(result1, result2)

	#result_eroded = cv2.erode(result, kernel)

	if opencv_major_version < 4:  #opencv 2 and 3
		_, contours, hierarchy = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	else: # opencv 4
		contours, hierarchy = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	if len(contours) > 0:
		en_buyuk_contour = max(contours, key = cv2.contourArea)

		#for contour in contours:
		#	if cv2.contourArea(contour) > 100:
		#		cX, cY = contourCenter(contour)
		#		cv2.circle(tracking_frame, (cX, cY), 3, 255, -1)

		if cv2.contourArea(en_buyuk_contour) > 100:
			cX, cY = contourCenter(en_buyuk_contour)
			cv2.circle(tracking_frame, (cX, cY), 3, 255, -1)

		
	solma_hizi = 5
	tracking_frame[tracking_frame>0] -= solma_hizi

	cv2.imshow("frame", frame)
	cv2.imshow("result", result)
	cv2.imshow("tracking_frame", tracking_frame)
	#cv2.imshow("result_eroded", result_eroded)
	# alttaki waitKey bizim işimize yaramasa bile (30 ms bekliyor) gerekli.
	basilan_tus = cv2.waitKey(30)

	if basilan_tus == ord("q"):
		break

cv2.destroyAllWindows()
