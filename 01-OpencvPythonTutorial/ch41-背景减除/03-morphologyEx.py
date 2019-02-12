# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-12 下午10:10
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

counter = 0

while True:
	ret, frame = cap.read()
	fgmask = fgbg.apply(frame)
	"""
	morphologyEx(src, op, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) -> dst
	.   @brief Performs advanced morphological transformations.
	.   
	.   The function cv::morphologyEx can perform advanced morphological transformations using an erosion and dilation as
	.   basic operations.
	.   
	.   Any of the operations can be done in-place. In case of multi-channel images, each channel is
	.   processed independently.
	.   
	.   @param src Source image. The number of channels can be arbitrary. The depth should be one of
	.   CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
	.   @param dst Destination image of the same size and type as source image.
	.   @param op Type of a morphological operation, see #MorphTypes
	.   @param kernel Structuring element. It can be created using #getStructuringElement.
	.   @param anchor Anchor position with the kernel. Negative values mean that the anchor is at the
	.   kernel center.
	.   @param iterations Number of times erosion and dilation are applied.
	.   @param borderType Pixel extrapolation method, see #BorderTypes
	.   @param borderValue Border value in case of a constant border. The default value has a special
	.   meaning.
	.   @sa  dilate, erode, getStructuringElement
	.   @note The number of iterations is the number of times erosion or dilatation operation will be applied.
	.   For instance, an opening operation (#MORPH_OPEN) with two iterations is equivalent to apply
	.   successively: erode -> erode -> dilate -> dilate (and not erode -> dilate -> erode -> dilate).
	"""
	fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)  # 利用前120帧进行高级形态学转换

	cv2.imshow('frame', fgmask)
	counter += 1
	print(counter)

	if cv2.waitKey(1) == ord('q'):
		break
cv2.destroyAllWindows()
cap.release()