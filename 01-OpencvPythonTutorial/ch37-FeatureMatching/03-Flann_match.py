# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-26 下午10:06
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import matplotlib.pyplot as plt


img1 = cv2.imread('box.png', 0)
img2 = cv2.imread('box_in_scene.png', 0)

sift = cv2.xfeatures2d.SIFT_create()

kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
seach_params = dict(checks=50)

flann = cv2.FlannBasedMatcher(index_params, seach_params)  # Flann匹配器及其参数
matches = flann.knnMatch(des1, des2, k=2)

matchesMask = [[0, 0] for i in range(len(matches))]

for i, (m, n) in enumerate(matches):
	if m.distance < 0.7 * n.distance:
		matchesMask[i] = [1, 0]

draw_params = dict(matchColor=(0, 255, 0), singlePointColor=(255, 0, 0), matchesMask=matchesMask, flags=0)  # 绘制的参数

img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches, None, **draw_params)
plt.imshow(img3)
plt.show()
