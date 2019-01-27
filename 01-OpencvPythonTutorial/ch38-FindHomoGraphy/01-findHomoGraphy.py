# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-27 下午10:51
# @Email : wwymsn@163.com
# @Software: PyCharm

import cv2
import numpy as np
import matplotlib.pyplot as plt


MIN_MATCH_COUNT = 10
img1 = cv2.imread('../ch37-FeatureMatching/box.png', 0)
img2 = cv2.imread('../ch37-FeatureMatching/box_in_scene.png', 0)

sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)

good = []
for m, n in matches:
	if m.distance < 0.7 * n.distance:
		good.append(m)

if len(good) > MIN_MATCH_COUNT:
	src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
	dst_pts = np.float32([kp2[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)

	'''
	# 第三个参数 Method used to computed a homography matrix. The following methods are possible:
		#0 - a regular method using all the points
		#CV_RANSAC - RANSAC-based robust method
		#CV_LMEDS - Least-Median robust method
		# 第四个参数取值范围在 1 到 10 , 绝一个点对的阈值。原图像的点经过变换后点与目标图像上对应点的误差
		# 超过误差就认为是 outlier
		# 返回值中 H 为变换矩阵。mask是掩模，online的点
		H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
	'''
	M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
	matchesMask = mask.ravel().tolist()

	h, w = img1.shape

	pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
	dst = cv2.perspectiveTransform(pts, M)

	img2 = cv2.polylines(img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
else:
	print("Not enough matches are found - %d/%d"(len(good), MIN_MATCH_COUNT))
	matchesMask = None

draw_params = dict(matchColor=(0, 255, 0), singlePointColor=None, matchesMask=matchesMask, flags=2)
img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)

plt.imshow(img3, 'gray')
plt.show()