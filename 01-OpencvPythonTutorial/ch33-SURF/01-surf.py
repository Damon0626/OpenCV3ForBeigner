# -*-coding:utf-8-*-
# @Author: Damon0626
# @Time  : 19-1-18 下午11:21
# @Email : wwymsn@163.com
# @Software: PyCharm


import cv2
import matplotlib.pyplot as plt

img = cv2.imread('butterfly.jpg', 0)
surf = cv2.xfeatures2d.SURF_create(400)

kp, des = surf.detectAndCompute(img, None)
print(len(kp))  # 1330

print(surf.getHessianThreshold())  # 400

surf.setHessianThreshold(50000)
kp, des = surf.detectAndCompute(img, None)
print(len(kp))  # 48

img2 = cv2.drawKeypoints(img, kp, None, (255, 0, 0), 4)
plt.imshow(img2)
plt.show()