# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-17 下午7:43
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import compare_ssim as ssim
from skimage.measure import compare_mse as mes

cap = cv2.VideoCapture(0)

ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)

title = 'camera compare'

plt.ion()  # 交互模式,即不是阻塞模式

ret, frame = cap.read()
temp = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

while cap.isOpened():
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	m = mes(temp, gray)  # 计算两张图之间的均方差 mean-squared error
	s = ssim(temp, gray)  # 计算两张图平均结构相似性指数

	print("MSE:%.2f, SSIM:%.2f" % (m, s))

	temp = gray.copy()
	continue


