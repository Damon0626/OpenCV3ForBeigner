# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-2-12 下午9:04
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np


cap = cv2.VideoCapture('../ch39-VideoAnalysis/slow.flv')

# params for ShiTomasi corner detection
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

# params for lucas kanade optical flow
lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TermCriteria_COUNT, 10, 0.03))

color = np.random.randint(0, 255, (100, 3))

# 利用第一帧，找到其中的"角点"
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

# 计算光流前需要先初始特征点，Python实例采用的是角点
# 参数介绍：
'''
参数说明：image 输入的单通道图像，可以为8-bit或32-bit

         maxCorners 最大的角点数，如果检测出的角点多余最大角点数，将取出最强最大角点数个角点

         qualityLevel 最小可接受的角点质量

         minDistance 角点间的最小欧几里得距离（也就是两个角点间不能太近）

         corners 输出的检测到的角点

         mask 需要检测角点的区域

         blocksize 计算离散卷积块的大小

         useHarrisDetector 是否使用Harris角点
'''
p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

mask = np.zeros_like(old_frame)  # 返回和old_frame维度一样的全0元素矩阵

while True:
	ret, frame = cap.read()
	frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Calculates an optical flow for a sparse feature set using the iterative Lucas-Kanade method with pyramids
	'''
	参数说明：prevImage 前一帧8-bit图像

            nextImage 当前帧8-bit图像

            prevPts 待跟踪的特征点向量

            nextPts 输出跟踪特征点向量

            status 特征点是否找到，找到的状态为1，未找到的状态为0

            err 输出错误向量，（不太理解用途...）

            winSize 搜索窗口的大小

            maxLevel 最大的金字塔层数

            flags 可选标识：OPTFLOW_USE_INITIAL_FLOW   OPTFLOW_LK_GET_MIN_EIGENVALS
	'''
	p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
	good_new = p1[st == 1]
	good_lod = p0[st == 1]

	# 画出跟踪
	for i, (new, old) in enumerate(zip(good_new, good_lod)):
		a, b = new.ravel()
		c, d = old.ravel()
		mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
		frame = cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)
	img = cv2.add(frame, mask)
	cv2.imshow('frame', img)

	k = cv2.waitKey(30)
	if k == 27:
		break

	old_gray = frame_gray.copy()
	p0 = good_new.reshape(-1, 1, 2)
cv2.destroyAllWindows()
cap.release()