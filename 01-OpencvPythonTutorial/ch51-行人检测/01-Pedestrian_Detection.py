# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-21 下午9:01
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
import path
import imutils
from imutils.object_detection import non_max_suppression

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())  # 返回SVM参数，用于对SVM进行设置．

for image in ['p1.jpg', 'p2.jpg', 'p3.jpg', 'p4.JPG']:
	img = cv2.imread(image)
	img = imutils.resize(img, min(400, img.shape[1]))
	orig = img.copy()

	# Detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles.
	rects, weights = hog.detectMultiScale(img, winStride=(4, 4), padding=(8, 8), scale=1.05)

	for (x, y, w, h) in rects:
		cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

	rects = np.array([[x, y, x+w, y+h] for (x, y, w, h) in rects])
	pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

	for (xA, yA, xB, yB) in pick:
		cv2.rectangle(img, (xA, yA), (xB, yB), (0, 255, 0), 2)

	cv2.imshow("Before NMS", orig)
	cv2.moveWindow('Before NMS', x=0, y=0)
	cv2.imshow("After NMS", img)
	cv2.moveWindow("After NMS", x=orig.shape[1], y=0)
	if cv2.waitKey(0) == ord('q'):
		break
cv2.destroyAllWindows()