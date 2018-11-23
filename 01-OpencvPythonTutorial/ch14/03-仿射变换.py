# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 18-11-23 下午8:34
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("drawing.png")
rows, cols, ch = img.shape
print(img.shape)

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)
print(M)

dst = cv2.warpAffine(img, M, (cols, rows))

plt.figure(figsize=(8, 7), dpi=98)
p1 = plt.subplot(211)
p1.imshow(img)
p1.set_title('Input')

p2 = plt.subplot(212)
p2.imshow(dst)
p2.set_title('Output')
plt.show()