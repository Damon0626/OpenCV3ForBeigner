# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-20 下午8:43
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import matplotlib.pyplot as plt
import numpy as np

'''
图像相减2
'''
img1 = cv2.imread('subtract1.jpg', 0)
img22 = cv2.imread('subtract2.jpg')
img2 = cv2.cvtColor(img22, cv2.COLOR_BGR2GRAY)  # 两种转换为灰度图的方式

st = cv2.subtract(img2, img1)
st[st <= 5] = 0  # 把小于20的像素值设置为0, 0为黑色

pxs = st.ravel()  # 多维降一维，返回的视图，修改影响原始矩阵，np.flattern()返回拷贝，不影响原始矩阵．
pxs = [x for x in pxs if x > 5]
# plt.hist(pxs, 256, [0, 256])  # 256直方图的柱数，range[0, 256]
# plt.show()

ret, threshold = cv2.threshold(st, 50, 255, cv2.THRESH_BINARY)

'''
第二个参数表示轮廓的检索模式，有四种（本文介绍的都是新的cv2接口）：
	cv2.RETR_EXTERNAL表示只检测外轮廓
	cv2.RETR_LIST检测的轮廓不建立等级关系
	cv2.RETR_CCOMP建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。如果内孔内还有一个连通物体，这个物体的边界也在顶层。
	cv2.RETR_TREE建立一个等级树结构的轮廓。

第三个参数method为轮廓的近似办法
	cv2.CHAIN_APPROX_NONE存储所有的轮廓点，相邻的两个点的像素位置差不超过1，即max（abs（x1-x2），abs（y2-y1））==1
	cv2.CHAIN_APPROX_SIMPLE压缩水平方向，垂直方向，对角线方向的元素，只保留该方向的终点坐标，例如一个矩形轮廓只需4个点来保存轮廓信息
	cv2.CHAIN_APPROX_TC89_L1，CV_CHAIN_APPROX_TC89_KCOS使用teh-Chinl chain 近似算法
'''
'''
返回值contours是一个list, list中的每个元素都是图像中的一个轮廓
返回值hierarchy是可选的，每个contours对应４个hierarchy元素，表示后一个轮廓，前一个轮廓，副轮廓，内嵌轮廓的索引编号，如果没有对应项，返回负数
'''
image, contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(contours) 145个轮廓
areas = list()
for i, cnt in enumerate(contours):
	areas.append((i, cv2.contourArea(cnt)))  # [(0, 21188.5), (1, 6.0), (2, 8.0), (3, 2.0),...]

a2 = sorted(areas, key=lambda x: x[1], reverse=True)
#
# for i, are in a2:
# 	if are < 100:
# 		continue
# 	cv2.drawContours(img22, contours, i, (0, 0, 255), 1)  # 画出所有的边界

cnt = contours[0]
hull = cv2.convexHull(cnt)  # 找到包围一组散点的最小凸边形
epsilon1 = 0.001 * cv2.arcLength(hull, True)  # 轮廓周长的0.001
simplified_cnt = cv2.approxPolyDP(hull, epsilon1, True)  # 对指定的点集进行逼近，精度epsilon

epsilon2 = 0.1 * cv2.arcLength(cnt, True)  # 原始轮廓周长
approx = cv2.approxPolyDP(cnt, epsilon2, True)

# cv2.drawContours(img22, [approx], 0, (255, 0, 0), 2)
# cv2.imshow('st', img22)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(approx.shape)  # (4, 1, 2)

# pts = approx.reshape(4, 2)
# rect = np.zeros((4, 2), dtype=np.float32)
# print(pts)
#
# rect[0] = pts[np.argmin(pts[:, 0])]  # 横坐标最小
# rect[2] = pts[np.argmax(pts[:, 0])]
#
# rect[1] = pts[np.argmin(pts[:, 1])]  # 纵坐标最小
# rect[3] = pts[np.argmax(pts[:, 1])]
#
# ratio = image.shape[0]/300.0
# rect *= ratio
# (tl, tr, br, bl) = rect
# widthA = np.sqrt(((br[0] - bl[0])**2) + ((br[1] - bl[1])**2))
# widthB = np.sqrt(((tr[0] - tl[0])**2) + ((tr[1] - tl[1])**2))
#
# heightA = np.sqrt(((tr[0] - br[0])**2) + ((tr[1] - br[1])**2))
# heightB = np.sqrt(((tl[0] - bl[0])**2) + ((tl[1] - bl[1])**2))
#
# maxWidth = int(max(widthA, widthB))
# maxHeight = int(max(heightA, heightB))
#
# dst = np.array([
# 				[0, 0],
# 				[maxWidth -1, 0],
# 				[maxWidth - 1, maxHeight - 1],
# 				[0, maxHeight -1]], dtype=np.float32)
#
# M = cv2.getPerspectiveTransform(rect, dst)
# warp = cv2.warpPerspective(img22, M, (maxWidth, maxHeight))
# cv2.imshow("Final", warp)
# cv2.waitKey(0)