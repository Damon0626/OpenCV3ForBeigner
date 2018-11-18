# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-18 下午4:22
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import compare_mse as mes  # 均方误差
from skimage.measure import compare_ssim as ssim  # 结构相似性指数

cap = cv2.VideoCapture(0)
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)


title = 'camera compare'
ret, frame = cap.read()
temp = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

while cap.isOpened():
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	m = mes(temp, gray)
	s = ssim(temp, gray)
	print("MSE: %.2f, SSIM: %.2f" % (m, s))

