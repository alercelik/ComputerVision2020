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
alt_degerler = (30, 127, 90)
ust_degerler = (60, 255, 180)

# döngüden çıkmak için terminal üstündeyken ctrl+c yapın.
while True:
	_, frame = camera.read()
	hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# görüntü HSV renk uzayında olduğu için alt ve üst değeleri
	# HSV formatında ayarlamamız gerekli.
	result = cv2.inRange(hsv_frame, alt_degerler, ust_degerler)

	cv2.imshow("frame", frame)
	cv2.imshow("result", result)
	# alttaki waitKey bizim işimize yaramasa bile (30 ms bekliyor) gerekli.
	cv2.waitKey(30)
