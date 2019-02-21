# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-21 下午9:30
# @Email : wwymsn@163.com
# @Software: PyCharm


import numpy as np
import cv2
from imutils.object_detection import non_max_suppression
import imutils


hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture('./礼让斑马线！齐齐哈尔城市文明的伤！.mp4')

fps = cap.get(cv2.CAP_PROP_FPS)  # 25
num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # 获取总帧数

frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

skips = 20

while cap.isOpened():
	ret, frame = cap.read()
	image = frame
	current = cap.get(cv2.CAP_PROP_POS_FRAMES)
	if current % skips != 0:  # 每隔20帧
		continue

	image = imutils.resize(image, width=min(400, image.shape[1]))
	orig = image.copy()

	rects, weight = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

	for (x, y, w, h) in rects:
		cv2.rectangle(orig, (x, y), (x+w, y+h), (0, 0, 255), 2)

	rects = np.array([[x, y, x+w, y+h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

	for (xA, xB, yA, yB) in pick:
		cv2.rectangle(image, (xA, xB), (yA, yB), (0, 255, 0), 2)

	cv2.imshow('Before NMS', orig)
	cv2.imshow('After NMS', image)
	cv2.moveWindow('After NMS', x=0, y=400)

	if cv2.waitKey(1) == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()