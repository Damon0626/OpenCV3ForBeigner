# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-17 下午8:02
# @Email : wwymsn@163.com
# @Software: PyCharm

"""
img 输入图像
mask 蒙板图像，确定前景区域，背景区域，不确定区域，可以设置为cv2.GC_BGD,cv2.GC_FGD,cv2.GC_PR_BGD,cv2.GC_PR_FGD，也可以输入0,1,2,3
rect 前景的矩形，格式为（x,y,w,h），分别为左上角坐标和宽度，高度
bdgModel, fgdModel 算法内部是用的数组，只需要创建两个大小为(1,65）np.float64的数组。
iterCount 迭代次数
mode cv2.GC_INIT_WITH_RECT 或 cv2.GC_INIT_WITH_MASK，使用矩阵模式还是蒙板模式。
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('messi5.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (50, 50, 450, 290)

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, iterCount=5, mode=cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
img = img * mask2[:, :, np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()