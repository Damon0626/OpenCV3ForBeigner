# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-17 下午8:26
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('messi5.jpg')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (50, 50, 450, 290)

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')
# print(mask2[:, :, np.newaxis].shape)  # 342, 548, 1
# print(img.shape)  # 342, 548, 3
img = img * mask2[:, :, np.newaxis]  # 每个颜色都乘上mask2
plt.imshow(img), plt.colorbar(), plt.show()

newmask = cv2.imread('newmask.jpg', 0)
mask[newmask == 0] = 0
mask[newmask == 255] = 1
mask, bgdModel, fgdModel = cv2.grabCut(img, mask, None, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_MASK)
mask = np.where((mask == 2)|(mask == 0), 0, 1).astype('uint8')

img = img * mask[:, :, np.newaxis]
plt.imshow(img), plt.colorbar(), plt.show()
